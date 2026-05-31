"""JSTQB FL seed データ（sample_questions.py）の品質テスト。

DB 不要。Python リストを直接検証する。

仕様書 §4.3 / §6.2 の要件:
  - 全82問
  - 全6カテゴリを最低1問カバー
  - 全問単一選択（multi_select_count=1）
  - 全問で is_correct=True の選択肢が必ず1件だけ存在する
  - 全問に explanation がある
"""

from app.config import JSTQB_CATEGORIES
from app.seed.sample_questions import SAMPLE_QUESTIONS

EXPECTED_CATEGORY_NAMES = {c["name"] for c in JSTQB_CATEGORIES}


class TestSeedCoverage:

    def test_total_question_count(self):
        """Phase 1 + MD追加: 82問。"""
        assert len(SAMPLE_QUESTIONS) == 82, (
            f"問題数: {len(SAMPLE_QUESTIONS)} (82問必要)"
        )

    def test_all_categories_covered(self):
        """全6カテゴリが最低1問ずつカバーされている。"""
        covered = {q["category"] for q in SAMPLE_QUESTIONS}
        missing = EXPECTED_CATEGORY_NAMES - covered
        assert missing == set(), f"未カバーカテゴリ: {sorted(missing)}"

    def test_category_names_match_config(self):
        """全問題の category 名が JSTQB_CATEGORIES に含まれる（typo 検出）。"""
        invalid = {q["category"] for q in SAMPLE_QUESTIONS} - EXPECTED_CATEGORY_NAMES
        assert invalid == set(), f"未定義カテゴリ名: {invalid}"

    def test_all_single_select(self):
        """全問 multi_select_count=1（JSTQB FL は単一選択のみ）。"""
        errors = [
            f"Q{i} ({q['category']}): multi_select_count={q['multi_select_count']}"
            for i, q in enumerate(SAMPLE_QUESTIONS)
            if q["multi_select_count"] != 1
        ]
        assert errors == [], f"単一選択でない問題: {errors}"

    def test_all_four_choices(self):
        """全問4択（選択肢4つ）。"""
        errors = [
            f"Q{i} ({q['category']}): 選択肢数={len(q['choices'])}"
            for i, q in enumerate(SAMPLE_QUESTIONS)
            if len(q["choices"]) != 4
        ]
        assert errors == [], f"4択でない問題: {errors}"

    def test_exactly_one_correct_per_question(self):
        """全問で is_correct=True の選択肢が必ず1件だけ存在する。"""
        errors = []
        for i, q in enumerate(SAMPLE_QUESTIONS):
            correct_count = sum(1 for c in q["choices"] if c["is_correct"])
            if correct_count != 1:
                errors.append(f"Q{i} ({q['category']}): 正解数={correct_count}")
        assert errors == [], "\n".join(errors)

    def test_no_question_without_correct_choice(self):
        """is_correct=True が0件の問題が存在しない。"""
        errors = [
            f"Q{i} ({q['category']})"
            for i, q in enumerate(SAMPLE_QUESTIONS)
            if not any(c["is_correct"] for c in q["choices"])
        ]
        assert errors == [], f"正解選択肢がない問題: {errors}"

    def test_no_question_with_multiple_correct_choices(self):
        """is_correct=True が2件以上の問題が存在しない。"""
        errors = [
            f"Q{i} ({q['category']}): 正解数={sum(1 for c in q['choices'] if c['is_correct'])}"
            for i, q in enumerate(SAMPLE_QUESTIONS)
            if sum(1 for c in q["choices"] if c["is_correct"]) > 1
        ]
        assert errors == [], f"正解が複数ある問題: {errors}"

    def test_all_questions_have_explanation(self):
        """全問に explanation がある（空文字・None 不可）。"""
        missing = [
            f"Q{i} ({q['category']})"
            for i, q in enumerate(SAMPLE_QUESTIONS)
            if not q.get("explanation")
        ]
        assert missing == [], f"explanation がない問題: {missing}"

    def test_display_order_unique_per_question(self):
        """各問題内で display_order が重複しない。"""
        errors = []
        for i, q in enumerate(SAMPLE_QUESTIONS):
            orders = [c["display_order"] for c in q["choices"]]
            if len(orders) != len(set(orders)):
                errors.append(f"Q{i} ({q['category']}): display_order 重複")
        assert errors == [], "\n".join(errors)

    def test_difficulty_range(self):
        """difficulty が 1〜3 の範囲内。"""
        errors = [
            f"Q{i} ({q['category']}): difficulty={q['difficulty']}"
            for i, q in enumerate(SAMPLE_QUESTIONS)
            if q["difficulty"] not in (1, 2, 3)
        ]
        assert errors == [], f"difficulty 範囲外: {errors}"

    def test_category_distribution(self):
        """各カテゴリの問題数が仕様に合致する。"""
        expected = {
            "テストの基礎": 18,
            "テスト活動とプロセス": 17,
            "静的テスト": 9,
            "テスト技法": 15,
            "テストマネジメント": 16,
            "ツール支援": 7,
        }
        actual = {}
        for q in SAMPLE_QUESTIONS:
            actual[q["category"]] = actual.get(q["category"], 0) + 1
        assert actual == expected, f"配分不一致: 実際={actual} 期待={expected}"
