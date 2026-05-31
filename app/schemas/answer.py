"""回答送信リクエスト / レスポンスの Pydantic スキーマ。

JSTQB FL 版（/api/v1/answers）と旧 SQL Silver 版（/api/answers）の両方を定義する。
"""

from pydantic import BaseModel, Field, field_validator


# ── JSTQB FL 版（単一選択） ────────────────────────────────────────

class AnswerRequest(BaseModel):
    question_id: int
    choice_id: int


class AnswerResponse(BaseModel):
    is_correct: bool
    correct_choice_id: int
    correct_choice_text: str
    selected_choice_id: int
    selected_choice_text: str
    explanation: str


# ── 旧 SQL Silver 版（複数選択対応、後方互換） ─────────────────────

class LegacyAnswerRequest(BaseModel):
    question_id: int
    selected_choice_ids: list[int] = Field(min_length=1)
    user_name: str = Field(default="guest", min_length=1, max_length=50)

    @field_validator("selected_choice_ids")
    @classmethod
    def no_duplicates(cls, v: list[int]) -> list[int]:
        if len(v) != len(set(v)):
            raise ValueError("selected_choice_ids must not contain duplicates")
        return v

    @field_validator("user_name")
    @classmethod
    def strip_and_reject_blank(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("user_name must not be empty or whitespace only")
        return v


class LegacyAnswerResponse(BaseModel):
    is_correct: bool
    correct_choice_ids: list[int]
    explanation: str
    trap_reason: str | None
