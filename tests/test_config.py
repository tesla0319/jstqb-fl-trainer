"""config.py の整合性テスト。"""

from app.config import CATEGORIES, JSTQB_CATEGORIES


def test_categories_unique():
    """CATEGORIES に重複がないこと。"""
    assert len(CATEGORIES) == len(set(CATEGORIES)), \
        f"CATEGORIES に重複があります: {CATEGORIES}"


def test_jstqb_categories_count():
    """JSTQB_CATEGORIES が6件であること。"""
    assert len(JSTQB_CATEGORIES) == 6


def test_jstqb_categories_have_id_and_name():
    """各カテゴリに id と name があること。"""
    for cat in JSTQB_CATEGORIES:
        assert "id" in cat
        assert "name" in cat


def test_sample_questions_use_valid_categories():
    """全サンプル問題のカテゴリが config.CATEGORIES に含まれること。"""
    from app.seed.sample_questions import SAMPLE_QUESTIONS

    invalid = [
        q for q in SAMPLE_QUESTIONS
        if q["category"] not in CATEGORIES
    ]
    assert not invalid, (
        f"未定義カテゴリを使う問題があります: "
        f"{[(q.get('id', '?'), q['category']) for q in invalid]}"
    )
