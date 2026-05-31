"""GET /api/stats/categories のAPIテスト。

stats 機能はJSTQB FL仕様書のスコープ外だが、既存機能として維持する。
"""

import json

from app.models.question import Question
from app.models.choice import Choice
from app.models.user_answer import UserAnswer


def _add_answers(
    db_session,
    question_id: int,
    is_correct: bool,
    count: int,
    user_name: str = "guest",
) -> None:
    """指定数の回答履歴を直接 DB に挿入する。"""
    for _ in range(count):
        db_session.add(UserAnswer(
            question_id=question_id,
            selected_choices=json.dumps([]),
            is_correct=is_correct,
            user_name=user_name,
        ))
    db_session.commit()


def _make_question(db_session, category: str) -> tuple[int, int]:
    """最小構成の問題と選択肢を作成し (question_id, correct_choice_id) を返す。"""
    q = Question(
        category=category,
        difficulty=1,
        question_text=f"{category}テスト問題",
        multi_select_count=1,
        explanation="解説",
    )
    db_session.add(q)
    db_session.flush()
    q_id = q.id

    c = Choice(question_id=q_id, choice_text="正解", is_correct=True, display_order=1)
    db_session.add(c)
    db_session.flush()
    c_id = c.id

    db_session.commit()
    return q_id, c_id


class TestCategoryStats:

    def test_empty_when_no_answers(self, client, seeded_db):
        """全カテゴリ未着手 → stats: []。"""
        response = client.get("/api/stats/categories")
        assert response.status_code == 200
        assert response.json() == {"stats": []}

    def test_shows_category_after_answer(self, client, db_session):
        """回答後はそのカテゴリの統計が現れる。"""
        q_id, _ = _make_question(db_session, "テストの基礎")
        _add_answers(db_session, q_id, is_correct=True, count=1)

        response = client.get("/api/stats/categories")
        stats = response.json()["stats"]
        assert len(stats) == 1
        s = stats[0]
        assert s["category"] == "テストの基礎"
        assert s["answered_count"] == 1
        assert s["correct_count"] == 1
        assert s["accuracy"] == 1.0

    def test_accuracy_calculation(self, client, db_session):
        """正答率 = correct_count / answered_count が正しく計算される。"""
        q_id, _ = _make_question(db_session, "テストの基礎")
        _add_answers(db_session, q_id, is_correct=True,  count=1)
        _add_answers(db_session, q_id, is_correct=False, count=3)

        stats = client.get("/api/stats/categories").json()["stats"]
        s = next(x for x in stats if x["category"] == "テストの基礎")
        assert s["answered_count"] == 4
        assert s["correct_count"] == 1
        assert abs(s["accuracy"] - 0.25) < 1e-9

    def test_excludes_unanswered_categories(self, client, db_session):
        """回答済みカテゴリのみ返す（answered=0 のカテゴリは含めない）。"""
        q1_id, _ = _make_question(db_session, "テストの基礎")
        _make_question(db_session, "テスト活動とプロセス")  # 回答しない

        _add_answers(db_session, q1_id, is_correct=True, count=1)

        stats = client.get("/api/stats/categories").json()["stats"]
        categories = [s["category"] for s in stats]
        assert "テストの基礎" in categories
        assert "テスト活動とプロセス" not in categories

    def test_multiple_categories(self, client, db_session):
        """複数カテゴリを回答すると、それぞれの統計が返る。"""
        q1_id, _ = _make_question(db_session, "テストの基礎")
        q2_id, _ = _make_question(db_session, "テスト活動とプロセス")

        _add_answers(db_session, q1_id, is_correct=True, count=1)
        _add_answers(db_session, q2_id, is_correct=True, count=1)

        stats = client.get("/api/stats/categories").json()["stats"]
        assert len(stats) == 2


class TestUserIsolation:
    """ユーザー別データ分離テスト。"""

    def test_stats_isolated_per_user(self, client, db_session):
        """alice と bob の統計が互いに干渉しない。"""
        q1_id, _ = _make_question(db_session, "テストの基礎")
        q2_id, _ = _make_question(db_session, "テスト活動とプロセス")

        _add_answers(db_session, q1_id, is_correct=False, count=3, user_name="alice")
        _add_answers(db_session, q2_id, is_correct=False, count=3, user_name="bob")

        alice_stats = client.get("/api/stats/categories?user_name=alice").json()["stats"]
        bob_stats   = client.get("/api/stats/categories?user_name=bob").json()["stats"]

        assert len(alice_stats) == 1
        assert alice_stats[0]["category"] == "テストの基礎"
        assert len(bob_stats) == 1
        assert bob_stats[0]["category"] == "テスト活動とプロセス"

    def test_guest_user_isolated_from_named_user(self, client, db_session):
        """guest と alice のデータが分離される。"""
        q1_id, _ = _make_question(db_session, "テストの基礎")
        q2_id, _ = _make_question(db_session, "テスト活動とプロセス")

        _add_answers(db_session, q1_id, is_correct=True, count=3, user_name="guest")
        _add_answers(db_session, q2_id, is_correct=True, count=3, user_name="alice")

        guest_stats = client.get("/api/stats/categories").json()["stats"]
        assert any(s["category"] == "テストの基礎"          for s in guest_stats)
        assert not any(s["category"] == "テスト活動とプロセス" for s in guest_stats)

        alice_stats = client.get("/api/stats/categories?user_name=alice").json()["stats"]
        assert any(s["category"] == "テスト活動とプロセス"    for s in alice_stats)
        assert not any(s["category"] == "テストの基礎"        for s in alice_stats)
