"""問題取得レスポンスの Pydantic スキーマ。

is_correct は出題時点でクライアントに渡さない（カンニング防止）。
正解情報は /api/v1/answers レスポンスにのみ含める。
"""

from pydantic import BaseModel, Field


class ChoiceResponse(BaseModel):
    """選択肢レスポンス（is_correct は除外）。新旧 API 共通。"""
    id: int
    choice_text: str
    display_order: int

    model_config = {"from_attributes": True}


class QuestionResponse(BaseModel):
    """JSTQB FL API (/api/v1/questions) 用レスポンス。"""
    id: int
    # question.category（文字列）を category_name として出力する
    category_name: str = Field(validation_alias="category")
    difficulty: int
    question_text: str
    choices: list[ChoiceResponse]

    model_config = {"from_attributes": True, "populate_by_name": True}


class QuestionsListResponse(BaseModel):
    questions: list[QuestionResponse]


class LegacyQuestionResponse(BaseModel):
    """旧 SQL Silver API (/api/questions/random) 用レスポンス（後方互換）。"""
    id: int
    category: str
    difficulty: int
    question_text: str
    multi_select_count: int
    choices: list[ChoiceResponse]

    model_config = {"from_attributes": True}
