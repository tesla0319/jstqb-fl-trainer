"""DB 初期化スクリプト。

処理内容:
    1. テーブルを作成（既存テーブルはスキップ）
    2. 問題を投入（既にデータがある場合はスキップ）

DBテーブル構造変更なし。categories テーブルは作成しない。
カテゴリ一覧は config.JSTQB_CATEGORIES から提供する。
"""

from sqlalchemy.orm import Session

from app.database import Base, SessionLocal, engine
from app.models import Question, Choice  # noqa: F401
from app.seed.sample_questions import SAMPLE_QUESTIONS


def create_tables() -> None:
    """全テーブルを作成する。既存テーブルは変更しない。"""
    Base.metadata.create_all(bind=engine)
    print("テーブルを作成しました（既存テーブルはスキップ）。")


def seed_questions(db: Session) -> None:
    """問題を投入する。既にデータがある場合はスキップする。"""
    existing_count = db.query(Question).count()
    if existing_count > 0:
        print(f"既に {existing_count} 件の問題が存在するためスキップします。")
        return

    for q_data in SAMPLE_QUESTIONS:
        q_dict = dict(q_data)
        choices_data = q_dict.pop("choices")

        question = Question(**q_dict)
        db.add(question)
        db.flush()

        for c_data in choices_data:
            choice = Choice(question_id=question.id, **c_data)
            db.add(choice)

    db.commit()
    print(f"{len(SAMPLE_QUESTIONS)} 件の問題を投入しました。")


def main() -> None:
    create_tables()
    db = SessionLocal()
    try:
        seed_questions(db)
    finally:
        db.close()


if __name__ == "__main__":
    main()
