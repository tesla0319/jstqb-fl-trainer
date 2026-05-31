"""JSTQB Foundation Level 向けオリジナル問題データ（Phase 1 / 10問）。

全問単一選択・4択・正解1つ。公式問題のコピーは含まない。
category は config.JSTQB_CATEGORIES の name と一致させること。
DBテーブル変更なし。questions.category（文字列）で管理する既存方式を維持。
"""

SAMPLE_QUESTIONS: list[dict] = [
    # ── テストの基礎 × 2問 ────────────────────────────────────────
    {
        "category": "テストの基礎",
        "difficulty": 1,
        "question_text": "ソフトウェアテストの主な目的として最も適切なものはどれか。",
        "multi_select_count": 1,
        "explanation": (
            "JSTQBシラバスによると、テストの主な目的は欠陥を発見し、"
            "ソフトウェアの品質に関する情報をステークホルダーに提供することです。"
            "テストによってバグを完全になくすことはできません"
            "（テストの7原則：「テストは欠陥があることを示す」）。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "バグを完全に取り除くこと",                                            "is_correct": False, "display_order": 1},
            {"choice_text": "欠陥を発見し、ソフトウェアの品質に関する情報をステークホルダーに提供すること", "is_correct": True,  "display_order": 2},
            {"choice_text": "ソフトウェアを正常に動作させること",                                   "is_correct": False, "display_order": 3},
            {"choice_text": "開発コストを削減すること",                                            "is_correct": False, "display_order": 4},
        ],
    },
    {
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": "テストの7原則の一つである「欠陥の偏在」として最も適切な説明はどれか。",
        "multi_select_count": 1,
        "explanation": (
            "「欠陥の偏在」という原則は、少数のモジュールや機能に欠陥の大部分が集中することが多いことを示しています。"
            "これはパレートの法則（80:20の法則）とも関連しており、"
            "テストリソースを高リスク・高欠陥密度の領域に集中させることを推奨しています。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストの欠陥はシステム全体に均等に分布している",            "is_correct": False, "display_order": 1},
            {"choice_text": "少数のモジュールに欠陥の大部分が集中する傾向がある",         "is_correct": True,  "display_order": 2},
            {"choice_text": "欠陥は必ずユーザーインターフェースに存在する",              "is_correct": False, "display_order": 3},
            {"choice_text": "欠陥の数はソースコードの行数に比例する",                    "is_correct": False, "display_order": 4},
        ],
    },

    # ── テスト活動とプロセス × 2問 ────────────────────────────────
    {
        "category": "テスト活動とプロセス",
        "difficulty": 1,
        "question_text": "ソフトウェア開発において「早期テスト」を実施する最も重要な理由はどれか。",
        "multi_select_count": 1,
        "explanation": (
            "テストの7原則の一つ「早期テスト」によると、欠陥の修正コストは発見が遅れるほど増大します。"
            "要件定義や設計フェーズで発見した欠陥の修正コストは、"
            "リリース後の修正コストの何十分の一にもなります。"
            "そのため、できるだけ早い段階からテスト活動を開始することが重要です。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストチームの作業量を増やすため",                   "is_correct": False, "display_order": 1},
            {"choice_text": "欠陥を早い段階で発見し、修正コストを削減するため",    "is_correct": True,  "display_order": 2},
            {"choice_text": "開発者がテストを実施しなくて済むようにするため",      "is_correct": False, "display_order": 3},
            {"choice_text": "テスト自動化を容易にするため",                       "is_correct": False, "display_order": 4},
        ],
    },
    {
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": "テストプロセスにおけるテスト完了フェーズの活動として最も適切なものはどれか。",
        "multi_select_count": 1,
        "explanation": (
            "テスト完了フェーズでは、完了レポートの作成、テスト結果のまとめ、"
            "テストウェア（テストケース・スクリプト等）のアーカイブ、次のプロジェクトへの教訓の整理などを行います。"
            "テストケースの設計はテスト設計フェーズ、欠陥報告はテスト実施フェーズの活動です。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストケースを設計する",                               "is_correct": False, "display_order": 1},
            {"choice_text": "テスト結果を分析して欠陥を報告する",                   "is_correct": False, "display_order": 2},
            {"choice_text": "テスト環境のセットアップを行う",                       "is_correct": False, "display_order": 3},
            {"choice_text": "完了レポートを作成し、テストウェアをアーカイブする",    "is_correct": True,  "display_order": 4},
        ],
    },

    # ── 静的テスト × 1問 ─────────────────────────────────────────
    {
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": "静的テストと動的テストの違いについて最も適切な説明はどれか。",
        "multi_select_count": 1,
        "explanation": (
            "静的テストは、ソフトウェアを実際に実行することなく、"
            "コード・設計書・要件定義書などの成果物を検査するテスト手法です"
            "（例：コードレビュー、ウォークスルー、インスペクション）。"
            "一方、動的テストはソフトウェアを実際に実行してその動作を確認するテスト手法です"
            "（例：単体テスト、システムテスト）。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "静的テストは自動化ツールのみを使用し、動的テストは手動で行う",                       "is_correct": False, "display_order": 1},
            {"choice_text": "静的テストはソフトウェアを実行せずに検査し、動的テストはソフトウェアを実行して確認する", "is_correct": True,  "display_order": 2},
            {"choice_text": "静的テストは開発者が実施し、動的テストはテスターが実施する",                        "is_correct": False, "display_order": 3},
            {"choice_text": "静的テストは本番環境で行い、動的テストはテスト環境で行う",                          "is_correct": False, "display_order": 4},
        ],
    },

    # ── テスト技法 × 2問 ─────────────────────────────────────────
    {
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "同値分割法において、年齢入力欄が「1歳以上120歳以下」のみを有効とする場合、"
            "正しい同値クラスの分割はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "同値分割法では入力値を、同じ処理が行われるグループ（同値クラス）に分割します。"
            "「1〜120のみ有効」という仕様では、"
            "有効同値クラスは1〜120の範囲の値、"
            "無効同値クラスは0以下と121以上の2つになります。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "有効同値クラス：1〜120、無効同値クラス：0以下 と 121以上",     "is_correct": True,  "display_order": 1},
            {"choice_text": "有効同値クラス：1〜60 と 61〜120、無効同値クラス：0以下",      "is_correct": False, "display_order": 2},
            {"choice_text": "有効同値クラス：1〜120、無効同値クラス：0のみ",               "is_correct": False, "display_order": 3},
            {"choice_text": "有効同値クラス：1 と 120のみ、無効同値クラス：0 と 121",      "is_correct": False, "display_order": 4},
        ],
    },
    {
        "category": "テスト技法",
        "difficulty": 3,
        "question_text": "デシジョンテーブルテストを使用する最も適切な状況はどれか。",
        "multi_select_count": 1,
        "explanation": (
            "デシジョンテーブルテスト（判定表テスト）は、"
            "複数の条件の組み合わせに対してシステムがどのように動作するかを"
            "表形式で整理するテスト技法です。"
            "複数条件の組み合わせによって動作が変わるシステムに最も有効です。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "入力値が連続した数値範囲である場合",                              "is_correct": False, "display_order": 1},
            {"choice_text": "複数の条件の組み合わせによって異なる動作をするシステムをテストする場合", "is_correct": True,  "display_order": 2},
            {"choice_text": "システムのパフォーマンスを測定する場合",                           "is_correct": False, "display_order": 3},
            {"choice_text": "ソフトウェアのユーザビリティを評価する場合",                       "is_correct": False, "display_order": 4},
        ],
    },

    # ── テストマネジメント × 2問 ──────────────────────────────────
    {
        "category": "テストマネジメント",
        "difficulty": 1,
        "question_text": "テストマネジメントにおけるリスクベースドテストの主な目的はどれか。",
        "multi_select_count": 1,
        "explanation": (
            "リスクベースドテストは、製品リスク（欠陥の発生確率×影響度）を評価し、"
            "高リスクな機能・領域を優先してテストする手法です。"
            "限られたリソースで最も重要な部分を確実にテストするために用いられます。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストチーム自身のリスクを最小化すること",                               "is_correct": False, "display_order": 1},
            {"choice_text": "製品リスクに基づいてテストの優先順位を決め、限られたリソースを効率的に配分すること", "is_correct": True,  "display_order": 2},
            {"choice_text": "すべての機能を均等にテストすること",                                    "is_correct": False, "display_order": 3},
            {"choice_text": "テスト期間中のリスクをゼロにすること",                                   "is_correct": False, "display_order": 4},
        ],
    },
    {
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": "テストの進捗を監視・制御するために使用するメトリクスとして最も適切なものはどれか。",
        "multi_select_count": 1,
        "explanation": (
            "テストの進捗監視・制御には、テストケースの実行率、欠陥の発見率、欠陥の修正率"
            "などのメトリクスが使用されます。"
            "これらによりテスト活動の現状把握と計画との差異を特定できます。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "開発チームのメンバー数",                               "is_correct": False, "display_order": 1},
            {"choice_text": "テストケースの実行率、欠陥の発見率、欠陥の修正率",      "is_correct": True,  "display_order": 2},
            {"choice_text": "ソースコードの行数",                                   "is_correct": False, "display_order": 3},
            {"choice_text": "プロジェクトの予算残高",                               "is_correct": False, "display_order": 4},
        ],
    },

    # ── ツール支援 × 1問 ─────────────────────────────────────────
    {
        "category": "ツール支援",
        "difficulty": 1,
        "question_text": "テスト実行ツール（テスト自動化ツール）の主な利点として最も適切なものはどれか。",
        "multi_select_count": 1,
        "explanation": (
            "テスト実行ツールの主な利点は、回帰テストのような繰り返し実行するテストを効率化できることです。"
            "自動化により、一貫した手順でのテスト実行・人的ミスの削減・高速なフィードバックが実現できます。"
            "ただし、すべての欠陥を自動的に発見することはできません。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "すべての欠陥を自動的に発見できる",                              "is_correct": False, "display_order": 1},
            {"choice_text": "反復実行（回帰テスト等）の効率化と一貫性のあるテスト実行を実現できる", "is_correct": True,  "display_order": 2},
            {"choice_text": "テストケース設計の作業を不要にできる",                           "is_correct": False, "display_order": 3},
            {"choice_text": "テストの意思決定をツールに委任できる",                           "is_correct": False, "display_order": 4},
        ],
    },
]
