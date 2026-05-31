"""回答送信・正誤判定 API エンドポイント。

router       : /api/v1/answers  （JSTQB FL 新 API、単一選択）
legacy_router: /api/answers     （旧 SQL Silver API、複数選択対応、後方互換で維持）
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import config
from app.crud.answer import create_user_answer, delete_all_answers
from app.crud.question import get_choice_by_id, get_question_by_id
from app.database import get_db
from app.schemas.answer import (
    AnswerRequest,
    AnswerResponse,
    LegacyAnswerRequest,
    LegacyAnswerResponse,
)
from app.services.grading import grade_answer

# ── JSTQB FL 新 API ────────────────────────────────────────────────

router = APIRouter(prefix="/api/v1/answers", tags=["answers"])


@router.post("", response_model=AnswerResponse)
def submit_answer(body: AnswerRequest, db: Session = Depends(get_db)):
    """回答を送信して正誤を判定する（単一選択）。

    バリデーション順序:
    1. question_id が存在しない → 404
    2. choice_id が存在しない → 404
    3. choice_id が question_id に属していない → 400
    4. 型不正（Pydantic） → 422
    """
    question = get_question_by_id(db, body.question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")

    choice = get_choice_by_id(db, body.choice_id)
    if choice is None:
        raise HTTPException(status_code=404, detail="Choice not found")

    if choice.question_id != question.id:
        raise HTTPException(
            status_code=400,
            detail="choice_id does not belong to the specified question_id",
        )

    correct_choice = next(c for c in question.choices if c.is_correct)
    is_correct = (choice.id == correct_choice.id)

    create_user_answer(
        db=db,
        question_id=question.id,
        selected_choice_ids=[body.choice_id],
        is_correct=is_correct,
    )

    return AnswerResponse(
        is_correct=is_correct,
        correct_choice_id=correct_choice.id,
        correct_choice_text=correct_choice.choice_text,
        selected_choice_id=choice.id,
        selected_choice_text=choice.choice_text,
        explanation=question.explanation,
    )


# ── 旧 SQL Silver API（後方互換、未使用のまま維持） ────────────────

legacy_router = APIRouter(prefix="/api/answers", tags=["answers-legacy"])


@legacy_router.post("", response_model=LegacyAnswerResponse)
def submit_answer_legacy(body: LegacyAnswerRequest, db: Session = Depends(get_db)):
    """回答を送信して正誤を判定する（旧 API、複数選択対応）。"""
    question = get_question_by_id(db, body.question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")

    question_choice_ids = {c.id for c in question.choices}
    for cid in body.selected_choice_ids:
        if cid not in question_choice_ids:
            raise HTTPException(
                status_code=422,
                detail=f"choice_id {cid} does not belong to question {body.question_id}",
            )

    correct_choice_ids = [c.id for c in question.choices if c.is_correct]

    result = grade_answer(
        selected_ids=body.selected_choice_ids,
        correct_ids=correct_choice_ids,
        multi_select_count=question.multi_select_count,
        mode=config.INSUFFICIENT_SELECTION_MODE,
    )

    if result.should_warn:
        raise HTTPException(
            status_code=422,
            detail=f"Please select exactly {question.multi_select_count} choice(s)",
        )

    create_user_answer(
        db=db,
        question_id=question.id,
        selected_choice_ids=body.selected_choice_ids,
        is_correct=result.is_correct,
        user_name=body.user_name,
    )

    return LegacyAnswerResponse(
        is_correct=result.is_correct,
        correct_choice_ids=correct_choice_ids,
        explanation=question.explanation,
        trap_reason=question.trap_reason,
    )


@legacy_router.delete("")
def reset_answers(db: Session = Depends(get_db)):
    """全回答履歴をリセットする（テスト用）。"""
    deleted_count = delete_all_answers(db)
    return {"deleted_count": deleted_count}
