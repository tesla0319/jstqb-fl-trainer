DATABASE_URL = "sqlite:///./app.db"

# JSTQB FL カテゴリ定義（ID と名称のマスタ）
JSTQB_CATEGORIES = [
    {"id": 1, "name": "テストの基礎"},
    {"id": 2, "name": "テスト活動とプロセス"},
    {"id": 3, "name": "静的テスト"},
    {"id": 4, "name": "テスト技法"},
    {"id": 5, "name": "テストマネジメント"},
    {"id": 6, "name": "ツール支援"},
]

# 後方互換: stats 等が参照するカテゴリ名リスト
CATEGORIES = [c["name"] for c in JSTQB_CATEGORIES]

# 問題取得のデフォルト件数
DEFAULT_QUESTION_LIMIT = 10

# 苦手判定の正答率閾値（stats 機能で使用）
WEAK_THRESHOLD = 0.5
MIN_ANSWERS = 3

# 選択数不一致時の挙動（既存複数選択ロジック用、Phase 1 では実質不使用）
INSUFFICIENT_SELECTION_MODE = "reject"
