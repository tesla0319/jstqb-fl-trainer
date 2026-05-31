"""問題テーブルの DB 操作層。

JSTQB FL 新 API 用関数と、旧 SQL Silver API との後方互換関数を両方持つ。
"""

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.choice import Choice
from app.models.question import Question
from app.models.user_answer import UserAnswer


def get_questions(
    db: Session,
    category: str | None = None,
    limit: int = 40,
) -> list[Question]:
    """問題一覧を取得する（JSTQB FL /api/v1/questions 用）。"""
    query = db.query(Question)
    if category is not None:
        query = query.filter(Question.category == category)
    return query.limit(limit).all()


def get_random_question(
    db: Session,
    category: str | None = None,
    exclude_ids: list[int] | None = None,
    excluded_categories: list[str] | None = None,
) -> Question | None:
    """ランダムに1問取得する。

    新 JSTQB FL API と旧 SQL Silver API の両方から呼ばれる。
    - 新 API: category のみ使用
    - 旧 API: exclude_ids / excluded_categories も使用
    """
    query = db.query(Question)
    if category:
        query = query.filter(Question.category == category)
    if exclude_ids:
        query = query.filter(Question.id.notin_(exclude_ids))
    if excluded_categories:
        query = query.filter(Question.category.notin_(excluded_categories))
    return query.order_by(func.random()).first()


def get_question_by_id(db: Session, question_id: int) -> Question | None:
    """ID で問題を取得する。"""
    return db.query(Question).filter(Question.id == question_id).first()


def get_choice_by_id(db: Session, choice_id: int) -> Choice | None:
    """ID で選択肢を取得する（JSTQB FL /api/v1/answers 用）。"""
    return db.query(Choice).filter(Choice.id == choice_id).first()


def get_wrong_question_ids(db: Session, user_name: str = "guest") -> list[int]:
    """最直近の回答が不正解だった question_id のリストを返す（旧 review モード用）。"""
    latest_subq = (
        db.query(
            UserAnswer.question_id,
            func.max(UserAnswer.id).label("max_id"),
        )
        .filter(UserAnswer.user_name == user_name)
        .group_by(UserAnswer.question_id)
        .subquery()
    )

    rows = (
        db.query(UserAnswer.question_id)
        .join(
            latest_subq,
            (UserAnswer.question_id == latest_subq.c.question_id)
            & (UserAnswer.id == latest_subq.c.max_id),
        )
        .filter(UserAnswer.is_correct == False)  # noqa: E712
        .filter(UserAnswer.user_name == user_name)
        .all()
    )

    return [r.question_id for r in rows]
