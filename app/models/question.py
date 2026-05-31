from datetime import datetime

from sqlalchemy import Integer, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # JSTQB FL ではカテゴリ名文字列で管理（正規化はPhase 2以降）
    category: Mapped[str] = mapped_column(Text, nullable=False, index=True)
    difficulty: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    question_text: Mapped[str] = mapped_column(Text, nullable=False)
    # Phase 1 では常に 1（JSTQB FL は単一選択のみ）。既存ロジックとの後方互換のため残す
    multi_select_count: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    explanation: Mapped[str] = mapped_column(Text, nullable=False)
    trap_reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )

    choices: Mapped[list["Choice"]] = relationship(
        "Choice", back_populates="question", order_by="Choice.display_order"
    )
    user_answers: Mapped[list["UserAnswer"]] = relationship(
        "UserAnswer", back_populates="question"
    )
