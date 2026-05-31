"""カテゴリ一覧取得 API エンドポイント。

Phase 1 では categories テーブルを持たない。
カテゴリ一覧は config.JSTQB_CATEGORIES から返す（DB 不要）。
"""

from fastapi import APIRouter

from app.config import JSTQB_CATEGORIES

router = APIRouter(prefix="/api/v1/categories", tags=["categories"])


@router.get("")
def get_categories():
    """全カテゴリ一覧を返す。"""
    return {"categories": JSTQB_CATEGORIES}
