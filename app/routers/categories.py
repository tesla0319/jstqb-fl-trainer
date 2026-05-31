"""カテゴリ一覧取得 API エンドポイント。

Phase 1 では categories テーブルを持たない。
カテゴリ一覧は config.JSTQB_CATEGORIES から返す（DB 不要）。
count フィールドは DB から取得した登録問題数（後方互換の追加項目）。
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config import JSTQB_CATEGORIES
from app.crud.question import get_category_counts
from app.database import get_db

router = APIRouter(prefix="/api/v1/categories", tags=["categories"])


@router.get("")
def get_categories(db: Session = Depends(get_db)):
    """全カテゴリ一覧を返す。count は登録済み問題数。"""
    counts = get_category_counts(db)
    return {
        "categories": [
            {**cat, "count": counts.get(cat["name"], 0)}
            for cat in JSTQB_CATEGORIES
        ]
    }
