"""問題取得 API エンドポイント。

router       : /api/v1/questions  （JSTQB FL 新 API）
legacy_router: /api/questions     （旧 SQL Silver API、後方互換で維持）
"""

import random
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import config
from app.crud.question import (
    get_question_by_id,
    get_questions,
    get_random_question,
    get_wrong_question_ids,
)
from app.crud.stats import get_category_stats
from app.database import get_db
from app.schemas.question import LegacyQuestionResponse, QuestionsListResponse
from app.services.stats import CategoryStat, compute_accuracy, get_weak_categories

# ── JSTQB FL 新 API ────────────────────────────────────────────────

router = APIRouter(prefix="/api/v1/questions", tags=["questions"])


@router.get("", response_model=QuestionsListResponse)
def list_questions(
    category_id: int | None = Query(default=None),
    random: bool = Query(default=False),
    limit: int = Query(default=config.DEFAULT_QUESTION_LIMIT, ge=1),
    exclude_ids: list[int] = Query(default=[]),
    db: Session = Depends(get_db),
):
    """問題一覧を取得する。

    - random=true のとき limit を無視して1問をランダムに返す。
    - category_id 指定時は config から名称を引いてカテゴリで絞り込む。
    - exclude_ids 指定時はそれらの問題IDを除外してランダム取得する。
    - 対象問題が0件の場合は {"questions": []} を返す（404 ではない）。
    """
    category_name = _resolve_category_name(category_id)
    if category_id is not None and category_name is None:
        # config に存在しない category_id → 0件
        return QuestionsListResponse(questions=[])

    if random:
        question = get_random_question(db, category=category_name, exclude_ids=exclude_ids or None)
        questions = [question] if question else []
    else:
        questions = get_questions(db, category=category_name, limit=limit)

    return QuestionsListResponse(questions=questions)


@router.get("/{question_id}", response_model=QuestionsListResponse)
def get_question(question_id: int, db: Session = Depends(get_db)):
    """問題を1件取得する。存在しない場合は 404 を返す。"""
    question = get_question_by_id(db, question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return QuestionsListResponse(questions=[question])


def _resolve_category_name(category_id: int | None) -> str | None:
    """category_id を config のカテゴリ名に変換する。見つからない場合は None。"""
    if category_id is None:
        return None
    cat_map = {c["id"]: c["name"] for c in config.JSTQB_CATEGORIES}
    return cat_map.get(category_id)


# ── 旧 SQL Silver API（後方互換、未使用のまま維持） ────────────────

legacy_router = APIRouter(prefix="/api/questions", tags=["questions-legacy"])


def _random_with_fallback(
    db: Session,
    *,
    category: str | None,
    exclude_ids: list[int],
    excluded_categories: list[str] | None = None,
):
    question = get_random_question(
        db, category=category,
        exclude_ids=exclude_ids or None,
        excluded_categories=excluded_categories or None,
    )
    if question is None and exclude_ids:
        question = get_random_question(
            db, category=category,
            exclude_ids=None,
            excluded_categories=excluded_categories or None,
        )
    if question is None and excluded_categories:
        question = get_random_question(
            db, category=category,
            exclude_ids=exclude_ids or None,
            excluded_categories=None,
        )
    return question


@legacy_router.get("/random", response_model=LegacyQuestionResponse)
def random_question(
    mode: Literal["normal", "weak", "review"] = "normal",
    category: str | None = None,
    exclude_ids: list[int] = Query(default=[]),
    user_name: str = Query(default="guest", min_length=1, max_length=50),
    excluded_categories: list[str] = Query(default=[]),
    db: Session = Depends(get_db),
):
    """ランダムに1問取得する（旧 API）。"""
    question = None

    if mode == "weak":
        question = _resolve_weak(db, exclude_ids, user_name=user_name)
    elif mode == "review":
        question = _resolve_review(db, exclude_ids, user_name=user_name)

    if question is None:
        question = _random_with_fallback(
            db, category=category, exclude_ids=exclude_ids,
            excluded_categories=excluded_categories or None,
        )

    if question is None:
        raise HTTPException(status_code=404, detail="No questions found")

    return question


def _resolve_weak(db: Session, exclude_ids: list[int], user_name: str = "guest"):
    raw_stats = get_category_stats(db, user_name=user_name)
    stats = [
        CategoryStat(
            category=row.category,
            answered_count=row.answered_count,
            correct_count=row.correct_count,
            accuracy=compute_accuracy(row.answered_count, row.correct_count),
        )
        for row in raw_stats
    ]
    weak_cats = get_weak_categories(
        stats,
        weak_threshold=config.WEAK_THRESHOLD,
        min_answers=config.MIN_ANSWERS,
    )
    if not weak_cats:
        return None
    target_category = random.choice(weak_cats)
    return _random_with_fallback(db, category=target_category, exclude_ids=exclude_ids)


def _resolve_review(db: Session, exclude_ids: list[int], user_name: str = "guest"):
    wrong_ids = get_wrong_question_ids(db, user_name=user_name)
    if not wrong_ids:
        return None
    exclude_set = set(exclude_ids)
    candidates = [qid for qid in wrong_ids if qid not in exclude_set]
    if not candidates:
        candidates = wrong_ids
    chosen_id = random.choice(candidates)
    return get_question_by_id(db, chosen_id)
