# JSTQB FL 学習支援アプリ

JSTQB Foundation Level 試験の学習を支援する Web アプリ。

- **出題・回答・解説**をシンプルなフローで繰り返し学習
- **カテゴリ指定 / ランダム**出題に対応
- **正誤判定と解説表示**で理解を定着
- **苦手克服・復習モード**で弱点を重点的に学習
- **ニックネーム別**に苦手分析を管理（複数ユーザー対応）

> 詳細仕様は `docs/spec_jstqb_fl_mvp.md` を参照してください。

---

## セットアップ

```bash
cd jstqb-fl-trainer

# 仮想環境の作成と有効化
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存ライブラリのインストール
pip install -r requirements.txt

# DB 作成 + 問題投入
python -m app.seed.init_db
```

---

## 起動

```bash
uvicorn app.main:app --reload
```

ブラウザで http://localhost:8000 にアクセス。

ヘルスチェック: http://localhost:8000/health

---

## テスト実行

```bash
pytest
```

現在 **78 テスト** が定義されています。

---

## 主な機能

| 機能 | 説明 |
|---|---|
| **ランダム出題** | 全カテゴリからランダムに1問出題 |
| **カテゴリ指定出題** | 指定カテゴリから問題を出題 |
| **正誤判定・解説表示** | 回答後に正解と解説を表示 |
| **苦手克服モード** | 正答率 50% 未満かつ 3問以上回答済みのカテゴリを優先出題 |
| **復習モード** | 直近の回答が不正解だった問題を優先出題 |
| **苦手分析** | カテゴリ別正答率・プログレスバーを表示 |
| **ニックネーム対応** | localStorage で保存。苦手分析・weak/review はユーザー別に管理 |

---

## API 一覧

### JSTQB FL API（`/api/v1`）

| メソッド | パス | 説明 |
|---|---|---|
| GET | `/api/v1/categories` | カテゴリ一覧取得 |
| GET | `/api/v1/questions` | 問題一覧取得（`category_id` / `random` / `limit` 対応） |
| GET | `/api/v1/questions/{id}` | 問題1件取得 |
| POST | `/api/v1/answers` | 回答送信・正誤判定 |

#### GET `/api/v1/questions` クエリパラメータ

| パラメータ | デフォルト | 説明 |
|---|---|---|
| `category_id` | なし | カテゴリ ID で絞り込み |
| `random` | `false` | `true` のとき `limit` を無視して1問ランダム返却 |
| `limit` | `10` | 取得件数上限（1以上）。`random=true` のときは無視 |

#### POST `/api/v1/answers` リクエスト Body

```json
{
  "question_id": 1,
  "choice_id": 3
}
```

#### GET `/api/v1/categories` レスポンス例

```json
{
  "categories": [
    { "id": 1, "name": "テストの基礎" },
    { "id": 2, "name": "テスト活動とプロセス" }
  ]
}
```

### 旧 API（後方互換で維持）

| メソッド | パス | 説明 |
|---|---|---|
| GET | `/health` | ヘルスチェック |
| GET | `/api/questions/random` | ランダム問題取得（`mode` / `exclude_ids` 対応） |
| POST | `/api/answers` | 回答送信（`selected_choice_ids` リスト形式） |
| GET | `/api/stats/categories` | カテゴリ別正答率取得 |
| DELETE | `/api/answers` | 回答履歴リセット（テスト用） |

---

## 問題データ管理

問題データは `app/seed/sample_questions.py` の Python リストで管理します。
現在 **10問 / 6カテゴリ**（Phase 1）。

### カテゴリ一覧

`テストの基礎` / `テスト活動とプロセス` / `静的テスト` /
`テスト技法` / `テストマネジメント` / `ツール支援`

カテゴリ定義は `app/config.py` の `JSTQB_CATEGORIES` で管理しています。
カテゴリ一覧 API はこの定義から返します（DB テーブルなし）。

### 問題を追加する

1. `app/seed/sample_questions.py` に辞書を追記する
2. 既存 DB を削除して再初期化する

```bash
# Mac/Linux
rm app.db
# Windows
del app.db

python -m app.seed.init_db
```

> **注意**: `init_db` は問題が 0 件のときのみ投入します。
> 問題を追加した場合は `app.db` を削除して再実行してください。

---

## ディレクトリ構成

```
jstqb-fl-trainer/
├── app/
│   ├── main.py               # FastAPI エントリポイント
│   ├── config.py             # 設定値（カテゴリ定数・閾値等）
│   ├── database.py           # DB 接続・セッション管理
│   ├── models/               # SQLAlchemy モデル
│   ├── schemas/              # Pydantic スキーマ
│   ├── crud/                 # DB 操作層
│   ├── routers/              # API エンドポイント
│   ├── services/             # ビジネスロジック（判定・苦手分析）
│   └── seed/                 # DB 初期化・問題データ
├── docs/
│   └── spec_jstqb_fl_mvp.md  # MVP 仕様書
├── static/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── images/
├── tests/
│   ├── conftest.py
│   ├── test_questions_api.py
│   ├── test_answers_api.py
│   ├── test_stats_api.py
│   ├── test_grading.py
│   ├── test_stats_service.py
│   ├── test_seed_coverage.py
│   └── test_config.py
├── requirements.txt
└── pytest.ini
```

---

## Render へのデプロイ

本アプリは [Render](https://render.com) で公開可能な構成です。

- **Runtime**: Python
- **Build Command**: `pip install -r requirements.txt && python -m app.seed.init_db`
- **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- **DB**: SQLite ファイル（`app.db`）はデプロイのたびに再生成されます
