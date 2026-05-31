"""pytest フィクスチャ定義（JSTQB FL 版）。

テスト方針:
- インメモリ SQLite を使用し、本番の app.db と完全に分離する
- 各テスト関数は独立して動く（フィクスチャスコープは function）
- FastAPI の Depends(get_db) を dependency_overrides で差し替えてテスト用 DB を使う
- categories テーブルは存在しない（config.JSTQB_CATEGORIES から提供）
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db
import app.models as _models  # noqa: F401
from app.models.question import Question
from app.models.choice import Choice

TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture
def db_engine():
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session(db_engine):
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
def seeded_db(db_session):
    """テスト用DBにサンプル問題を投入する。

    投入内容:
    - q1: テストの基礎（単一選択、選択肢4つ）
    - q2: テスト活動とプロセス（単一選択、選択肢4つ）
    """
    q1 = Question(
        category="テストの基礎",
        difficulty=1,
        question_text="テスト基礎のサンプル問題",
        multi_select_count=1,
        explanation="テスト基礎の解説です。",
    )
    db_session.add(q1)
    db_session.flush()
    q1_id = q1.id

    q1_c1 = Choice(question_id=q1_id, choice_text="正解A",  is_correct=True,  display_order=1)
    q1_c2 = Choice(question_id=q1_id, choice_text="不正解B", is_correct=False, display_order=2)
    q1_c3 = Choice(question_id=q1_id, choice_text="不正解C", is_correct=False, display_order=3)
    q1_c4 = Choice(question_id=q1_id, choice_text="不正解D", is_correct=False, display_order=4)
    db_session.add_all([q1_c1, q1_c2, q1_c3, q1_c4])
    db_session.flush()
    q1_correct_id   = q1_c1.id
    q1_incorrect_id = q1_c2.id

    q2 = Question(
        category="テスト活動とプロセス",
        difficulty=2,
        question_text="テスト活動のサンプル問題",
        multi_select_count=1,
        explanation="テスト活動の解説です。",
    )
    db_session.add(q2)
    db_session.flush()
    q2_id = q2.id

    q2_c1 = Choice(question_id=q2_id, choice_text="正解E",  is_correct=True,  display_order=1)
    q2_c2 = Choice(question_id=q2_id, choice_text="不正解F", is_correct=False, display_order=2)
    q2_c3 = Choice(question_id=q2_id, choice_text="不正解G", is_correct=False, display_order=3)
    q2_c4 = Choice(question_id=q2_id, choice_text="不正解H", is_correct=False, display_order=4)
    db_session.add_all([q2_c1, q2_c2, q2_c3, q2_c4])
    db_session.flush()
    q2_correct_id            = q2_c1.id
    q2_choice_for_cross_test = q2_c1.id  # q1 への送信でクロステスト用

    db_session.commit()

    return {
        "q1_id":                    q1_id,
        "q1_correct_choice_id":     q1_correct_id,
        "q1_incorrect_choice_id":   q1_incorrect_id,
        "q2_id":                    q2_id,
        "q2_correct_choice_id":     q2_c1.id,
        "q2_incorrect_choice_id":   q2_c2.id,
        "q2_choice_for_cross_test": q2_choice_for_cross_test,
    }
