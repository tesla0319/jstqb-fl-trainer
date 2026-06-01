"""JSTQB Foundation Level 向けオリジナル問題データ（152問）。

全問単一選択・4択・正解1つ。公式問題のコピーは含まない。
category は config.JSTQB_CATEGORIES の name と一致させること。
DBテーブル変更なし。questions.category（文字列）で管理する既存方式を維持。

カテゴリ配分:
  テストの基礎         25問
  テスト活動とプロセス  24問
  静的テスト           31問
  テスト技法           34問
  テストマネジメント   23問
  ツール支援           15問
"""

SAMPLE_QUESTIONS: list[dict] = [

    # ══════════════════════════════════════════════════════════════
    # テストの基礎  10問
    # ══════════════════════════════════════════════════════════════

    {   # Q01
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
    {   # Q02
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
    {   # Q03
        "category": "テストの基礎",
        "difficulty": 1,
        "question_text": "テストの7原則の一つである「全数テストは不可能」として最も適切な説明はどれか。",
        "multi_select_count": 1,
        "explanation": (
            "「全数テストは不可能」とは、すべての入力値・前提条件の組み合わせを網羅してテストすることは、"
            "リソースと時間の制約からほぼ不可能であることを意味します。"
            "そのため、リスクと優先度に基づいてテストを選択・集中することが重要です。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストの担当者が全員揃わない場合はテストができない",                    "is_correct": False, "display_order": 1},
            {"choice_text": "すべての入力値・前提条件の組み合わせを網羅することはリソース上ほぼ不可能である", "is_correct": True,  "display_order": 2},
            {"choice_text": "テストはコンピュータにしか実行できない",                              "is_correct": False, "display_order": 3},
            {"choice_text": "テストは必ず自動化しなければならない",                               "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q04
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": "テストの7原則の一つである「テストの弱化」の意味として最も適切なものはどれか。",
        "multi_select_count": 1,
        "explanation": (
            "テストの弱化は、同一の農薬を繰り返し使うと害虫が耐性を持つように、"
            "同じテストを繰り返すと新たな欠陥を発見できなくなることを示しています。"
            "これを防ぐには、定期的にテストケースを見直し・更新し、新たなテストを追加することが重要です。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストが農業分野でも応用できることを示す原則",                       "is_correct": False, "display_order": 1},
            {"choice_text": "同じテストを繰り返し実行すると、そのテストでは新たな欠陥を発見しにくくなる", "is_correct": True,  "display_order": 2},
            {"choice_text": "テストは農薬のように有害な副作用をもたらす場合がある",                "is_correct": False, "display_order": 3},
            {"choice_text": "テストを増やすほどソフトウェアの品質が下がる現象",                   "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q05
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": "テストの7原則の一つである「バグゼロの落とし穴」として最も適切な説明はどれか。",
        "multi_select_count": 1,
        "explanation": (
            "「バグゼロの落とし穴」とは、テストで全バグを取り除いても、"
            "そのソフトウェアがユーザーのニーズや期待・ビジネス要件を満たしていなければ役立たないことを示します。"
            "バグがゼロでも、仕様が誤っていたり使いにくかったりすれば、ソフトウェアとして価値がありません。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "バグを0件にすることは技術的に不可能である",                                "is_correct": False, "display_order": 1},
            {"choice_text": "バグが0件でも、ユーザーの要求や期待に応えていなければソフトウェアは使えない", "is_correct": True,  "display_order": 2},
            {"choice_text": "バグゼロのソフトウェアは存在しない",                                     "is_correct": False, "display_order": 3},
            {"choice_text": "バグを修正すると新たなバグが生まれる可能性がある",                        "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q06
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "ソフトウェアテストの文脈において、「エラー（error）」「欠陥（defect）」「故障（failure）」の"
            "関係として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQBの用語では、人間のミス（error）がソフトウェアの欠陥（defect/bug）を引き起こし、"
            "その欠陥が実行時に故障（failure）として現れます。"
            "例えば、開発者の設計ミス（error）→コード内の欠陥（defect）→実行時に誤った出力（failure）という流れになります。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "エラーはシステムの誤動作、欠陥はユーザーの操作ミス、故障はハードウェアの破損",     "is_correct": False, "display_order": 1},
            {"choice_text": "エラー（ミス）が原因で欠陥がコードに混入し、その欠陥が実行時に故障として現れる", "is_correct": True,  "display_order": 2},
            {"choice_text": "故障が発生すると欠陥が生まれ、欠陥が積み重なるとエラーになる",                  "is_correct": False, "display_order": 3},
            {"choice_text": "エラー・欠陥・故障はすべて同じ意味で使われる",                               "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q07
        "category": "テストの基礎",
        "difficulty": 1,
        "question_text": "テスト（testing）とデバッグ（debugging）の違いとして最も適切なものはどれか。",
        "multi_select_count": 1,
        "explanation": (
            "テストは、ソフトウェアを実行（または成果物をレビュー）して欠陥を発見する活動です。"
            "一方、デバッグは発見された欠陥の根本原因を特定し修正する開発活動です。"
            "テストと確認テストはテスト担当者が行い、デバッグ（修正）は一般に開発者が担当します。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストはオープンソースで、デバッグはクローズドソースにのみ適用する",           "is_correct": False, "display_order": 1},
            {"choice_text": "テストは欠陥を発見する活動であり、デバッグは欠陥の原因を特定して修正する活動である", "is_correct": True,  "display_order": 2},
            {"choice_text": "テストは自動化でのみ実施でき、デバッグは手動でのみ実施できる",                "is_correct": False, "display_order": 3},
            {"choice_text": "テストは開発者が担当し、デバッグはテスターが担当する",                       "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q08
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": "ソフトウェアテストと品質保証（QA）の関係として最も適切なものはどれか。",
        "multi_select_count": 1,
        "explanation": (
            "テスト（testing）は、特定のソフトウェアで欠陥を発見し品質情報を提供する製品評価活動です。"
            "品質保証（QA）は、開発・テストプロセス全体が適切に実施されているかを監視・改善する活動で、プロセス指向のアプローチです。"
            "テストはQAを支援する手段の一つですが、QAはより広い概念です。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストと品質保証は同じ活動であり、同じチームが担当する",                       "is_correct": False, "display_order": 1},
            {"choice_text": "テストは製品の欠陥を発見する活動であり、品質保証はプロセス全体の品質を改善する活動である", "is_correct": True,  "display_order": 2},
            {"choice_text": "品質保証はテストの一部であり、テストを実施すれば自動的に品質が保証される",        "is_correct": False, "display_order": 3},
            {"choice_text": "テストは品質保証の代替活動であり、どちらか一方だけ実施すればよい",               "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q09
        "category": "テストの基礎",
        "difficulty": 1,
        "question_text": "テストの7原則の一つである「テストは欠陥があることを示す」として最も適切な説明はどれか。",
        "multi_select_count": 1,
        "explanation": (
            "「テストは欠陥があることを示す」という原則は、テストによって欠陥が存在することを示せても、"
            "欠陥が存在しないことを証明することはできないことを意味します。"
            "テストを多く実施して欠陥が見つからなくても、それは「欠陥がない」ことの証明にはなりません。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストを実施すれば、必ず欠陥が発見される",                               "is_correct": False, "display_order": 1},
            {"choice_text": "テストによって欠陥がないことを証明できるが、コストがかかる",               "is_correct": False, "display_order": 2},
            {"choice_text": "テストは欠陥の存在を示すことができるが、欠陥がないことは証明できない",       "is_correct": True,  "display_order": 3},
            {"choice_text": "テストはすべての欠陥を必ず発見する",                                    "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q10
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": "ソフトウェアに欠陥が生じる根本的な原因として最も適切なものはどれか。",
        "multi_select_count": 1,
        "explanation": (
            "ソフトウェアの欠陥は主に人間のミス（error）から生じます。"
            "時間的プレッシャー・複雑な要件・設計・コード・コミュニケーション不足・新技術の習得不足など"
            "様々な要因が重なり、開発者や設計者が誤りを犯すことで欠陥が混入します。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストの予算不足と人員不足のみが原因である",                                   "is_correct": False, "display_order": 1},
            {"choice_text": "人間は誤りを犯しやすく、時間的プレッシャーや複雑な要件・コードが欠陥の主な原因となる", "is_correct": True,  "display_order": 2},
            {"choice_text": "プログラミング言語の性質上、すべてのプログラムには必ず欠陥が含まれる",            "is_correct": False, "display_order": 3},
            {"choice_text": "テスト自動化の不十分さが欠陥の主な原因である",                                 "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # テスト活動とプロセス・その他  MD由来 30問
    # ══════════════════════════════════════════════════════════════

    {   # Q11
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるECサイトでは、新しい「クーポン適用機能」の開発が完了し、"
            "テスト担当者がテスト活動を開始しようとしている。\n\n"
            "テスト担当者は要求仕様書を確認し、以下の内容を整理した。\n"
            "- 会員ランクによって割引率が異なること\n"
            "- クーポンには有効期限があること\n"
            "- 一部の商品カテゴリはクーポン対象外であること\n"
            "- 1回の注文につき使用できるクーポンは1枚であること\n\n"
            "この後、テスト担当者は整理した内容をもとに、"
            "テスト条件をカバーするテストケースの設計に取り掛かろうとしている。\n\n"
            "この「この後に取り掛かろうとしている」活動として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "問題文に記載されている「要求仕様書を確認し、テスト観点を整理した」活動がテスト分析にあたる。"
            "「この後に取り掛かろうとしている」のは、整理したテスト条件をカバーする"
            "テストケースを設計する活動であり、これはテスト設計に相当する。"
            "テスト設計ではハイレベルなテストケースを作成しテスト技法を適用する。"
            "テスト実装はテストケースを具体化しテスト手順・テストデータを準備する段階、"
            "テスト実行はテストケースを実際に動かして結果を確認する段階を指す。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト分析",   "is_correct": False, "display_order": 1},
            {"choice_text": "テスト設計",   "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト実装",   "is_correct": False, "display_order": 3},
            {"choice_text": "テスト実行",   "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q12
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスでは、宿泊予約機能のテストを計画している。\n\n"
            "テスト担当者は既に以下の条件を識別している。\n"
            "- 宿泊人数\n"
            "- 宿泊日数\n"
            "- 部屋タイプ\n"
            "- 支払方法\n\n"
            "次の作業として、識別したテスト条件をもとにテストケースを設計しようとしている。\n\n"
            "最も適切な活動はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストプロセスにおいて、テスト条件を識別する活動はテスト分析に相当する。"
            "識別したテスト条件をカバーするテストケースを設計する活動はテスト設計である。"
            "テスト設計ではハイレベルなテストケースを作成しテスト技法を適用する。"
            "A（テスト条件を識別する）はすでに完了した活動、"
            "C（テスト環境・テストデータの準備）はテスト実装、"
            "D（テスト結果の評価）はテスト実行後の活動にあたる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト条件を識別する活動",              "is_correct": False, "display_order": 1},
            {"choice_text": "テスト条件をカバーするテストケースを設計する活動", "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト環境やテストデータを準備する活動",  "is_correct": False, "display_order": 3},
            {"choice_text": "テスト結果を評価する活動",               "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q13
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "ある航空券予約システムの要求仕様レビューで以下の指摘が挙がった。\n\n"
            "- キャンセル料の計算方法が未記載\n"
            "- 「迅速に処理する」という曖昧な表現が存在する\n"
            "- 同一内容が異なる表現で複数箇所に記載されている\n\n"
            "プロジェクトマネージャは「実装前に見つかって良かった」と評価した。\n\n"
            "その理由として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストの7原則のひとつ「早期テスト」によれば、欠陥の修正コストは発見フェーズが遅いほど増大する。"
            "実装前の要求仕様レビューで発見した欠陥（記載不足・曖昧な表現・重複記述など）は、"
            "実装後・テスト後・リリース後に発見するよりはるかに低コストで修正できる。"
            "レビューは性能測定（A）でも全欠陥の除去（C）でもなく、テスト実行を不要にする（D）ものでもない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "レビューにより実行性能を測定できたため",          "is_correct": False, "display_order": 1},
            {"choice_text": "レビューにより欠陥を早期に発見できたため",         "is_correct": True,  "display_order": 2},
            {"choice_text": "レビューにより全欠陥を除去できたため",             "is_correct": False, "display_order": 3},
            {"choice_text": "レビューによりテスト実行が不要になったため",        "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q14
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスでは、利用者の年齢に応じて以下のように"
            "成人向けオプションの表示を制御している。\n\n"
            "- 18歳未満：非表示\n"
            "- 18歳以上：表示\n\n"
            "同値分割法を適用してテストケースを設計する場合、"
            "各同値クラスから代表値を1つずつ選ぶ組み合わせとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "同値分割法では、同じ処理結果になる値のグループ（同値クラス）を識別し、各クラスから代表値を1つ選ぶ。"
            "この仕様では「18歳未満（非表示クラス）」と「18歳以上（表示クラス）」の2つの同値クラスが存在する。"
            "各クラスから代表値を1つずつ選ぶ場合、10歳（非表示クラス代表）と25歳（表示クラス代表）の組み合わせが正しい（C）。"
            "A（17歳・18歳）は17歳が非表示クラス代表として正しいが18歳は境界値のため同値クラスの代表として不適切。"
            "B（0歳・18歳・99歳）も18歳が境界値のため不適切で、同値クラスは2つのため3値は過剰。"
            "D（18歳のみ）は1クラスしかカバーできていない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "17歳、18歳",      "is_correct": False, "display_order": 1},
            {"choice_text": "0歳、18歳、99歳", "is_correct": False, "display_order": 2},
            {"choice_text": "10歳、25歳",      "is_correct": True,  "display_order": 3},
            {"choice_text": "18歳のみ",        "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q15
        "category": "テスト技法",
        "difficulty": 3,
        "question_text": (
            "あるネット銀行では振込機能について以下の制約を設けている。\n\n"
            "- 1回の振込金額は1円以上100万円以下\n"
            "- 100万円を超える振込はエラー\n"
            "- 0円以下は入力不可\n\n"
            "テスト担当者は限られた工数で境界値分析を適用したい。\n\n"
            "最も優先して選択すべき組み合わせはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "境界値分析では、有効範囲の下限・上限とその直外の値をテストする。"
            "JSTQBシラバスでは3値境界値分析として「境界の前後と境界値そのもの」をテストすることが推奨される。"
            "1円以上100万円以下の仕様に対して3値分析を適用すると、"
            "下限側は0円（境界外）・1円（下限境界）・2円（境界内+1）、"
            "上限側は99万9999円（境界内-1）・100万円（上限境界）・100万1円（境界外）の6値が最適である。"
            "A（3値のみ）とD（2値のみ）は網羅性が不十分、C（中間値のみ）は境界値を含まない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "1円、50万円、100万円",                              "is_correct": False, "display_order": 1},
            {"choice_text": "0円、1円、2円、99万9999円、100万円、100万1円",       "is_correct": True,  "display_order": 2},
            {"choice_text": "10万円、50万円、90万円",                            "is_correct": False, "display_order": 3},
            {"choice_text": "1円、100万円のみ",                                  "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q16
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "ある会員サービスでは以下の状態が存在する。\n\n"
            "- 無料会員 → 有料会員\n"
            "- 有料会員 → 解約申請中\n"
            "- 解約申請中 → 解約済み\n"
            "- 解約申請中 → 有料会員（取り消し）\n\n"
            "テスト担当者は以下のシーケンスを実行した。\n\n"
            "無料会員 → 有料会員 → 解約申請中 → 有料会員\n\n"
            "このテストによって確認されたものとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "状態遷移テストのカバレッジ基準には、全状態カバレッジ・全遷移カバレッジ・全遷移シーケンスカバレッジなどがある。"
            "このテストでは「解約済み」状態が未カバーのため全状態カバレッジ（A）は未達成。"
            "「解約申請中→解約済み」遷移が未実行のため全遷移カバレッジ（B）も未達成。"
            "すべての遷移パターン（D）とも異なる。"
            "実施したシーケンスは定義された遷移を一部たどった「一連の状態遷移シーケンスの確認」に相当する（C）。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "全状態カバレッジ",         "is_correct": False, "display_order": 1},
            {"choice_text": "全遷移カバレッジ",         "is_correct": False, "display_order": 2},
            {"choice_text": "一連の状態遷移シーケンス", "is_correct": True,  "display_order": 3},
            {"choice_text": "すべての状態遷移パターン", "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q17
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サイトで、予約確認メールが送信されない不具合が修正された。\n\n"
            "テストチームは以下を実施した。\n\n"
            "- テストA：予約確認メール送信確認\n"
            "- テストB：予約変更機能確認\n"
            "- テストC：予約キャンセル機能確認\n\n"
            "最も適切な説明はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "確認テスト（confirmation testing）は、報告された欠陥が修正されたことを確認するテストである。"
            "修正した機能（予約確認メール送信）を再テストするテストAがこれに相当する。"
            "回帰テスト（regression testing）は、変更によって既存機能が意図せず影響を受けていないことを確認するテストであり、"
            "関連機能である予約変更（B）・予約キャンセル（C）の確認がこれにあたる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "Aは確認テスト、BとCは回帰テスト", "is_correct": True,  "display_order": 1},
            {"choice_text": "Aは回帰テスト、BとCは確認テスト", "is_correct": False, "display_order": 2},
            {"choice_text": "すべて確認テスト",                 "is_correct": False, "display_order": 3},
            {"choice_text": "すべて回帰テスト",                 "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q18
        "category": "テストマネジメント",
        "difficulty": 3,
        "question_text": (
            "あるネット銀行では次回リリースで以下の機能を変更した。\n\n"
            "- 振込：変更規模=中、過去欠陥数=3、障害時影響=高\n"
            "- 残高照会：変更規模=大、過去欠陥数=6、障害時影響=中\n"
            "- 住所変更：変更規模=中、過去欠陥数=4、障害時影響=中\n"
            "- お知らせ：変更規模=小、過去欠陥数=1、障害時影響=低\n\n"
            "回帰テストに利用できる時間は限られている。\n\n"
            "リスクベースドテストの考え方に基づき、最優先で重点的に確認すべき対象はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "リスクベースドテストでは「リスクレベル＝発生可能性×影響度」を総合的に評価してテストの優先度を決める。"
            "残高照会は変更規模が大きく過去欠陥数も最多であることから発生可能性が高く、最優先となる。"
            "振込は障害時影響が高いが、変更規模・過去欠陥数の両面で残高照会を下回るため2番手となる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "振込",     "is_correct": False, "display_order": 1},
            {"choice_text": "残高照会", "is_correct": True,  "display_order": 2},
            {"choice_text": "住所変更", "is_correct": False, "display_order": 3},
            {"choice_text": "お知らせ", "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q19
        "category": "テストマネジメント",
        "difficulty": 3,
        "question_text": (
            "ある動画配信サービスではシステムテスト終了判断を行っている。\n\n"
            "終了基準は以下の通りである。\n"
            "- 要件カバレッジ95%以上\n"
            "- 重大度高欠陥0件\n"
            "- 未実施テスト5%未満\n\n"
            "現在の状況は以下である。\n"
            "- 要件カバレッジ：97%\n"
            "- 重大度高欠陥：1件\n"
            "- 未実施率：2%\n\n"
            "残っている欠陥は「特定条件で月額課金が二重計上される可能性がある」という内容である。\n\n"
            "最も適切な判断はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "終了基準は絶対的なGOサインではなく、残存リスクを関係者で合意して判断するものである。"
            "ただし重大度高欠陥は必ず修正方針を決めてから進めるべきであり、"
            "「月額課金の二重計上」という深刻な内容を踏まえると、"
            "修正・回避策・リリース延期のいずれかについてステークホルダーと合意することが求められる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "カバレッジと未実施率は基準達成のため終了する",          "is_correct": False, "display_order": 1},
            {"choice_text": "重大度高欠陥があるため他の状況に関係なく延期する",       "is_correct": False, "display_order": 2},
            {"choice_text": "終了基準未達項目と残存リスクを評価して判断する",         "is_correct": True,  "display_order": 3},
            {"choice_text": "未実施率が低いため欠陥はリリース後対応とする",           "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q20
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるECサイトのシステムテストでは、計画上200件のテストケースを実施する予定である。\n\n"
            "現在の状況は以下の通り。\n"
            "- 実施済み：160件\n"
            "- 合格：145件\n"
            "- 不合格：15件\n\n"
            "テストマネージャが「計画に対してどれだけテストが進んでいるか」を把握したい。\n\n"
            "最も適切な指標はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "「計画に対してどれだけテストが進んでいるか」はテスト進捗のメトリクスで把握する。"
            "テスト実行率（実施済みテスト数÷計画総数）は進捗そのものを示す指標であり、"
            "この例では160÷200＝80%となる。"
            "テスト合格率（B）は品質の指標、"
            "未解決欠陥数（C）と欠陥検出数（D）は欠陥に関するメトリクスであり、"
            "進捗把握が目的の場合はテスト実行率が最適である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト実行率",   "is_correct": True,  "display_order": 1},
            {"choice_text": "テスト合格率",   "is_correct": False, "display_order": 2},
            {"choice_text": "未解決欠陥数",   "is_correct": False, "display_order": 3},
            {"choice_text": "欠陥検出数",     "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q21
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスでは、新しい「予約内容確認機能」の開発を進めている。\n\n"
            "プロダクトオーナーは次のユーザーストーリーを作成した。\n\n"
            "「宿泊者として、出発前に予約内容を確認したい。なぜなら、予約内容の誤りを事前に発見したいからだ。」\n\n"
            "スプリント計画会議で、チームから次のような質問が挙がった。\n"
            "- 予約内容は何日前から確認できるのか\n"
            "- キャンセル済み予約も表示するのか\n"
            "- 複数の予約が存在する場合はどう表示するのか\n\n"
            "プロダクトオーナーは「その点は一緒に整理していきたい」と回答した。\n\n"
            "この状況について、ユーザーストーリーの考え方に最も合致する説明はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ユーザーストーリーは詳細な要件仕様書ではなく、関係者が対話するためのきっかけとなるものである。"
            "価値の概要をもとにプロダクトオーナー・開発者・テスト担当者が継続的に対話を重ねることで詳細が明確化される。"
            "すべての要件をストーリーに記載する必要はなく（Aは誤り）、"
            "プロダクトオーナーが対話に積極参加することが推奨される（Cは誤り）。"
            "実装後に内容を決めるのはアジャイルの考え方と逆行する（Dは誤り）。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ユーザーストーリーには必要な要件がすべて記載されているべきであり、このような質問が出ること自体が問題である", "is_correct": False, "display_order": 1},
            {"choice_text": "ユーザーストーリーは会話のきっかけであり、詳細は関係者の対話を通じて明確化される",                       "is_correct": True,  "display_order": 2},
            {"choice_text": "ユーザーストーリーは開発担当者向けの作業指示であり、プロダクトオーナーが議論に参加する必要はない",         "is_correct": False, "display_order": 3},
            {"choice_text": "ユーザーストーリーの内容は実装完了後に決定するのが望ましい",                                             "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q22
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるオンライン書店では、購入履歴確認機能の開発を進めている。\n\n"
            "プロダクトオーナーは次のユーザーストーリーを提示した。\n\n"
            "「利用者として、購入履歴を確認したい。なぜなら、過去に購入した商品を再度購入したいからだ。」\n\n"
            "その後の議論で、チームは次の内容を整理した。\n"
            "- 過去1年間の購入履歴を表示する\n"
            "- 商品名、購入日、購入金額を表示する\n"
            "- キャンセル済み注文は表示しない\n\n"
            "テスト担当者は、これらの内容をテスト設計や受入判断に利用する予定である。\n\n"
            "この情報の主な役割として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ユーザーストーリーの「確認（Confirmation）」にあたるのが受入基準（acceptance criteria）である。"
            "チームが対話を通じて整理した「過去1年間の履歴表示」「表示項目の定義」「キャンセル済み注文の除外」といった内容は、"
            "ストーリーが正しく実現されたかをテスト設計・受入判断で確認するための基準として機能する。"
            "詳細設計書の代替（A）ではなく、完了後に作成する運用手順（C）でも個人メモ（D）でもない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ユーザーストーリーの代わりに利用する詳細設計書",              "is_correct": False, "display_order": 1},
            {"choice_text": "ストーリーが期待通りに実現されたかを判断するための基準",       "is_correct": True,  "display_order": 2},
            {"choice_text": "開発完了後に作成する運用手順",                               "is_correct": False, "display_order": 3},
            {"choice_text": "プロダクトオーナーの個人的なメモ",                           "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q23
        "category": "テスト活動とプロセス",
        "difficulty": 3,
        "question_text": (
            "あるWebサービス開発チームでは、DevOpsの考え方を取り入れて以下の体制をすでに構築している。\n\n"
            "- 開発チームと運用チームが合同でインシデント対応を行っている\n"
            "- ビルド・テスト・本番デプロイまでを自動化している\n"
            "- 週次でリリースを継続している\n\n"
            "しかしチームは「障害発生後の対応が属人化しており、同種の障害が繰り返されている」という課題を認識した。\n\n"
            "DevOpsの考え方に基づき、このチームが次に優先すべき活動として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "DevOpsでは「継続的な改善」が重要な考え方であり、"
            "障害の原因を組織的に分析し、プロセスに反映することを重視する。"
            "ポストモーテム（事後検証）は「責任追及」ではなく「仕組みの改善」を目的として実施するものであり、"
            "同種障害の繰り返しを防ぐ有効な手段である。"
            "デプロイを手動に戻すことはDevOpsの自動化原則に反し、"
            "チームを分離することはDevOpsの協力の考え方と逆行し、"
            "リリース頻度を下げ変更範囲を広げることはリスクを増大させDevOpsの方向性と逆行する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "本番デプロイを手動に戻し、リリース前レビューを強化する",                  "is_correct": False, "display_order": 1},
            {"choice_text": "障害発生時のポストモーテムを実施し、再発防止策をプロセスに組み込む",       "is_correct": True,  "display_order": 2},
            {"choice_text": "運用チームを開発チームから分離し、それぞれの専門性を高める",              "is_correct": False, "display_order": 3},
            {"choice_text": "リリース頻度を月次に下げ、一度に変更する範囲を広げる",                   "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q24
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "ある動画配信サービスでは、毎週リリースを行っている。\n\n"
            "現在の状況は以下の通りである。\n"
            "- ビルド：自動\n"
            "- 単体テスト：自動\n"
            "- APIテスト：自動\n"
            "- 本番デプロイ：手動\n"
            "- 障害分析：開発チームのみ\n\n"
            "チームは、リリース頻度を維持しながら品質向上も実現したいと考えている。\n\n"
            "DevOpsの考え方に最も合致する改善策はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "DevOpsでは開発と運用の協力体制と自動化が重要な考え方である。"
            "本番デプロイを自動化することでリリース頻度を維持しながら人的ミスを削減でき、"
            "開発担当者と運用担当者が協力して継続的な改善活動を行うことで品質が向上する（A）。"
            "リリース前レビューの強化（B）は手動ゲートを追加し自動化の利点を損なう。"
            "チームの分離（C）はDevOpsの協力原則に反する。"
            "本番デプロイを手動のままにすることも自動化の後退につながる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "本番環境への反映を自動化し、開発担当者と運用担当者が協力して継続的な改善活動を行う",                        "is_correct": True,  "display_order": 1},
            {"choice_text": "本番環境への反映を自動化し、品質リスク低減のためリリース前レビューを強化する",                              "is_correct": False, "display_order": 2},
            {"choice_text": "運用担当者を障害分析へ参加させる一方で、本番環境への反映は承認後に手動で実施する",                          "is_correct": False, "display_order": 3},
            {"choice_text": "リリース頻度を維持するため本番環境への反映を自動化するが、障害分析は障害発生時のみ実施する",                  "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q25
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるWebサービス開発チームでは、回帰テストの実行時間増加が課題となっている。\n\n"
            "テスト担当者は、自動テストの構成を見直したいと考えている。\n\n"
            "テストピラミッドの考え方として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストピラミッドは自動テスト戦略の考え方で、"
            "下層（単体テスト）を最も多く実施し、中層（統合/APIテスト）、上層（UIテスト/E2Eテスト）と"
            "上に行くほど件数を減らす構造を推奨する。"
            "単体テストは実行速度が速くコストが低い一方、UI/E2Eテストは実行が遅くメンテナンスコストが高いため、"
            "上層ほど件数を絞ることで全体の実行時間と維持コストを適正化できる。"
            "UIテストを最多にする（A）やE2Eのみ（D）、均等実施（C）はいずれもこの考え方と逆行する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "UIテストを最も多く実施する",                   "is_correct": False, "display_order": 1},
            {"choice_text": "単体テストを最も多く実施し、上位層ほど少なくする", "is_correct": True,  "display_order": 2},
            {"choice_text": "すべてのテストレベルを同数実施する",             "is_correct": False, "display_order": 3},
            {"choice_text": "E2Eテストのみを実施する",                      "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q26
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスでは、新しい注文画面をリリースする予定である。\n\n"
            "テストチームは以下の活動を計画している。\n"
            "- 開発者による単体テスト\n"
            "- APIレベルの結合テスト\n"
            "- 利用者による試用評価\n"
            "- ユーザビリティ専門家による操作性評価\n\n"
            "プロダクトオーナーは「利用者が価値を感じるかを確認したい」と考えている。\n\n"
            "この目的に最も直接貢献する活動の組み合わせはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "「利用者が価値を感じるか」を確認するには、"
            "実際の利用者がシステムを操作して評価するユーザー受入テスト（UAT）と、"
            "ユーザビリティ専門家が操作性を評価するユーザビリティテストが直接貢献する（C）。"
            "単体テストとAPIテスト（A・D）はコードレベルの正確性を確認するが、利用者が価値を感じるかという判断には直結しない。"
            "APIテストとUAT（B）はAPIテストが利用者視点でないため目的に対して不完全な組み合わせとなる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "単体テストとAPIレベルの結合テスト",             "is_correct": False, "display_order": 1},
            {"choice_text": "APIレベルの結合テストと利用者による試用評価",    "is_correct": False, "display_order": 2},
            {"choice_text": "利用者による試用評価とユーザビリティ評価",        "is_correct": True,  "display_order": 3},
            {"choice_text": "単体テストとユーザビリティ評価",                 "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q27
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行では、振込機能の改修を行った。\n\n"
            "テスト担当者は以下の情報を管理している。\n"
            "- 要件ID\n"
            "- テスト条件\n"
            "- テストケース\n"
            "- テスト実行結果\n\n"
            "リリース前に「すべての要件が適切にテストされているか」を確認したいと考えている。\n\n"
            "この目的に最も有効なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "要件トレーサビリティは、要件IDとテスト条件・テストケース・テスト実行結果を対応付けることで"
            "「すべての要件が適切にテストされているか（要件カバレッジ）」を追跡・確認できるようにするものである。"
            "欠陥レポート（A）は欠陥情報の管理、テストサマリーレポート（B）はテスト活動全体の概要、"
            "テストログ（D）は実行時の詳細記録であり、要件との対応関係を確認する目的にはトレーサビリティが最も適している。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "欠陥レポート",               "is_correct": False, "display_order": 1},
            {"choice_text": "テストサマリーレポート",       "is_correct": False, "display_order": 2},
            {"choice_text": "要件トレーサビリティ",         "is_correct": True,  "display_order": 3},
            {"choice_text": "テストログ",                  "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q28
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるECサイトでは、商品検索機能の不具合が報告された。\n\n"
            "テスト担当者は欠陥レポートを作成している。\n\n"
            "開発担当者から「同じ事象を再現できない」という連絡があった。\n\n"
            "この状況を改善するために、欠陥レポートへ優先的に記載すべき情報として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "欠陥を再現できない原因の多くは「再現手順の不明確さ」と「環境情報の不足」である。"
            "欠陥レポートには、再現に必要な操作手順（前提条件・操作ステップ・使用データ）と"
            "実行環境（OS・ブラウザ・バージョン等）を明記することで、"
            "開発担当者が同じ状況で事象を再現できるようになる。"
            "期待結果と実際結果（B）・重大度と優先度（C）・影響範囲（D）も必要な情報だが、"
            "「再現できない」という問題の直接的な解決策としては操作手順と実行環境（A）が優先される。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "欠陥発生時の操作手順および実行環境",           "is_correct": True,  "display_order": 1},
            {"choice_text": "欠陥発生時の期待結果と実際結果",               "is_correct": False, "display_order": 2},
            {"choice_text": "欠陥の重大度と優先度",                         "is_correct": False, "display_order": 3},
            {"choice_text": "欠陥修正後に想定される影響範囲",               "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q29
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるオンライン書店では、新しいおすすめ商品表示機能のテストを実施している。\n\n"
            "利用者の行動パターンが十分に把握できていないため、"
            "テスト担当者は90分のセッションを設定し、テスト中に得られた知見を記録しながら追加のテストを実施した。\n\n"
            "テスト終了後には、実施内容・発見した欠陥・今後の調査事項をまとめた。\n\n"
            "このテストアプローチとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "探索的テストは、事前に手順を固定せず、テスト設計・実行・学習を同時進行で行うテスト手法である。"
            "テスト担当者は実行中に得た知見をもとにリアルタイムで追加テストを判断し、"
            "終了後に実施内容・発見欠陥・今後の調査事項をまとめる。"
            "利用者の行動パターンが未知の状況で有効であり、経験ベーステスト技法の一種に位置づけられる。"
            "事前定義スクリプトによる自動テスト（D）や回帰テスト（B）・確認テスト（C）とは性質が異なる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "経験ベースのテスト技法を活用した探索的テスト", "is_correct": True,  "display_order": 1},
            {"choice_text": "要件ベースの回帰テスト",                      "is_correct": False, "display_order": 2},
            {"choice_text": "欠陥修正後の確認テスト",                      "is_correct": False, "display_order": 3},
            {"choice_text": "事前定義済みスクリプトによる自動テスト",       "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q30
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスでは、予約機能の改修を予定している。\n\n"
            "テストリーダーは、前回リリース時に作成した以下の成果物を確認している。\n"
            "- テストケース\n"
            "- テストデータ\n"
            "- テストスクリプト\n"
            "- テスト実行結果\n"
            "- 欠陥レポート\n\n"
            "テストリーダーは「前回の成果物を活用して効率的に回帰テストを計画したい」と考えている。\n\n"
            "これらの成果物を適切に保管・管理する主な目的として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト完了フェーズの活動のひとつがテストウェア（テストケース・テストデータ・テストスクリプト等）の適切なアーカイブである。"
            "保管の主目的は将来の回帰テスト・改修時のテスト計画・類似プロジェクトへの再利用であり、効率的なテスト活動につながる。"
            "担当者の業績評価（A）・要件変更防止（C）・テスト環境の復元（D）は成果物保管の主目的ではない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト担当者の作業履歴を評価するため",            "is_correct": False, "display_order": 1},
            {"choice_text": "将来のテスト活動で再利用できるようにするため",     "is_correct": True,  "display_order": 2},
            {"choice_text": "要件変更を防止するため",                          "is_correct": False, "display_order": 3},
            {"choice_text": "テスト環境を復元するため",                        "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q31
        "category": "テストマネジメント",
        "difficulty": 3,
        "question_text": (
            "あるECサイトのシステムテストでは、前回リリース時に以下の実績があった。\n\n"
            "- テストケース数：240件\n"
            "- 再テスト対象：テストケース数の15%\n"
            "- 総実施時間（テストケースと再テストの合計）：69時間\n\n"
            "今回のリリースでは、テストケース数は300件、再テスト対象はテストケース数の25%になると予測されている。\n\n"
            "テストケースおよび再テスト1件あたりの平均実施時間は前回と同じと仮定する。\n\n"
            "今回必要となる総実施時間として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "前回: テストケース240件 + 再テスト36件（240×15%）= 276件、69時間。"
            "1件あたりの平均実施時間は69÷276＝0.25時間。"
            "今回: テストケース300件 + 再テスト75件（300×25%）= 375件。"
            "見積もりは375×0.25＝93.75時間≒約94時間（B）。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "約84時間",  "is_correct": False, "display_order": 1},
            {"choice_text": "約94時間",  "is_correct": True,  "display_order": 2},
            {"choice_text": "約104時間", "is_correct": False, "display_order": 3},
            {"choice_text": "約114時間", "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q32
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "ある保険契約管理システムの要求仕様レビューを実施した。\n\n"
            "レビュー会議中に以下の状況が発生した。\n"
            "- 議論が仕様から脱線し始めた\n"
            "- 一部の指摘事項が記録されていないことが判明した\n"
            "- 終了予定時刻が近づいている\n\n"
            "プロジェクトマネージャは、レビューの進行方法を見直すよう求めた。\n\n"
            "この状況において、最も適切な対応の組み合わせはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "形式的なレビューでは役割の明確化が重要である。"
            "モデレータはレビューの進行を管理し、議論が脱線した際に軌道修正する責任を持つ。"
            "書記（レコーダー）は会議中に出た指摘事項を漏れなく記録する責任を持つ。"
            "作成者（A）はレビュー対象の説明役であり進行管理は担わない。"
            "レビューアは欠陥を指摘する役割で議論整理は担当しない。"
            "この状況で発生した「脱線」と「記録漏れ」の両問題に対応できるのはモデレータと書記の組み合わせ（B）である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "作成者が議論を整理し、レビューアが指摘事項を記録する",   "is_correct": False, "display_order": 1},
            {"choice_text": "モデレータが議論を整理し、書記が指摘事項を記録する",     "is_correct": True,  "display_order": 2},
            {"choice_text": "レビューアが議論を整理し、モデレータが指摘事項を記録する", "is_correct": False, "display_order": 3},
            {"choice_text": "書記が議論を整理し、作成者が指摘事項を記録する",         "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q33
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの要件定義書レビューで、以下の状況が発生した。\n\n"
            "- レビュー参加者が5名で、全員が自由に発言している\n"
            "- 指摘事項の記録が漏れていることに途中で気づいた\n"
            "- 一部の参加者が仕様とは関係ない話題を話し始めた\n"
            "- 終了予定時刻まであと15分しかない\n\n"
            "レビューを進行しているメンバーが改善を求めた。\n\n"
            "この状況で不足していたレビューの役割として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "形式的なレビューでは役割の明確化が重要であり、JSTQBシラバスでは以下の役割が定義されている。"
            "モデレータはレビューの進行を管理し、議論が脱線しないよう整理する責任を持つ。"
            "書記（レコーダー）は指摘事項を記録する責任を持つ。"
            "この事例では「議論の脱線」と「指摘の記録漏れ」が問題であり、"
            "モデレータと書記が不在または機能していなかったことが原因と判断できる。"
            "作成者はレビュー対象の成果物を説明する役割。"
            "ファシリテータはJSTQBシラバスの正式な役割名ではない。"
            "テストリーダーとプロジェクトマネージャはレビューの役割ではない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "作成者と書記",                         "is_correct": False, "display_order": 1},
            {"choice_text": "モデレータと書記",                     "is_correct": True,  "display_order": 2},
            {"choice_text": "レビューアとファシリテータ",            "is_correct": False, "display_order": 3},
            {"choice_text": "テストリーダーとプロジェクトマネージャ", "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q34
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスでは、以下の仕様を持つクーポン機能を開発している。\n\n"
            "- 会員のみ利用できる\n"
            "- 注文金額5,000円以上で利用できる\n"
            "- 一部商品は対象外である\n\n"
            "テスト担当者は「条件の組み合わせによる判定漏れがないこと」を確認したいと考えている。\n\n"
            "最も適切なテスト技法はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "デシジョンテーブルテストは、複数の条件の組み合わせによって動作が変わるシステムに適したブラックボックステスト技法である。"
            "「会員である・注文金額5,000円以上・対象商品かどうか」という3条件がクーポン利用可否を決定するケースでは、"
            "条件の組み合わせを表形式で整理することで判定漏れを体系的に防げる。"
            "同値分割（A）は単一条件の値のグループ化、境界値分析（B）は数値範囲の境界確認、"
            "探索的テスト（D）は条件の網羅的な確認には向かない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "同値分割",               "is_correct": False, "display_order": 1},
            {"choice_text": "境界値分析",             "is_correct": False, "display_order": 2},
            {"choice_text": "デシジョンテーブルテスト", "is_correct": True,  "display_order": 3},
            {"choice_text": "探索的テスト",           "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q35
        "category": "テスト技法",
        "difficulty": 3,
        "question_text": (
            "あるECサイトでは、割引クーポン機能を提供している。\n\n"
            "以前のテスト担当者は、以下のデシジョンテーブルを用いてテストを実施した。\n\n"
            "R1: 会員=Yes、注文金額5,000円以上=Yes、有効クーポン=Yes → 割引適用=Yes\n"
            "R2: 会員=No、その他=−（ドントケア） → 割引適用=No\n"
            "R3: 注文金額5,000円以上=No、その他=− → 割引適用=No\n"
            "R4: 有効クーポン=No、その他=− → 割引適用=No\n\n"
            "リリース後、「特定の条件の組み合わせで誤って割引が適用される」という欠陥が報告された。\n\n"
            "会員条件、注文金額条件、有効クーポン条件がそれぞれ独立した二値条件（Yes/No）であると仮定した場合、"
            "条件の組み合わせをすべて確認するために必要なルール数として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "二値条件（Yes/No）が3つ独立して存在する場合、条件の組み合わせは2の3乗で8通りとなる（C）。"
            "元のデシジョンテーブル（R1〜R4）ではドントケア（−）が多用されていたが、"
            "−は「その条件の値に関係なく結果が同じ」ことを意味し、実際に同じ結果かどうかは検証が必要である。"
            "安易に−としてまとめると確認漏れが生じる。"
            "たとえばR2「会員=No」の場合、注文金額やクーポンの状態によって異なる動作をする可能性がある。"
            "条件の組み合わせを網羅的に確認するには、ドントケアを展開して全8ルールを明示したテーブルを作成し、"
            "それぞれの期待結果を定義することが望ましい。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "4",  "is_correct": False, "display_order": 1},
            {"choice_text": "6",  "is_correct": False, "display_order": 2},
            {"choice_text": "8",  "is_correct": True,  "display_order": 3},
            {"choice_text": "12", "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q36
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスでは、利用者が以下の流れでサービスを利用する。\n\n"
            "1. 宿泊施設を検索する\n"
            "2. 詳細情報を確認する\n"
            "3. 予約する\n"
            "4. 支払いを行う\n"
            "5. 予約確認メールを受信する\n\n"
            "過去の障害分析では、検索・予約・支払いの各機能は正常であったにもかかわらず、"
            "予約確認メールが送信されず利用者が予約完了を確認できない不具合が発生していた。\n\n"
            "テスト担当者は「利用者が実際に行う一連の操作を通じてサービスを利用できること」を確認したいと考えている。\n\n"
            "最も適切なテスト技法はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ユースケーステストは、ユーザーとシステムの間の一連の対話シナリオ（ユースケース）に基づいてテストケースを設計する技法である。"
            "「検索→詳細確認→予約→支払い→確認メール受信」という一連のフローを通じてサービスの利用可否を確認するシナリオは、"
            "ユースケーステストが最も適している。"
            "状態遷移テスト（A）は状態とその遷移の確認、デシジョンテーブルテスト（B）は条件組み合わせの確認に用いる。"
            "エラー推測（D）は過去経験からバグ発生箇所を予測するアプローチで、エンドツーエンドの業務フロー確認には向かない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "状態遷移テスト",         "is_correct": False, "display_order": 1},
            {"choice_text": "デシジョンテーブルテスト", "is_correct": False, "display_order": 2},
            {"choice_text": "ユースケーステスト",      "is_correct": True,  "display_order": 3},
            {"choice_text": "エラー推測",              "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q37
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行では、本番環境に近いテスト環境を用意してシステムテストを実施している。\n\n"
            "しかし、本番環境では発生した不具合がテスト環境では再現しなかった。\n\n"
            "テストマネージャは「環境差異が影響している可能性がある」と考えている。\n\n"
            "この状況から得られる教訓として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト環境が本番環境と異なる場合、環境依存の欠陥がテストで検出されずに本番で発生するリスクがある。"
            "この事例はその典型であり、テスト環境と本番環境の差異は品質リスクとして認識・管理すべきである。"
            "本番環境との完全一致（A）が理想ではあるが、コストやセキュリティ制約から実現が難しいことも多く、"
            "差異が生じる可能性を前提にリスク管理を行うことが現実的である。"
            "性能テスト禁止（C）や環境構成を考慮しない（D）という考え方はリスクをさらに高める。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト環境は本番環境と完全に一致させることが望ましい",   "is_correct": False, "display_order": 1},
            {"choice_text": "テスト環境と本番環境の差異は品質リスクとなり得る",       "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト環境では性能テストを実施すべきではない",           "is_correct": False, "display_order": 3},
            {"choice_text": "システムテストでは環境構成を考慮する必要はない",         "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q38
        "category": "テストの基礎",
        "difficulty": 3,
        "question_text": (
            "ある税計算システムでは消費税率改定への対応を行った。\n\n"
            "テスト担当者は新しい税率での計算結果を確認していたところ、以下の状況となった。\n\n"
            "- 最新要求仕様書：11,000円\n"
            "- 旧バージョンシステム：10,800円\n"
            "- 税務部門が提示した計算例：11,000円\n\n"
            "今回の改修では、税率改定に伴い計算ロジックの変更が行われている。\n\n"
            "期待結果を判断する際に最も適切な情報源の組み合わせはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストオラクルとは、テスト実行の期待結果を決定するための根拠・情報源である。"
            "税率改定を伴う改修では、旧バージョンのシステム（A）は旧税率に基づく値を返すため期待結果の根拠にならない。"
            "最新要求仕様書（B）は変更後の仕様を定義する主要な情報源であり、"
            "税務部門の計算例（C）はドメイン専門家による正確な期待値を提供する。"
            "両者が11,000円で一致していることから、複数の情報源を組み合わせたDが最も信頼性の高いテストオラクルとなる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "旧バージョンシステムの計算結果",                     "is_correct": False, "display_order": 1},
            {"choice_text": "最新要求仕様書",                                    "is_correct": False, "display_order": 2},
            {"choice_text": "税務部門が提示した計算例",                           "is_correct": False, "display_order": 3},
            {"choice_text": "最新要求仕様書および税務部門が提示した計算例",         "is_correct": True,  "display_order": 4},
        ],
    },
    {   # Q39
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "ある保険契約管理システムではシステムテストが完了した。\n\n"
            "3か月後には同機能の改修プロジェクトが予定されており、"
            "現在利用しているテスト環境は他プロジェクトが利用する予定である。\n\n"
            "テストリーダーは、テスト完了活動として優先的に実施すべき内容を整理している。\n\n"
            "最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト完了フェーズでは、①テストウェアのアーカイブ・保管、"
            "②テスト結果・完了レポートの関係者への共有、"
            "③不要となったテスト環境・リソースの解放、"
            "④次プロジェクトへの教訓の整理などを行う。"
            "3か月後の改修プロジェクトへの引き継ぎと他プロジェクトへの環境解放が必要な文脈では、"
            "成果物保管・結果共有・環境解放の3点すべてが求められる。"
            "A〜Cはそれぞれ要素の一部しか含んでおらず、業務継続性の観点で不十分である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト成果物を保管し、改善提案をまとめて関係者へ共有する",                                   "is_correct": False, "display_order": 1},
            {"choice_text": "テスト結果を関係者へ共有し、不要となったテスト環境を解放する",                               "is_correct": False, "display_order": 2},
            {"choice_text": "テスト成果物を保管し、不要となったテスト環境を解放する",                                     "is_correct": False, "display_order": 3},
            {"choice_text": "テスト成果物を保管し、テスト結果を関係者へ共有したうえで、不要となったテスト環境を解放する",   "is_correct": True,  "display_order": 4},
        ],
    },
    {   # Q40
        "category": "テストマネジメント",
        "difficulty": 3,
        "question_text": (
            "あるオンライン書店では、大規模な機能改修を実施した。\n\n"
            "システムテスト終了時点で以下の状況となっている。\n\n"
            "- 要件カバレッジ：98%\n"
            "- 重大度高欠陥：0件\n"
            "- 中重大度欠陥：6件\n"
            "- 未実施テスト：1%\n\n"
            "プロジェクトマネージャはリリース可否を判断しようとしている。\n\n"
            "最も適切な判断はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト終了基準はリリース可否の自動判定ではなく、判断のための参照指標である。"
            "要件カバレッジ98%・重大度高欠陥0件・未実施テスト1%という状況は基準を概ね満たしているが、"
            "中重大度欠陥6件の内容・影響・回避策を残存リスクとして評価し、"
            "プロジェクトマネージャと関係者が合意したうえでリリース可否を判断することが求められる。"
            "単一の達成指標のみでリリース判断する（A・B）のも、欠陥の存在のみで一律拒否する（D）のも、"
            "リスクベースの判断として不十分である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "要件カバレッジが高いため即時リリースする",          "is_correct": False, "display_order": 1},
            {"choice_text": "未実施テストが少ないため即時リリースする",          "is_correct": False, "display_order": 2},
            {"choice_text": "残存リスクを評価したうえでリリース可否を判断する",   "is_correct": True,  "display_order": 3},
            {"choice_text": "欠陥が残っているためリリースしてはならない",         "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # ツール支援  2問（既存Q39–Q40を維持）
    # ══════════════════════════════════════════════════════════════

    {   # Q41
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
            {"choice_text": "反復実行の効率化と一貫性のあるテスト実行を実現できる", "is_correct": True,  "display_order": 2},
            {"choice_text": "テストケース設計の作業を不要にできる",                           "is_correct": False, "display_order": 3},
            {"choice_text": "テストの意思決定をツールに委任できる",                           "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q42
        "category": "ツール支援",
        "difficulty": 1,
        "question_text": "テスト管理ツール（test management tool）の主な機能として最も適切なものはどれか。",
        "multi_select_count": 1,
        "explanation": (
            "テスト管理ツールは、テスト活動全体を組織的に管理するためのツールです。"
            "主な機能として、テストケースの登録・管理・テスト実行の計画と追跡・"
            "欠陥の記録と状態管理・テスト進捗レポートの生成などが挙げられます。"
            "JIRAやTestRailなどが代表的なツールです。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ソースコードを自動的にテストコードに変換する",                            "is_correct": False, "display_order": 1},
            {"choice_text": "テストケースの管理・テスト実行の追跡・欠陥管理・テスト結果のレポート作成を支援する", "is_correct": True,  "display_order": 2},
            {"choice_text": "ネットワーク越しのシステムに対してのみ使用できる",                        "is_correct": False, "display_order": 3},
            {"choice_text": "テスト担当者のパフォーマンスを自動評価する",                             "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # テストの基礎  追加7問（Q43–Q49）
    # ══════════════════════════════════════════════════════════════

    {   # Q43 (MD第41問)
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの注文機能において、テスト担当者が以下の事象を記録した。\n\n"
            "- 金額が0円の注文を確定できてしまった\n"
            "- 開発担当者がコードを調査したところ、金額の入力チェック処理が実装されていないことが判明した\n"
            "- 要求仕様書には「注文金額は1円以上であること」と明記されていた\n\n"
            "この事象において、「欠陥」「誤り」「障害」をJSTQB FL の定義に基づいて正しく対応付けているものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL シラバスでは以下のように定義されている。\n"
            "誤り（Error）: 人間が起こすミス。今回は「要求仕様を見落として入力チェックを実装しなかった開発担当者の行為」が該当する。\n"
            "欠陥（Defect / Bug）: 誤りによってコードや成果物に生じた不備。今回は「入力チェック処理が実装されていないコードの状態」が該当する。\n"
            "障害（Failure）: 欠陥が実行されたことで発生する、期待と異なる動作。今回は「0円注文が確定できてしまった事象」が該当する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "0円注文が確定できた事象が「欠陥」、入力チェック処理が実装されていないことが「障害」、要求仕様を見落とした開発担当者の行為が「誤り」", "is_correct": False, "display_order": 1},
            {"choice_text": "入力チェック処理が実装されていないことが「欠陥」、0円注文が確定できた事象が「障害」、要求仕様を見落とした開発担当者の行為が「誤り」", "is_correct": True,  "display_order": 2},
            {"choice_text": "要求仕様を見落とした開発担当者の行為が「欠陥」、入力チェック処理が実装されていないことが「誤り」、0円注文が確定できた事象が「障害」", "is_correct": False, "display_order": 3},
            {"choice_text": "入力チェック処理が実装されていないことが「誤り」、0円注文が確定できた事象が「欠陥」、要求仕様を見落とした開発担当者の行為が「障害」", "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q44 (MD第42問)
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスでは、新機能の開発を進めている。\n\n"
            "開発チームのリーダーは「テストはすべての欠陥を発見できるので、テストを十分に実施すれば品質は完全に保証できる」と発言した。\n\n"
            "JSTQB FL のテストの原則に照らして、この発言の問題点として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL の「テストの原則」のひとつに「テストは欠陥があることは示せるが、欠陥がないことは示せない」がある。"
            "テストによって欠陥を発見し品質を改善することはできるが、「すべての欠陥を発見できる」「品質を完全に保証できる」という主張は原則に反する。"
            "また「完全なテストは不可能」という原則もあり、すべての入力・条件の組み合わせをテストすることは現実的ではない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストは欠陥を発見するものであり、欠陥がないことを証明することはできない", "is_correct": True,  "display_order": 1},
            {"choice_text": "テストは自動化しなければ十分な品質保証にならない",                     "is_correct": False, "display_order": 2},
            {"choice_text": "テストは開発の最終工程でのみ実施すべきである",                         "is_correct": False, "display_order": 3},
            {"choice_text": "テストは仕様書がなければ実施できない",                                 "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q45 (MD第43問)
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームでは、新しい決済機能の開発が完了した。\n\n"
            "テストマネージャは「どのテストレベルで、誰が、何をテストするか」を整理している。\n\n"
            "テストレベルの責任と対象の説明として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストレベルはそれぞれ目的・対象・主な実施者が異なる。\n"
            "単体テスト（コンポーネントテスト）: 個別コンポーネントの動作確認。主に開発担当者が実施する。\n"
            "結合テスト: コンポーネント間のインターフェース・連携の確認。主に開発担当者やテスト担当者が実施する。\n"
            "システムテスト: システム全体の動作確認。主にテスト担当者が実施する。\n"
            "受入テスト: ビジネス要件の充足確認。主にユーザーやビジネスオーナーが実施する。\n"
            "Aはシステムテストの説明、Cは単体テストの説明、Dは受入テストの実施者が誤り。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "単体テストはシステム全体の動作を確認するもので、主にテスト担当者が実施する",                          "is_correct": False, "display_order": 1},
            {"choice_text": "結合テストはコンポーネント間のインターフェースや連携を確認するもので、主に開発担当者やテスト担当者が実施する", "is_correct": True,  "display_order": 2},
            {"choice_text": "システムテストは個別コンポーネントの内部ロジックを確認するもので、主に開発担当者が実施する",           "is_correct": False, "display_order": 3},
            {"choice_text": "受入テストは技術的な品質を確認するもので、主にテスト担当者が実施する",                                "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q46 (MD第44問)
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスの開発プロジェクトでは、開発初期に要求仕様書のレビューを実施したところ、複数の欠陥が発見された。\n\n"
            "プロジェクトマネージャは「早期のレビューで発見できてコストが抑えられた」と評価した。\n\n"
            "この評価の根拠として JSTQB FL の観点から最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL の「テストの原則」のひとつに「早期テストで時間とコストを節約できる」がある。"
            "欠陥は発見が遅い工程ほど修正コストが高くなる傾向があり、要求仕様の欠陥が実装・テスト・リリース後に発見された場合、修正の影響範囲が大きくなる。"
            "早期に欠陥を発見・修正することでプロジェクト全体のコストを抑えられる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "レビューは開発工程の後半にまとめて実施した方がコスト効率が高い",         "is_correct": False, "display_order": 1},
            {"choice_text": "欠陥は発見が遅くなるほど修正コストが高くなる傾向がある",               "is_correct": True,  "display_order": 2},
            {"choice_text": "要求仕様書の欠陥はテスト工程で発見することが最も効率的である",           "is_correct": False, "display_order": 3},
            {"choice_text": "欠陥の修正コストは発見した工程に関係なく一定である",                    "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q47 (MD第45問)
        "category": "テストの基礎",
        "difficulty": 3,
        "question_text": (
            "あるECサイトの開発チームでは、リリースのたびに同じ回帰テストを繰り返し実施していた。\n\n"
            "最初のうちは毎回欠陥が発見されていたが、しばらくするとほとんど欠陥が発見されなくなった。\n\n"
            "しかしリリース後に、テストでカバーしていなかった新しい操作パターンで障害が発生した。\n\n"
            "この状況に関連するテストの原則として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL v4.0 の「テストの弱化」とは、同じテストを繰り返し実施すると、そのテストが新しい欠陥を発見する効果が低下する現象を指す。"
            "欠陥が発見されなくなった理由は担当者の習熟度ではなく、テストが既知のパターンしかカバーしていないことにある。"
            "テストケースを定期的に見直し、新しい観点・未確認の操作パターンを追加することでテストの有効性を維持することが重要である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストを繰り返すほど欠陥発見率が上がるため、同じテストを継続することが最善策である", "is_correct": False, "display_order": 1},
            {"choice_text": "テスト担当者の習熟度が上がったため欠陥が発見されなくなったと判断してよい",         "is_correct": False, "display_order": 2},
            {"choice_text": "同じテストを繰り返すとテストが新しい欠陥を見つける効果が下がる",                  "is_correct": True,  "display_order": 3},
            {"choice_text": "テストは均等に全機能へ配分するべきである",                                        "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q48 (MD第46問)
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるオンライン書店の開発プロジェクトでは、コンテキスト（状況・環境）に応じてテストアプローチを変える必要があることが議論された。\n\n"
            "以下の状況のうち、テストアプローチを変える必要があるコンテキストの違いとして最も適切な組み合わせはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL の「テストはコンテキスト次第」という原則では、テストアプローチはプロジェクトの性質・リスク・制約によって異なることが示されている。"
            "医療システムのような安全性重視のシステムでは厳密な検証が求められる一方、短サイクルのリリースを繰り返すシステムでは迅速なフィードバックを重視したテストアプローチが求められる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "安全性が重要な医療システムと、短サイクルでリリースするECサイトでは同じアプローチが適切である",      "is_correct": False, "display_order": 1},
            {"choice_text": "安全性が重要な医療システムと、短サイクルでリリースするECサイトでは求められるテストの厳密さや手法が異なる", "is_correct": True,  "display_order": 2},
            {"choice_text": "プロジェクト規模が大きくなるほど自動テストのみに移行すべきである",                                    "is_correct": False, "display_order": 3},
            {"choice_text": "コンテキストに関係なく、すべてのプロジェクトで同じテストプロセスを適用すべきである",                  "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q49 (MD第47問)
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスの開発チームでは、新機能のリリース前にさまざまなテストを計画している。\n\n"
            "以下のテストのうち「非機能テスト」として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストタイプは「機能テスト」「非機能テスト」「ホワイトボックステスト」「変更関連テスト」の4つに分類される。"
            "機能テストは「システムが何をするか（What）」を確認するテストであり、非機能テストは「システムがどのように動作するか（How well）」を確認するテストである。"
            "レスポンスタイム・スループット・同時接続数などを確認する性能テストは非機能テストの代表例である。"
            "A・C・D はいずれも「何ができるか」を確認する機能テストに該当する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "予約確認メールが正しい内容で送信されることを確認するテスト",                           "is_correct": False, "display_order": 1},
            {"choice_text": "同時に1,000件の予約リクエストが発生した場合のレスポンスタイムを確認するテスト",         "is_correct": True,  "display_order": 2},
            {"choice_text": "予約ボタンを押した後に予約が登録されることを確認するテスト",                           "is_correct": False, "display_order": 3},
            {"choice_text": "キャンセル手続きを行った後に予約が取り消されることを確認するテスト",                   "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # テスト活動とプロセス  追加7問（Q50–Q56）
    # ══════════════════════════════════════════════════════════════

    {   # Q50 (MD第48問)
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発プロジェクトでは、システムテスト開始前にテストマネージャがテスト計画を作成しようとしている。\n\n"
            "テスト計画に含めるべき内容として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト計画は「何を・どのように・いつ・誰が・どのリソースでテストするか」を定義する文書である。"
            "具体的にはテストの目的・対象範囲・アプローチ・使用する技法・必要なリソース（人・環境・ツール）・スケジュール・リスクと対策などを含む。"
            "テスト設計ではテスト条件をカバーするテストケースを設計し入力値と期待結果を定義する。"
            "テスト実装ではテストケースをもとにテスト手順・テストデータ・テストスクリプトを具体化する。"
            "欠陥一覧はテスト実行の成果物、運用手順はテストの範囲外である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストの目的・対象範囲・アプローチ・リソース・スケジュール", "is_correct": True,  "display_order": 1},
            {"choice_text": "テストケースの具体的な入力値と期待結果",                   "is_correct": False, "display_order": 2},
            {"choice_text": "テスト実行中に発見された欠陥の一覧",                       "is_correct": False, "display_order": 3},
            {"choice_text": "テスト完了後のシステムの運用手順",                         "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q51 (MD第49問)
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行のプロジェクトでは、テスト担当者が結合テストの開始基準（エントリークライテリア）を確認している。\n\n"
            "開始基準として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "開始基準（エントリークライテリア）は「このテストフェーズを始めるために満たすべき条件」を定義する。"
            "結合テストの場合、前工程である単体テストが完了していること、および結合対象のコンポーネントがテスト環境に揃っていることが典型的な開始基準となる。"
            "全テストケースの合格や全欠陥の修正は終了基準（エグジットクライテリア）に該当し、開始基準ではない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "全テストケースが合格していること",                                        "is_correct": False, "display_order": 1},
            {"choice_text": "単体テストが完了し、結合対象のコンポーネントがテスト環境に導入されていること", "is_correct": True,  "display_order": 2},
            {"choice_text": "本番環境へのリリース承認が完了していること",                              "is_correct": False, "display_order": 3},
            {"choice_text": "欠陥がすべて修正されていること",                                         "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q52 (MD第50問)
        "category": "テスト活動とプロセス",
        "difficulty": 3,
        "question_text": (
            "あるECサイトのシステムテストでは、テスト実行の途中でテストマネージャが以下の状況を確認した。\n\n"
            "- 予定テストケース数：500件\n"
            "- 実施済み：320件\n"
            "- 合格：290件\n"
            "- 不合格：30件\n"
            "- 未解決欠陥（重大度高）：8件\n"
            "- 残り期間：3日\n\n"
            "テストマネージャが最も優先して対応すべき事項として適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストモニタリングとコントロールの活動では、進捗・品質状況・リスクを継続的に評価し、必要に応じてステークホルダーへ報告・判断を仰ぐことが求められる。"
            "重大度高の欠陥が8件残っている状況と残り3日という制約は重大なリスクであり、"
            "「残りのテスト完了可能性」「欠陥修正の見通し」「リリース可否」についてステークホルダーと合意を形成することが最優先となる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "残り180件のテストケースをすべて実施してから欠陥対応を判断する",                                          "is_correct": False, "display_order": 1},
            {"choice_text": "重大度高の欠陥8件の修正状況と残り期間でのテスト完了可能性をリスク評価してステークホルダーへ報告する", "is_correct": True,  "display_order": 2},
            {"choice_text": "合格率が90%超のため、テストは順調と判断してそのまま継続する",                                           "is_correct": False, "display_order": 3},
            {"choice_text": "不合格件数が多いためテストを中断してリリースを延期する",                                                  "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q53 (MD第51問)
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームでは、開発担当者が自分の実装したコードを自分でテストする体制をとっていた。\n\n"
            "テストリーダーはこの体制を見直し、別担当者がテストを実施する体制への移行を提案した。\n\n"
            "テスト独立性を高めることの主なメリットとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト独立性とは、テストを実施する人物が成果物の作成者から分離されている度合いを指す。"
            "開発担当者は自分が書いたコードに対して「こう動くはず」という思い込み（認知バイアス）を持ちやすく、欠陥を見落としやすい。"
            "独立したテスト担当者はその先入観なく確認できるため、見落とされやすい欠陥を発見しやすいというメリットがある。\n"
            "ただし独立性を高めることのデメリットも存在する。"
            "開発担当者とテスト担当者間のコミュニケーションコストが増加すること、"
            "また「テストは別の人がやるもの」という意識が広まることで開発担当者の品質意識が低下するリスクがある。Cは逆の説明であり誤り。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "開発担当者は自分のコードに詳しいため、独立したテスト担当者より欠陥を発見しやすい",       "is_correct": False, "display_order": 1},
            {"choice_text": "独立したテスト担当者は思い込みや先入観なくテストできるため、開発担当者が見落とした欠陥を発見しやすい", "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト独立性を高めると、開発担当者の品質に対する責任意識が向上する",                     "is_correct": False, "display_order": 3},
            {"choice_text": "独立したテスト担当者はコードの詳細を把握しているため、テスト設計が容易になる",           "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q54 (MD第52問)
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるオンライン書店では、新機能のテストが完了し、テストサマリーレポートを作成することになった。\n\n"
            "テストサマリーレポートに記載すべき内容として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストサマリーレポートはテスト活動の終了時に作成する文書であり、ステークホルダーへテスト結果を伝えることを目的とする。"
            "記載内容としては「テスト実施結果の概要（実施件数・合格・不合格）」「欠陥の発見数・状況・未解決件数」"
            "「終了基準の達成状況」「残存するリスク」「プロセス改善への提言」などが含まれる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "次のプロジェクトで使用するテスト計画のドラフト",                     "is_correct": False, "display_order": 1},
            {"choice_text": "テスト実施結果の概要・欠陥状況・終了基準の達成状況・残存リスク",     "is_correct": True,  "display_order": 2},
            {"choice_text": "開発担当者へのコードレビュー指摘事項",                               "is_correct": False, "display_order": 3},
            {"choice_text": "本番環境の監視ダッシュボードの設定方法",                             "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q55 (MD第53問)
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発プロジェクトでは、テスト担当者がテスト実行後に以下の状況を確認した。\n\n"
            "- 実際の結果が期待結果と異なっていた\n"
            "- テスト担当者は「これは欠陥である」と判断した\n\n"
            "テスト担当者が次に行うべき活動として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト実行中に期待結果と異なる結果を確認した場合、欠陥レポートを作成して欠陥管理システムに登録することが標準的なプロセスである。"
            "欠陥レポートには発生手順・実際の結果・期待結果・実行環境・重大度・優先度などを記載する。"
            "口頭での連絡だけでは追跡・管理ができず、欠陥の修正確認や再発防止の分析に支障をきたす。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "直ちに本番環境での影響を調査する",                             "is_correct": False, "display_order": 1},
            {"choice_text": "欠陥レポートを作成し、欠陥管理システムに登録する",             "is_correct": True,  "display_order": 2},
            {"choice_text": "開発担当者に口頭で伝えて即時修正を依頼する",                   "is_correct": False, "display_order": 3},
            {"choice_text": "テストを中断してプロジェクトマネージャに報告する",             "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q56 (MD第54問)
        "category": "テスト活動とプロセス",
        "difficulty": 3,
        "question_text": (
            "あるネット銀行のプロジェクトでは、テスト完了後に振り返り会議（レトロスペクティブ）が実施された。\n\n"
            "チームから以下の意見が出た。\n\n"
            "- 「テスト環境の構築に時間がかかり、実際のテスト時間が圧迫された」\n"
            "- 「テストケースのレビューを実施しなかったため、観点の抜け漏れが多かった」\n"
            "- 「欠陥レポートの記載が不統一で、開発担当者が再現できない欠陥が多かった」\n\n"
            "この会議の主な目的として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト完了活動のひとつである振り返り（レトロスペクティブ）の目的は、"
            "「プロセスの課題・成功点を特定し、次のプロジェクトやイテレーションへの改善につなげること」である。"
            "責任者の特定や個人評価を目的とするものではなく、チーム全体でプロセスを改善するための活動である。"
            "今回挙げられた3つの意見はいずれも次回への具体的な改善項目として活用できる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "発生した問題の責任者を特定して対応策を検討する",                                        "is_correct": False, "display_order": 1},
            {"choice_text": "プロセスの課題を特定し、次のプロジェクトや次のイテレーションへ改善を反映させる",       "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト担当者の評価を行い、パフォーマンスに応じたタスクを割り当てる",                   "is_correct": False, "display_order": 3},
            {"choice_text": "テスト完了の承認をステークホルダーから得る",                                           "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # 静的テスト  追加6問（Q57–Q62）
    # ══════════════════════════════════════════════════════════════

    {   # Q57 (MD第55問)
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるオンライン書店の開発プロジェクトで、テスト担当者が要求仕様書を確認したところ以下の記載を見つけた。\n\n"
            "「検索結果は適切な順序で表示されること」\n\n"
            "この記述の問題点として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "要求仕様書に記載される条件は「テスト可能（Testable）」であることが重要な品質特性のひとつである。"
            "「適切な順序」という表現は判断基準が人によって異なり、テスト担当者が期待結果を定義できない。"
            "正しくは「関連度スコアの高い順に表示する」「新着順に表示する」など具体的な判断基準を明記する必要がある。"
            "このような曖昧な記述は静的テスト（レビュー）で発見・修正すべき欠陥である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "検索機能はテストが難しいため、この記述でよい",                          "is_correct": False, "display_order": 1},
            {"choice_text": "「適切な順序」が曖昧であり、テスト可能な基準として機能しない",          "is_correct": True,  "display_order": 2},
            {"choice_text": "検索結果の順序はシステムが自動的に決定するため仕様書に記載不要である",   "is_correct": False, "display_order": 3},
            {"choice_text": "要求仕様書への記載ではなく画面設計書に記載すべき内容である",            "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q58 (MD第56問)
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発プロジェクトで、要求仕様書のレビューを計画している。\n\n"
            "レビュー参加者を決める際、作成者（仕様書の執筆者）も参加させることへの懸念意見が出た。\n\n"
            "この懸念に対する最も適切な考え方はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "形式的なレビューにおいて、作成者は重要な役割を担う。"
            "作成者はレビュー対象の成果物の背景・意図・制約を最もよく知っており、"
            "レビューアの指摘に対して「なぜそのように書いたか」を説明することで議論の質が向上する。"
            "ただし、作成者は指摘を防衛的に受け取らず、欠陥の改善に前向きに取り組む姿勢が求められる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "作成者はレビューに参加すべきではない。なぜなら自身の欠陥を発見するのは困難だからである",     "is_correct": False, "display_order": 1},
            {"choice_text": "作成者はレビューに参加すべきである。なぜなら指摘事項の背景を説明する役割を担うからである", "is_correct": True,  "display_order": 2},
            {"choice_text": "作成者はレビューに参加しても意見を述べてはならない",                                       "is_correct": False, "display_order": 3},
            {"choice_text": "作成者はレビューの主導権を持ち、指摘に反論する役割を担う",                                 "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q59 (MD第57問)
        "category": "静的テスト",
        "difficulty": 3,
        "question_text": (
            "あるネット銀行では、基幹システムの設計書に対してインスペクションを実施した。\n\n"
            "インスペクションの特徴として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL シラバスでは、レビューの形式として「非公式レビュー」「ウォークスルー」「テクニカルレビュー」「インスペクション」が定義されている。"
            "インスペクションは最も形式的なレビュー形式であり、以下の特徴を持つ。\n"
            "- 形式的な役割（モデレータ・作成者・レビューア・書記）が定義されている\n"
            "- 入口基準・チェックリスト・メトリクス・出口基準を使用する\n"
            "- レビューアは事前に成果物を確認し、個別に欠陥を識別する\n"
            "- レビュー会議では欠陥の発見に集中し、修正方法の議論は行わない"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "参加者全員が自由に発言し、議事録は作成しない非公式なレビュー形式である",                                   "is_correct": False, "display_order": 1},
            {"choice_text": "形式的な役割（モデレータ・書記・レビューア）を設け、入口基準・チェックリスト・出口基準を用いる最も形式的なレビュー形式である", "is_correct": True,  "display_order": 2},
            {"choice_text": "作成者が成果物を口頭で説明し、参加者がリアルタイムでフィードバックする形式である",                         "is_correct": False, "display_order": 3},
            {"choice_text": "レビューアが事前に成果物を確認せず、会議の場で初めて内容を確認する形式である",                            "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q60 (MD第58問)
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスの開発チームでは、コードレビューを実施しているが、レビューの効果が低いという課題があった。\n\n"
            "改善策として「チェックリストの導入」が提案された。\n\n"
            "チェックリストを用いたレビューの利点として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "チェックリストを用いたレビューの主な利点は「過去の経験から蓄積されたよくある欠陥パターンを体系的に確認でき、重要な観点の見落としを防げる」点にある。"
            "チェックリストはレビューの基準を統一し、担当者によるレビュー品質のばらつきを抑える効果もある。"
            "ただしチェックリストは「確認すべき最低限の観点」であり、チェックリスト以外の観点も状況に応じて確認することが求められる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "チェックリストがあれば、レビューアは成果物を読む必要がなくなる",                         "is_correct": False, "display_order": 1},
            {"choice_text": "チェックリストにない観点は確認しなくてよい基準が明確になる",                             "is_correct": False, "display_order": 2},
            {"choice_text": "よくある欠陥パターンを体系的に確認でき、重要な観点の見落としを防げる",                   "is_correct": True,  "display_order": 3},
            {"choice_text": "チェックリストを使用すると、レビューの実施時間が2倍以上必要になる",                       "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q61 (MD第59問)
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームでは、静的テストの対象について議論していた。\n\n"
            "静的テストの対象として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "静的テストはソフトウェアを実行せずに欠陥を発見するテスト活動であり、さまざまな作業成果物を対象にできる。"
            "具体的には要求仕様書・設計書・ソースコード・テストケース・テスト計画書・ユーザーマニュアルなどが対象となる。"
            "動的テスト（実行を伴うテスト）と組み合わせることで、ライフサイクル全体を通じた品質改善が可能になる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ソースコードのみ",                                                                     "is_correct": False, "display_order": 1},
            {"choice_text": "要求仕様書・設計書・ソースコード・テストケースなど、さまざまな作業成果物",               "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト実行の結果ログのみ",                                                             "is_correct": False, "display_order": 3},
            {"choice_text": "本番環境で稼働しているシステムの動作",                                                 "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q62 (MD第60問)
        "category": "静的テスト",
        "difficulty": 3,
        "question_text": (
            "あるオンライン書店の開発チームでは、スプリントレビューの場でプロダクトオーナーとチームメンバーが新機能の動作確認を行った。\n\n"
            "この活動の静的テストとしての位置づけとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "静的テストはソフトウェアを「実行せずに」欠陥を発見する活動であり、レビューや静的解析が該当する。"
            "スプリントレビューでは実際にソフトウェアを動作させて確認するため、動的テストに分類される。"
            "静的テスト（レビュー）の典型的な対象はソースコード・仕様書・設計書などの成果物であり、実行を伴うものは動的テストとなる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ソフトウェアを実行しているため動的テストであり、静的テストには該当しない",                        "is_correct": True,  "display_order": 1},
            {"choice_text": "参加者が成果物の動作を確認しているが、欠陥の有無を評価しているため静的テストに該当する",           "is_correct": False, "display_order": 2},
            {"choice_text": "スプリントレビューは静的テストの一形態であるインスペクションに該当する",                          "is_correct": False, "display_order": 3},
            {"choice_text": "プロダクトオーナーが参加しているため、受入テストに分類される",                                    "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # テスト技法  追加7問（Q63–Q69）
    # ══════════════════════════════════════════════════════════════

    {   # Q63 (MD第61問)
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるECサイトでは、ポイント会員の割引率を以下のように定めている。\n\n"
            "- 保有ポイント0〜999ポイント：割引なし\n"
            "- 保有ポイント1000〜4999ポイント：5%割引\n"
            "- 保有ポイント5000ポイント以上：10%割引\n\n"
            "境界値分析を適用する場合、テスト値として最も適切な組み合わせはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "境界値分析では各同値クラスの「境界」付近の値を重点的にテストする。この仕様では以下の境界が存在する。\n"
            "割引なし/5%割引の境界: 999（最大値）・1000（最小値）\n"
            "5%割引/10%割引の境界: 4999（最大値）・5000（最小値）\n"
            "下限境界: 0（最小値）・1（次の値）\n"
            "上限は仕様に明記がないため5001など5000超の値で確認\n"
            "各境界の直前・直後の値をテストすることで、境界付近での条件分岐の誤りを効率的に発見できる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "500ポイント、2500ポイント、7500ポイント",                     "is_correct": False, "display_order": 1},
            {"choice_text": "0、999、1000、4999、5000、5001ポイント（および上限付近の値）", "is_correct": True,  "display_order": 2},
            {"choice_text": "1000ポイント、5000ポイントのみ",                              "is_correct": False, "display_order": 3},
            {"choice_text": "0ポイント、5000ポイント、10000ポイント",                       "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q64 (MD第62問)
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスでは、注文のキャンセル可否を以下のルールで制御している。\n\n"
            "- 注文確定前：キャンセル可\n"
            "- 注文確定後・配達員出発前：キャンセル可（手数料あり）\n"
            "- 配達員出発後：キャンセル不可\n\n"
            "テスト担当者が状態遷移テストを設計する際、最初に行うべきことして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "状態遷移テストでは、まずシステムの「状態（State）」「イベント（Event）」「遷移（Transition）」「ガード条件」「アクション」を整理した"
            "状態遷移図または状態遷移表を作成することが出発点となる。"
            "この図表をもとにテストシナリオ（どの状態からどのイベントでどの状態へ遷移するか）を設計する。"
            "テスト環境の準備やコードの読解はその後の工程である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト実行環境を準備する",                                                             "is_correct": False, "display_order": 1},
            {"choice_text": "システムの取り得る状態と状態変化の条件を図表として整理する",                         "is_correct": True,  "display_order": 2},
            {"choice_text": "境界値となる注文金額を洗い出す",                                                       "is_correct": False, "display_order": 3},
            {"choice_text": "キャンセル機能のソースコードを読む",                                                   "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q65 (MD第63問)
        "category": "テスト技法",
        "difficulty": 3,
        "question_text": (
            "あるネット銀行では、ローン申込の可否を以下の条件で判定している。\n\n"
            "- 年収300万円以上\n"
            "- 勤続年数1年以上\n"
            "- 信用スコア600点以上\n\n"
            "テスト担当者はデシジョンテーブルテストを適用し、全条件の組み合わせを確認したいと考えている。\n\n"
            "全ルールを網羅した場合に必要な最小ルール数として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "二値条件（満たす/満たさない）が3つ独立して存在する場合、条件の組み合わせは 2³ = 8通り となる。"
            "各ルールは「年収300万円以上/未満」×「勤続1年以上/未満」×「信用スコア600点以上/未満」の組み合わせであり、"
            "すべての組み合わせを確認するには8ルール必要である。"
            "デシジョンテーブルを用いることで、複数の条件が組み合わさる判定ロジックの確認漏れを防ぐことができる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "3",  "is_correct": False, "display_order": 1},
            {"choice_text": "6",  "is_correct": False, "display_order": 2},
            {"choice_text": "8",  "is_correct": True,  "display_order": 3},
            {"choice_text": "12", "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q66 (MD第64問)
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスでは、「チェックアウト日はチェックイン日より後でなければならない」という仕様がある。\n\n"
            "テスト担当者がエラー推測を適用してテストケースを追加しようとしている。\n\n"
            "エラー推測で追加するテストケースとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "エラー推測は「経験・直感・過去の欠陥情報」をもとに、欠陥が潜みやすい条件を推測してテストケースを設計する技法である。"
            "「チェックアウト日はチェックイン日より後」という仕様に対して、「同じ日付を入力する（境界となる等値ケース）」は典型的な誤りが起きやすい入力パターンであり、エラー推測として適切である。"
            "また「チェックアウト日がチェックイン日より前」「日付を空欄にする」なども同様に推測されるテストケースとなる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "通常の宿泊日程（チェックイン: 明日、チェックアウト: 3日後）", "is_correct": False, "display_order": 1},
            {"choice_text": "チェックアウト日にチェックイン日と同じ日付を入力する",       "is_correct": True,  "display_order": 2},
            {"choice_text": "宿泊人数に最大値を入力する",                                 "is_correct": False, "display_order": 3},
            {"choice_text": "支払方法としてクレジットカードを選択する",                   "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q67 (MD第65問)
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるECサイトでは、ポイント還元率を以下のように設定している。\n\n"
            "- 通常会員：1%\n"
            "- シルバー会員（年間購入額10万円以上）：2%\n"
            "- ゴールド会員（年間購入額30万円以上）：3%\n\n"
            "同値分割法を適用してテストクラスを識別する場合、有効同値クラスの数として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "同値分割法では「同じ処理結果になる入力値のグループ」を同値クラスとして識別する。"
            "この仕様では年間購入額に応じて3つの異なる処理結果（1%・2%・3%還元）が存在するため、有効同値クラスは3つとなる。\n"
            "0〜99,999円：通常会員（1%還元）\n"
            "100,000〜299,999円：シルバー会員（2%還元）\n"
            "300,000円以上：ゴールド会員（3%還元）\n"
            "これに加えて、無効同値クラス（マイナス値・非数値など）も検討する必要がある。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "1", "is_correct": False, "display_order": 1},
            {"choice_text": "2", "is_correct": False, "display_order": 2},
            {"choice_text": "3", "is_correct": True,  "display_order": 3},
            {"choice_text": "4", "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q68 (MD第66問)
        "category": "テスト技法",
        "difficulty": 3,
        "question_text": (
            "あるオンライン書店では、ユーザーが「お気に入り登録」→「カートに追加」→「購入」という一連の操作を行う。\n\n"
            "テスト担当者は、この一連の操作フローに対してユースケーステストを設計しようとしている。\n\n"
            "ユースケーステストの主な目的として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ユースケーステストは「利用者がシステムをどのように使うか」というシナリオをもとに、複数の機能をまたぐ一連の操作フローを確認するテスト技法である。"
            "個別の機能が正常に動作していても、機能間の連携や状態の引き継ぎに問題がある場合にこの技法で発見しやすい。"
            "境界値確認・性能測定・コードカバレッジはそれぞれ別の技法・目的に該当する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "各画面の入力値の境界値を確認すること",                           "is_correct": False, "display_order": 1},
            {"choice_text": "システム全体の性能（レスポンスタイム）を測定すること",             "is_correct": False, "display_order": 2},
            {"choice_text": "利用者が実際に行う一連の操作フローをエンドツーエンドで確認すること", "is_correct": True,  "display_order": 3},
            {"choice_text": "ソースコードの全分岐を網羅すること",                             "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q69 (MD第67問)
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるオンライン書店の開発チームでは、新機能の設計書に対してウォークスルーを実施することになった。\n\n"
            "ウォークスルーの特徴として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL シラバスでは、レビューの形式として「非公式レビュー」「ウォークスルー」「テクニカルレビュー」「インスペクション」を定義している。"
            "ウォークスルーは作成者が主導し、成果物の内容を参加者に説明しながら進める形式であり、"
            "参加者は理解を深めながら質問・コメント・欠陥指摘を行う。"
            "v4.0 では「新しいアイディアの創出」もウォークスルーの目的のひとつとして追加されている。\n"
            "A: インスペクションの特徴（最も形式的なレビュー）\n"
            "C: 非公式レビューの特徴\n"
            "D: インスペクションの事前準備・会議運営の特徴"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "事前に入口基準・チェックリスト・出口基準を設定し、厳密な手順で実施する最も形式的なレビュー形式である", "is_correct": False, "display_order": 1},
            {"choice_text": "作成者が成果物の内容を参加者に説明しながら進め、参加者が質問・コメント・欠陥指摘を行う形式である",   "is_correct": True,  "display_order": 2},
            {"choice_text": "参加者全員が自由に発言し、記録を残さない最も非公式なレビュー形式である",                           "is_correct": False, "display_order": 3},
            {"choice_text": "レビューアが事前に個別に成果物を確認し、会議では欠陥の発見のみに集中する形式である",               "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # テストマネジメント  追加7問（Q70–Q76）
    # ══════════════════════════════════════════════════════════════

    {   # Q70 (MD第68問)
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行の開発プロジェクトでは、テストマネージャがリスクの識別と評価を行っている。\n\n"
            "「決済処理のバグによる二重引き落とし」というリスクを評価する際に使用する2つの観点として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL シラバスでは、プロダクトリスクの評価は「発生可能性（Likelihood）」と「影響度（Impact）」の2軸で行うとされている。"
            "「決済処理のバグによる二重引き落とし」の場合、"
            "「そのような欠陥が実際に発生する可能性はどれほどか」と「発生した場合に利用者・ビジネスへの影響はどれほど大きいか」を評価することで優先度を決定する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "開発担当者のスキルレベルと開発期間の長さ",     "is_correct": False, "display_order": 1},
            {"choice_text": "欠陥の発生可能性と障害発生時の影響度",         "is_correct": True,  "display_order": 2},
            {"choice_text": "テストケースの件数とテスト環境の数",           "is_correct": False, "display_order": 3},
            {"choice_text": "リリース日と予算の残額",                       "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q71 (MD第69問)
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発プロジェクトでは、テスト担当者が以下の2種類のリスクを識別した。\n\n"
            "- リスクA：「検索機能に欠陥があり、誤った商品が表示される」\n"
            "- リスクB：「テスト担当者が1名退職し、テスト実施工数が不足する」\n\n"
            "リスクの分類として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL シラバスでは、テストに関するリスクを以下のように分類している。\n"
            "プロダクトリスク: テスト対象のシステム・機能に関するリスク。欠陥によって利用者・ビジネスに悪影響を与える可能性。（例: 検索機能の欠陥）\n"
            "プロジェクトリスク: テストプロジェクトの計画・実行・管理に影響するリスク。（例: 人員不足・スケジュール遅延・環境問題）\n"
            "リスクAは「製品の欠陥」に関するプロダクトリスク、リスクBは「プロジェクト遂行上の問題」に関するプロジェクトリスクである。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "リスクAがプロジェクトリスク、リスクBがプロダクトリスク",  "is_correct": False, "display_order": 1},
            {"choice_text": "リスクAがプロダクトリスク、リスクBがプロジェクトリスク",  "is_correct": True,  "display_order": 2},
            {"choice_text": "リスクA・Bともにプロダクトリスク",                        "is_correct": False, "display_order": 3},
            {"choice_text": "リスクA・Bともにプロジェクトリスク",                      "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q72 (MD第70問)
        "category": "テストマネジメント",
        "difficulty": 3,
        "question_text": (
            "あるホテル予約サービスのプロジェクトでは、テスト担当者が3名・テスト期間が2週間という制約がある。\n\n"
            "テストマネージャはすべての機能を均等にテストする計画を立てていたが、プロジェクトオーナーから「最も重要なリスクに集中してほしい」と要望があった。\n\n"
            "この状況でテストマネージャが採用すべきアプローチとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "リスクベースドテストは「リスクレベルに応じてテストの優先度・深度・リソース配分を決定する」アプローチである。"
            "制約のある状況でテスト担当者のリソースを最大限に活かすためには、「発生可能性と影響度が高いリスク」に集中してテストすることが効果的である。"
            "均等なテストは限られたリソースの無駄遣いにつながる可能性があり、期間延長や無理な短縮は現実的でない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト期間を延長してすべての機能を均等にテストする",                                        "is_correct": False, "display_order": 1},
            {"choice_text": "リスクの高い機能を優先してテストリソースを配分するリスクベースドテストを採用する",           "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト担当者を増員せずに全機能のテストを完了させるため、各テストケースの実施時間を短縮する",   "is_correct": False, "display_order": 3},
            {"choice_text": "テストを全て自動化することで2週間以内に全機能をカバーする",                                 "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q73 (MD第71問)
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行のプロジェクトでは、テストマネージャが担当者へのタスク割り当てを行っている。\n\n"
            "タスクの割り当てにあたって考慮すべき事項として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストマネジメントにおけるタスク割り当てでは、各テスト担当者のスキル・経験・得意領域と、"
            "テストタスクの難易度・技術的要件・性質を照合して適切にアサインすることが重要である。"
            "たとえば性能テストには性能分析の経験者、セキュリティテストにはセキュリティの知識を持つ担当者をアサインするなどの判断が求められる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト担当者の現在の作業負荷と稼働状況",                                                       "is_correct": False, "display_order": 1},
            {"choice_text": "テスト担当者のスキル・経験・得意領域と、タスクの難易度・性質の適合性",                           "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト担当者の過去の欠陥発見実績",                                                               "is_correct": False, "display_order": 3},
            {"choice_text": "テスト担当者の業務経験年数",                                                                     "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q74 (MD第72問)
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発プロジェクトでは、テスト担当者が欠陥管理システムに登録した欠陥について、"
            "開発担当者から「仕様通りの動作であり欠陥ではない」という回答が来た。\n\n"
            "この状況への対応として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストで発見した事象が「欠陥か仕様通りか」で意見が分かれた場合、関係者間での事実確認と合意形成が必要となる。"
            "具体的には要求仕様書・設計書を確認し、意図された動作と現在の動作が一致しているかを客観的な資料に基づいて判断する。"
            "それでも解決しない場合はプロジェクトマネージャや要件オーナーも交えて意思決定を行う。"
            "欠陥の一方的なクローズや削除はトレーサビリティの観点から避けるべきである。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "開発担当者の判断に従い、欠陥を即座にクローズする",                                                 "is_correct": False, "display_order": 1},
            {"choice_text": "欠陥を欠陥管理システムから削除する",                                                               "is_correct": False, "display_order": 2},
            {"choice_text": "要求仕様書・設計書・テスト担当者・開発担当者・必要に応じて関係者を交えて事実確認と合意形成を行う",   "is_correct": True,  "display_order": 3},
            {"choice_text": "テストマネージャに報告せずにテスト担当者が独断でクローズする",                                     "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q75 (MD第73問)
        "category": "テストマネジメント",
        "difficulty": 3,
        "question_text": (
            "あるオンライン書店のプロジェクトでは、テストマネージャが以下の欠陥状況を確認した。\n\n"
            "- 重大度高：発見5件・修正済み3件・未解決2件\n"
            "- 重大度中：発見18件・修正済み10件・未解決8件\n"
            "- 重大度低：発見24件・修正済み20件・未解決4件\n\n"
            "リリース3日前という状況で、テストマネージャが最も優先すべき対応はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "リリース直前の欠陥管理では、最も重大なリスクを持つ「重大度高の未解決欠陥」の状況を把握し、"
            "ステークホルダーへ透明性を持って報告・判断を仰ぐことがテストマネージャの役割である。"
            "リリース可否の最終判断はテストマネージャが単独で行うものではなく、プロジェクトオーナー・開発マネージャ等の関係者と合意して決定する。"
            "低重大度の優先は順序が逆であり、無条件延期も独断の判断として不適切である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "低重大度の欠陥4件を優先的に修正させる",                                                               "is_correct": False, "display_order": 1},
            {"choice_text": "重大度高の未解決欠陥2件の修正状況・修正予定日・リリースへの影響をステークホルダーへ報告し、リリース可否の判断を仰ぐ", "is_correct": True,  "display_order": 2},
            {"choice_text": "欠陥が残っているためリリースを無条件で延期する",                                                     "is_correct": False, "display_order": 3},
            {"choice_text": "中重大度の未解決欠陥8件の修正をすべて完了してからリリース可否を判断する",                           "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q76 (MD第74問)
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発プロジェクトでは、アジャイル開発を採用している。\n\n"
            "各スプリントでテスト担当者が注意すべき事項として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "アジャイル開発におけるテストは「各スプリント内でテスト活動を完結させる」ことが基本である。"
            "開発担当者とテスト担当者が協力しながらスプリント内でテスト設計・実施・欠陥修正・確認テストを行い、継続的にフィードバックを提供する。"
            "テストをスプリント後にまとめて実施すると欠陥発見が遅れコストが増大する。"
            "テスト計画も各スプリントの状況に応じて適宜見直される。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストはスプリント終了後にまとめて実施するため、スプリント中は開発を優先する",             "is_correct": False, "display_order": 1},
            {"choice_text": "各スプリント内でテスト設計・実施・欠陥修正・確認まで完了させ、継続的にフィードバックを提供する", "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト計画は最初のスプリントで完全に確定させ、その後は変更しない",                         "is_correct": False, "display_order": 3},
            {"choice_text": "アジャイルではテストドキュメントの作成は不要である",                                       "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # ツール支援  追加5問（Q77–Q81）
    # ══════════════════════════════════════════════════════════════

    {   # Q77 (MD第75問)
        "category": "ツール支援",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行の開発チームでは、テスト自動化ツールの導入を検討している。\n\n"
            "テスト自動化ツール導入に際して、期待できるメリットとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト自動化の主なメリットは「繰り返し実行する回帰テストの実行時間短縮」「人手による実行コストの削減」"
            "「テスト担当者をより価値の高い探索的テストや分析活動に集中させられること」などである。"
            "自動化がすべての欠陥を発見できるわけではなく、テスト担当者が不要になるわけでもない。"
            "また自動化ツールの導入には初期設定・スクリプト開発・保守のコストがかかり、効果が出るまでに時間を要する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト自動化により、すべての欠陥を自動的に発見できる",                                               "is_correct": False, "display_order": 1},
            {"choice_text": "繰り返し実施する回帰テストの実行時間を短縮でき、リソースをより価値の高い活動に集中させられる",       "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト自動化を導入すれば、テスト担当者は不要になる",                                                 "is_correct": False, "display_order": 3},
            {"choice_text": "テスト自動化ツールは導入初日から即座に効果を発揮する",                                               "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q78 (MD第76問)
        "category": "ツール支援",
        "difficulty": 3,
        "question_text": (
            "あるECサイトのテストチームでは、UIテスト自動化を導入して6か月が経過した。\n\n"
            "しかし「UIの変更のたびにテストスクリプトの修正が必要となり、保守コストが高い」という課題が発生している。\n\n"
            "この課題の根本原因として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "UIテスト自動化において「UIの変更に弱い」という問題は、"
            "テストスクリプトがUI要素の具体的な配置や識別子に強く依存した設計になっている場合に典型的に発生する。"
            "ツールの問題や担当者のスキルよりも、スクリプトの設計方針が根本原因であることが多い。"
            "自動化スクリプトは変更の影響を受けにくい構造で設計することが保守コスト低減につながる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト自動化ツールの選定が誤っていた",                                                                 "is_correct": False, "display_order": 1},
            {"choice_text": "テストスクリプトがUI要素のロケータ（ID・クラス名・XPathなど）に直接依存しており、変更への耐性が低い設計になっている", "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト自動化は導入すべきではなかった",                                                                 "is_correct": False, "display_order": 3},
            {"choice_text": "テスト担当者のプログラミングスキルが不足している",                                                   "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q79 (MD第77問)
        "category": "ツール支援",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発チームでは、静的解析ツールをCIパイプラインに組み込んでいる。\n\n"
            "静的解析ツールの主な役割として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "静的解析ツールはソースコードを実行せずに解析するツールであり、"
            "コーディング規約違反・未使用変数・Null参照の可能性・SQLインジェクション等のセキュリティ脆弱性パターン・複雑度の高いコードなどを自動的に検出する。"
            "CIパイプラインに組み込むことで、コードのコミット時に自動的に検査が走り、問題の早期発見につながる。"
            "ソフトウェアの実行・性能測定・ログ監視はいずれも動的なツールの役割である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ソフトウェアを実行して性能を測定する",                                                       "is_correct": False, "display_order": 1},
            {"choice_text": "コードを実行せずに、コーディング規約違反・潜在的なバグ・セキュリティ上の問題などを自動的に検出する", "is_correct": True,  "display_order": 2},
            {"choice_text": "テストケースを自動生成して実行する",                                                         "is_correct": False, "display_order": 3},
            {"choice_text": "本番環境のログをリアルタイムで監視する",                                                     "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q80 (MD第78問)
        "category": "ツール支援",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスでは、テスト管理ツールを導入している。\n\n"
            "テスト管理ツールが提供する機能として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト管理ツールの主な機能は以下の通りである。\n"
            "テストケースの作成・管理・バージョン管理\n"
            "テスト実行の記録と進捗状況の追跡\n"
            "欠陥管理ツールとの連携によるトレーサビリティの確保（要件↔テストケース↔欠陥）\n"
            "テスト進捗・合格率・欠陥状況のレポート生成\n"
            "ソースコードの修正・デプロイ・要求仕様書の生成はテスト管理ツールの機能の範囲外である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ソースコードのバグを自動修正する",                                                                         "is_correct": False, "display_order": 1},
            {"choice_text": "テストケースの管理・テスト実行状況の追跡・欠陥とのトレーサビリティ確保・レポート生成",                   "is_correct": True,  "display_order": 2},
            {"choice_text": "本番環境へのデプロイを自動化する",                                                                         "is_correct": False, "display_order": 3},
            {"choice_text": "要求仕様書を自動的に生成する",                                                                             "is_correct": False, "display_order": 4},
        ],
    },
    {   # Q81 (MD第79問)
        "category": "ツール支援",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームでは、毎月のリリースで500件の回帰テストを手動で実施していたが、テスト自動化ツールの導入を検討している。\n\n"
            "テストリーダーは自動化対象を選定する際、「自動化すべきでないテスト」の基準を整理した。\n\n"
            "自動化に最も向いていないテストとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト自動化に向いているのは「繰り返し実行する」「仕様が安定している」「合否の判定基準が明確で機械的に判断できる」テストである。"
            "探索的テストはテスト担当者の経験・判断・臨機応変な対応が必要であり、"
            "テスト中に得た気づきをもとに次のテスト内容を都度決定するため、自動化になじまない代表的なテストである。"
            "A・B・Dはいずれも自動化に適した条件を示している。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "毎月必ず同じ手順で繰り返し実施する回帰テスト",                           "is_correct": False, "display_order": 1},
            {"choice_text": "仕様が安定しており、合否の判定基準が明確なテスト",                       "is_correct": False, "display_order": 2},
            {"choice_text": "テスト担当者の経験と判断に依存する探索的テスト",                         "is_correct": True,  "display_order": 3},
            {"choice_text": "大量の入力パターンを短時間で確認する必要があるデータ駆動テスト",         "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # テスト技法  追加1問（Q82）※MD第80問・カテゴリ上書き
    # ══════════════════════════════════════════════════════════════

    {   # Q82 (MD第80問) ※MDカテゴリはツール支援だが内容に基づきテスト技法として登録
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームでは、ホワイトボックステストを導入している。\n\n"
            "テスト担当者は「ステートメントカバレッジ」と「ブランチカバレッジ」の関係について整理しようとしている。\n\n"
            "両者の関係として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ブランチカバレッジ（分岐網羅）はステートメントカバレッジ（命令網羅）を包含する関係にある。"
            "すべての分岐（true と false）を通過すれば、必然的にすべての命令も実行されるため、"
            "ブランチカバレッジ100%はステートメントカバレッジ100%を意味する。\n"
            "逆は成立しない。ステートメントカバレッジ100%を達成しても、if 文の false 側（else ブランチ）が未実行のままになる場合があり、"
            "ブランチカバレッジは100%にならないことがある。\n"
            "このためブランチカバレッジはステートメントカバレッジより強い（より厳しい）カバレッジ基準であり、"
            "ホワイトボックステストでは一般的にブランチカバレッジの達成を目指すことが推奨される。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ステートメントカバレッジ100%を達成すれば、自動的にブランチカバレッジも100%達成される",   "is_correct": False, "display_order": 1},
            {"choice_text": "ブランチカバレッジ100%を達成すれば、自動的にステートメントカバレッジも100%達成される", "is_correct": True,  "display_order": 2},
            {"choice_text": "ステートメントカバレッジとブランチカバレッジは独立しており、どちらを先に達成してもよい",  "is_correct": False, "display_order": 3},
            {"choice_text": "ブランチカバレッジはステートメントカバレッジより達成が容易である",                      "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # 追加問題（MD第81〜120問）40問
    # ══════════════════════════════════════════════════════════════

    # --- テストの基礎 7問 ---

    {   # MD第81問
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発チームでは、品質に関する議論が行われた。\n\n"
            "チームメンバーから「品質とはバグがないことだ」という意見が出た。\n\n"
            "JSTQB FL の観点から、この意見への最も適切な補足はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL では品質を「製品・コンポーネント・プロセスが、規定された要件および暗黙の期待を"
            "満足させる度合い」として定義している。バグがないことは品質の一側面に過ぎず、"
            "ユーザーが使いにくいシステムや、機能は動作するが性能が低いシステムは品質が高いとは言えない。"
            "品質には機能適合性・性能効率性・使用性・信頼性・セキュリティなど複数の特性が含まれる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "バグがないことは品質の必要条件であり、それだけで品質が高いとは言えない。品質とはステークホルダーの明示的・暗黙的なニーズを満足させる度合いである", "is_correct": True,  "display_order": 1},
            {"choice_text": "バグがなければ品質は完全に保証されるため、テストでバグが出なければリリースしてよい",                                                          "is_correct": False, "display_order": 2},
            {"choice_text": "品質はコードの行数に比例するため、コードが少ないほど品質が高い",                                                                             "is_correct": False, "display_order": 3},
            {"choice_text": "品質はテスト担当者が評価するものであり、ユーザーの意見は品質の定義に含まれない",                                                            "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第82問
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行では、振込機能のリリース後に「画面上の金額表示は正しいが、"
            "実際の振込処理では小数点以下の端数が切り捨てられず、意図しない金額が送金される」"
            "という障害が報告された。\n\n"
            "この事象における「根本原因」として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "根本原因分析では「誤り（人間のミス）→欠陥（コードの不備）→障害（実行時の誤動作）」"
            "の連鎖を正確に把握することが重要である。"
            "今回の根本原因は「小数点以下の計算ロジックの実装に誤りがあった」という欠陥にある。"
            "「意図しない金額が送金された」は障害（結果）であり、"
            "「テスト担当者が確認しなかった」はプロセスの問題であって根本原因ではない。"
            "根本原因を正確に特定することで、再発防止策を適切に設計できる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト担当者が端数処理を確認しなかったこと",                  "is_correct": False, "display_order": 1},
            {"choice_text": "小数点以下の計算ロジックの実装に誤りがあったこと",             "is_correct": True,  "display_order": 2},
            {"choice_text": "振込ボタンを押したときに意図しない金額が送金されたこと",        "is_correct": False, "display_order": 3},
            {"choice_text": "要求仕様書に端数処理の仕様が記載されていたこと",               "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第83問
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発プロジェクトでは、テスト担当者が「シフトレフト」の考え方を"
            "導入しようとしている。\n\n"
            "シフトレフトの考え方として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "シフトレフトとはテスト活動をソフトウェア開発ライフサイクルの早い段階（左側）へ"
            "シフトさせるという考え方である。"
            "従来のテストは実装完了後に実施されることが多かったが、"
            "シフトレフトでは要件定義・設計段階からテスト担当者が関与し、"
            "仕様のレビューや早期の欠陥発見を行う。"
            "欠陥は発見が遅くなるほど修正コストが高くなるため、"
            "早期の関与が品質とコスト両面で効果的である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト活動を早期に開始することで、実装工程を省略してリリースまでの期間を短縮する考え方",                                          "is_correct": False, "display_order": 1},
            {"choice_text": "テスト活動をできるだけ早い段階から開始し、要件定義・設計段階から品質に関与することで欠陥の早期発見・修正コストの低減を図る", "is_correct": True,  "display_order": 2},
            {"choice_text": "テストはすべて自動化し、手動テストを廃止することでシフトレフトを実現する",                                                  "is_correct": False, "display_order": 3},
            {"choice_text": "シフトレフトとはリリーススケジュールを前倒しにするための手法であり、テストとは関係がない",                                      "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第84問
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるオンライン書店では、システムテストが完了し本番リリースを行った後に、"
            "別の機能をメンテナンスする予定がある。\n\n"
            "メンテナンステストとして最も適切な説明はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "メンテナンステストは、既存システムに対して「機能追加・変更・バグ修正・環境移行"
            "（OSやミドルウェアのバージョンアップ等）」が行われた後に実施するテストである。"
            "確認すべき内容は「変更が意図通りに動作すること（確認テスト）」と"
            "「変更によって他の機能に悪影響が出ていないこと（回帰テスト）」の2点である。"
            "本番環境の監視は運用活動であり、テストとは区別される。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "本番環境の稼働監視を行い、障害発生時に対応するテスト",                                                                                                  "is_correct": False, "display_order": 1},
            {"choice_text": "既存システムへの変更・修正・移行後に、変更が意図通りに機能すること、および変更によって影響を受けた他の機能に問題がないことを確認するテスト", "is_correct": True,  "display_order": 2},
            {"choice_text": "開発段階で実施する単体テストと結合テストを合わせたテスト",                                                                                              "is_correct": False, "display_order": 3},
            {"choice_text": "ユーザーが本番環境で日常業務を通じて行うテスト",                                                                                                        "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第85問
        "category": "テストの基礎",
        "difficulty": 3,
        "question_text": (
            "あるホテル予約サービスでは、ソフトウェア開発にVモデルを採用している。\n\n"
            "Vモデルにおけるテストレベルと開発フェーズの対応として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "Vモデルでは左側の開発フェーズと右側のテストレベルが対応している。"
            "各テストレベルのテストベース（根拠となる成果物）は以下の通りである。\n"
            "単体テスト: コンポーネント設計・詳細設計。\n"
            "結合テスト: アーキテクチャ設計・システム設計。\n"
            "システムテスト: 要求仕様・機能仕様。\n"
            "受入テスト: ビジネスニーズ・ユーザー要求。\n"
            "この対応関係を把握することで、各テストレベルで「何を根拠に何を確認するか」が明確になる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "単体テストは要求定義に、システムテストはアーキテクチャ設計に対応する",                                                                          "is_correct": False, "display_order": 1},
            {"choice_text": "単体テストはコンポーネント設計に、結合テストはシステム設計に、システムテストは要求仕様に、受入テストはビジネスニーズに対応する", "is_correct": True,  "display_order": 2},
            {"choice_text": "すべてのテストレベルは要求定義のみを根拠として実施する",                                                                                    "is_correct": False, "display_order": 3},
            {"choice_text": "Vモデルではテストは実装完了後にまとめて実施するため、各テストレベルと開発フェーズの対応は存在しない",                                       "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第86問
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームでは、テスト担当者に求められるスキルについて議論していた。\n\n"
            "JSTQB FL の観点からテスト担当者に求められるスキルとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL では、優れたテスト担当者に求められるスキルとして以下を挙げている。"
            "テスト技法・ツールに関する知識、ドメイン（業務）知識、分析力・批判的思考力、"
            "コミュニケーション能力（開発担当者・ステークホルダーとの連携）、"
            "技術的な好奇心、メトリクスの理解、リスク志向の思考などである。"
            "プログラミングスキルは有用だが必須ではなく、"
            "コミュニケーション能力は欠陥報告・関係者との調整において不可欠である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ドメイン知識と分析力が中核であり、テスト技法やツールの知識は実務を通じて自然に身につくため重視されない",                "is_correct": False, "display_order": 1},
            {"choice_text": "テスト技法の知識・分析力・批判的思考・コミュニケーション能力・技術的な好奇心など多面的なスキルが求められる",           "is_correct": True,  "display_order": 2},
            {"choice_text": "批判的思考と欠陥指摘の徹底が最優先であり、開発担当者との合意形成や調整はテスト担当者の責務には含まれない",            "is_correct": False, "display_order": 3},
            {"choice_text": "テスト技法の知識が備わっていれば十分であり、メトリクスの理解やリスク志向は管理者だけが持つべきスキルである",           "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第87問
        "category": "テストの基礎",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発プロジェクトで、"
            "品質保証（QA）とテストの役割について議論が起きた。\n\n"
            "QAとテストの関係として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "品質保証（QA）はプロセス全体を対象とした活動であり、"
            "適切なプロセスを実施することで品質を作り込むことを目的とする。"
            "テストはQAの中の一活動であり、実際にソフトウェアを動作させて"
            "（または静的に評価して）欠陥を発見することに特化している。"
            "QAはテストに限らず、要件管理・設計レビュー・プロセス改善・メトリクス管理"
            "など広範囲の活動を含む。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "QAとテストは同じ活動であり、区別する必要はない",                                                                          "is_correct": False, "display_order": 1},
            {"choice_text": "テストはQAの一部であり、QAはプロセス全体の品質改善を目的とした活動である。テストは欠陥を発見することに特化した活動である", "is_correct": True,  "display_order": 2},
            {"choice_text": "QAはテストの一部であり、テストが上位概念である",                                                                          "is_correct": False, "display_order": 3},
            {"choice_text": "QAはリリース後の運用フェーズでのみ実施する活動である",                                                                    "is_correct": False, "display_order": 4},
        ],
    },

    # --- テスト活動とプロセス 7問 ---

    {   # MD第88問
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行の開発プロジェクトで、テスト担当者がテスト実装フェーズの作業を行っている。\n\n"
            "テスト実装フェーズの作業として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストプロセスの活動は以下のように区別される。\n"
            "テスト分析: テストベースを分析してテスト条件を識別する。\n"
            "テスト設計: テスト条件をもとにテストケースと期待結果を定義する。\n"
            "テスト実装: テストケースをもとにテスト手順書・テストスクリプト・テストデータを準備し、テスト環境を構築・検証する。\n"
            "テスト実行: テストを実行し、実際の結果と期待結果を比較する。\n"
            "テスト完了: 成果物の整理・振り返り・レポート作成を行う。\n"
            "テスト実装は「実行する準備を整える」フェーズであり、実際の実行はその後のテスト実行フェーズで行う。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "要求仕様書を読んでテスト条件を識別する",                                                              "is_correct": False, "display_order": 1},
            {"choice_text": "テストケースをもとに、テスト手順書・テストスクリプト・テストデータを準備し、テスト環境を構築する", "is_correct": True,  "display_order": 2},
            {"choice_text": "実際にテストを実行し、実際の結果と期待結果を比較する",                                               "is_correct": False, "display_order": 3},
            {"choice_text": "テスト実行後に欠陥状況をまとめてステークホルダーへ報告する",                                         "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第89問
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるECサイトのプロジェクトで、テスト担当者が以下の終了基準（エグジットクライテリア）を確認した。\n\n"
            "・重大度高欠陥：0件\n"
            "・要件カバレッジ：95%以上\n"
            "・テスト実行率：98%以上\n\n"
            "この終了基準の目的として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "終了基準（エグジットクライテリア）は「このテストフェーズを終了してよい、"
            "または次のフェーズへ進んでよい状態」を客観的に定義するものである。"
            "主観的な判断ではなく数値・条件で定義することで、"
            "ステークホルダー間の合意形成を容易にし、早期終了や無限延長を防ぐ役割を果たす。"
            "開始基準（エントリークライテリア）と組み合わせることで、"
            "テストフェーズの入口と出口が明確になる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト担当者が好きなタイミングでテストを終了できるようにするためのガイドライン", "is_correct": False, "display_order": 1},
            {"choice_text": "次のテストフェーズへの移行またはリリース判断をするための客観的な判断基準",       "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト担当者のパフォーマンスを評価するための指標",                               "is_correct": False, "display_order": 3},
            {"choice_text": "テストケースの設計品質を測定するための基準",                                     "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第90問
        "category": "テスト活動とプロセス",
        "difficulty": 3,
        "question_text": (
            "あるホテル予約サービスの開発プロジェクトで、テストマネージャがテスト工数を見積もっている。\n\n"
            "見積もりの根拠として以下の情報を収集した。\n\n"
            "・前回の類似プロジェクトの実績：テストケース200件、総実施工数80時間\n"
            "・今回のプロジェクト：テストケース350件（前回より複雑な仕様を含む）\n\n"
            "テストマネージャは「類似プロジェクトの実績をベースにするが、複雑さを考慮して係数1.3を乗じる」"
            "という方針にした。\n\n"
            "今回の見積もり工数として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "計算は以下の通り。\n"
            "前回の1件あたり工数：80時間 ÷ 200件 = 0.4時間/件。\n"
            "複雑さ係数を考慮した1件あたり工数：0.4 × 1.3 = 0.52時間/件。\n"
            "今回の見積もり：350件 × 0.52 = 182時間。\n"
            "このような「過去の実績を基準に係数で調整する」見積もり手法は"
            "アナロジーベースの見積もりと呼ばれ、類似プロジェクトの実績データがある場合に有効である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "約140時間", "is_correct": False, "display_order": 1},
            {"choice_text": "約182時間", "is_correct": True,  "display_order": 2},
            {"choice_text": "約200時間", "is_correct": False, "display_order": 3},
            {"choice_text": "約230時間", "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第91問
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるオンライン書店の開発チームでは、アジャイル開発を採用しており、"
            "継続的インテグレーション（CI）を導入している。\n\n"
            "CIとテストの関係として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "継続的インテグレーション（CI）は、開発担当者がコードをリポジトリに統合するたびに"
            "自動的にビルド・テストを実行する手法である。"
            "CIパイプラインに単体テスト・統合テスト・静的解析などを組み込むことで、"
            "変更による欠陥を早期に検出でき、シフトレフトの実践につながる。"
            "DevOps の観点では CI/CD（継続的デリバリー）と組み合わせることで"
            "リリースサイクルを短縮しながら品質を維持できる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "CIパイプラインにはビルドと静的解析のみを組み込み、テストの実行はリリース前の専用フェーズに集約すべきである",        "is_correct": False, "display_order": 1},
            {"choice_text": "CIパイプラインにテストを組み込み、コードの変更のたびに自動的にテストを実行することで、欠陥を早期かつ継続的に検出できる", "is_correct": True,  "display_order": 2},
            {"choice_text": "CIパイプラインには単体テストのみを組み込むべきであり、結合テスト以上はCDパイプラインで実施する",                    "is_correct": False, "display_order": 3},
            {"choice_text": "CIを導入すると継続的にテストが実行されるため、手動によるシステムテストや受入テストは省略できる",                    "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第92問
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発プロジェクトで、"
            "テスト担当者が受入テストの種類について整理している。\n\n"
            "ユーザー受入テスト（UAT）の目的として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "受入テストにはいくつかの種類があり、「誰が・何を確認するか」で区別できることが重要である。\n"
            "ユーザー受入テスト（UAT）: 想定される利用者が、実際の業務シナリオに沿ってシステムを使用し業務目的を達成できることを確認する。\n"
            "運用受入テスト: 運用担当者がシステムの管理・保守ができることを確認する。\n"
            "契約受入テスト: 契約で定めた基準への適合を確認する。\n"
            "規制受入テスト: 法律・規制・業界標準への適合を確認する。\n"
            "選択肢Aは運用受入テスト、Cは契約受入テスト、Dは規制受入テストの説明である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "システムの運用担当者が、バックアップ・復旧・保守などの運用手順を実行できることを確認する",     "is_correct": False, "display_order": 1},
            {"choice_text": "想定される利用者が、実際の業務シナリオに沿ってシステムを使用し業務目的を達成できることを確認する", "is_correct": True,  "display_order": 2},
            {"choice_text": "発注者と開発者が、契約で合意した受入基準に成果物が適合していることを確認する",                 "is_correct": False, "display_order": 3},
            {"choice_text": "システムが、対象業界の法令・規制・標準に適合していることを確認する",                           "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第93問
        "category": "テスト活動とプロセス",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行のプロジェクトでは、テスト担当者が欠陥レポートを作成する際の"
            "優先度と重大度の設定について学んでいる。\n\n"
            "重大度と優先度の関係として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "重大度（Severity）はシステムへの技術的・機能的な影響度を示し、"
            "優先度（Priority）はビジネス上の緊急性・修正の順番を示す。この2つは独立した属性である。\n"
            "重大度高・優先度低の例: ほとんど使われない機能でシステムがクラッシュするが、リリース後でも対応可能。\n"
            "重大度低・優先度高の例: ロゴが微妙にずれているだけだが、翌日に重要な発表があるため今すぐ直す必要がある。\n"
            "この区別を理解することで、限られた修正リソースを適切に配分できる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "重大度が高い欠陥は必ず優先度も高くなる",                                                                                          "is_correct": False, "display_order": 1},
            {"choice_text": "重大度と優先度は独立した属性であり、重大度が高くても優先度が低い場合や、重大度が低くても優先度が高い場合がある", "is_correct": True,  "display_order": 2},
            {"choice_text": "優先度はテスト担当者が決定し、重大度はプロジェクトマネージャが決定する",                                                         "is_correct": False, "display_order": 3},
            {"choice_text": "重大度は技術的な影響度を示し、優先度も同じ技術的な観点で決まる",                                                                 "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第94問
        "category": "テスト活動とプロセス",
        "difficulty": 3,
        "question_text": (
            "あるECサイトのプロジェクトでは、テスト実行中にテスト環境が突然利用不能になり、"
            "2日間テストが実施できなかった。\n\n"
            "テストマネージャが取るべき対応として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストモニタリングとコントロールの活動では、計画から逸脱が発生した場合に"
            "適切な対応策を検討し、ステークホルダーへ透明性を持って報告することが求められる。"
            "環境障害はプロジェクトリスクの一例であり、発生した場合は"
            "「スケジュールへの影響」「品質リスク」「代替手段の有無」を整理して"
            "報告・合意することが優先される。"
            "報告なしの再開や独断での目標変更はステークホルダーの信頼を損なうリスクがある。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト担当者に残業させてスケジュール遅延を取り戻す",                                                                          "is_correct": False, "display_order": 1},
            {"choice_text": "テストの中断・遅延・リスクをステークホルダーへ報告し、スケジュール再調整・優先度変更・代替手段の検討を関係者と合意する", "is_correct": True,  "display_order": 2},
            {"choice_text": "環境が復旧するまでテスト活動を完全に停止し、復旧後に何も報告せず再開する",                                                    "is_correct": False, "display_order": 3},
            {"choice_text": "テスト実行率の目標を下げてリリースを予定通りに実施する",                                                                      "is_correct": False, "display_order": 4},
        ],
    },

    # --- 静的テスト 6問 ---

    {   # MD第95問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行の開発プロジェクトで、要求仕様書のレビューを実施した結果、"
            "以下の問題が発見された。\n\n"
            "・「振込手数料は規定に従い計算すること」（規定の参照先が不明）\n"
            "・同一の振込条件が異なる箇所に矛盾した記述で存在する\n"
            "・キャンセル後の手数料返金ルールが記載されていない\n\n"
            "これらの指摘を静的テストの効果として整理した場合、最も適切な説明はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "静的テストはソフトウェアを実行せずに成果物を検査することで欠陥を発見する活動である。"
            "要求仕様書のレビューで発見できる典型的な欠陥として"
            "「あいまいな表現」「矛盾した記述」「記載漏れ」「参照先不明」などがある。"
            "これらを実装前に発見・修正することで、"
            "実装コスト・テストコスト・リリース後の修正コストを大幅に削減できる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "静的テストはソフトウェアを実行するため、これらの問題は動的テストで発見されたものである",         "is_correct": False, "display_order": 1},
            {"choice_text": "静的テストによりソフトウェアを実行する前に、あいまいさ・矛盾・記載漏れといった欠陥を発見できた", "is_correct": True,  "display_order": 2},
            {"choice_text": "これらの問題は実装後のシステムテストで発見すべきものであり、静的テストの対象ではない",           "is_correct": False, "display_order": 3},
            {"choice_text": "静的テストは品質向上に寄与しないため、実施する必要はない",                                        "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第96問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームで、コードレビューを実施している。\n\n"
            "コードレビューで発見できる欠陥の種類として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "コードレビュー（静的テスト）で発見できる欠陥は、コードを読むことで識別できるものに限られる。"
            "代表的な例として、コーディング規約違反・変数の初期化漏れ・未使用変数・"
            "複雑すぎるロジック・コピー&ペーストミス・"
            "セキュリティ脆弱性パターン（SQLインジェクション・クロスサイトスクリプティングなど）がある。"
            "一方、実際にシステムを動作させないと発見できない"
            "性能問題・特定操作シーケンスでの障害などは動的テストで確認する必要がある。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "エンドユーザーが操作したときにのみ発生する障害",                                                                    "is_correct": False, "display_order": 1},
            {"choice_text": "コーディング規約違反・変数の未初期化・冗長なロジック・セキュリティ上の脆弱性パターンなど、コードを実行せずに確認できる問題", "is_correct": True,  "display_order": 2},
            {"choice_text": "本番環境の負荷状況でのみ発生する性能問題",                                                                          "is_correct": False, "display_order": 3},
            {"choice_text": "ユーザーが誤った操作をした場合にのみ発生する例外処理の問題",                                                        "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第97問
        "category": "静的テスト",
        "difficulty": 3,
        "question_text": (
            "あるフードデリバリーサービスのプロジェクトで、"
            "設計書レビューの形式を検討している。\n\n"
            "インスペクションとウォークスルーの違いとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL では4つのレビュー形式を定義している。\n"
            "非公式レビュー（形式度:最低）: 記録なし・自由な形式で実施する。\n"
            "ウォークスルー（形式度:低〜中）: 作成者が進行し、説明しながら進行・新アイデア創出も目的とする。\n"
            "テクニカルレビュー（形式度:中）: モデレータが進行し、技術的観点から欠陥を発見する。\n"
            "インスペクション（形式度:最高）: モデレータが進行し、チェックリスト・入口/出口基準・メトリクスを使用する。\n"
            "インスペクションは最も形式的で体系的なレビュー形式であり、大きな成果物や高リスク成果物に適している。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "インスペクションもウォークスルーも、作成者が進行を主導する点で同じである",                                                                      "is_correct": False, "display_order": 1},
            {"choice_text": "インスペクションは最も形式的なレビューで、モデレータが進行しチェックリスト・入口/出口基準を使用する。ウォークスルーは作成者が進行し、より柔軟な形式で実施する", "is_correct": True,  "display_order": 2},
            {"choice_text": "ウォークスルーはインスペクションより形式的であり、厳密な手順が必要である",                                                                      "is_correct": False, "display_order": 3},
            {"choice_text": "インスペクションとウォークスルーはどちらも記録を残さない非公式なレビューである",                                                                "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第98問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスの開発チームで、静的解析ツールをCIパイプラインに導入した。\n\n"
            "導入後に「ツールが多数の警告を出力するが、実際の問題かどうか判断が難しい」"
            "という状況が発生した。\n\n"
            "この状況を表す概念として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "静的解析ツールが実際には問題でないコードに対して警告を出すことを"
            "「誤検知（フォールスポジティブ）」という。"
            "誤検知が多すぎるとチームが警告を無視するようになり（アラート疲れ）、"
            "本当に重要な問題を見落とすリスクがある。"
            "対策としてはルール設定の調整・チームに合ったプロファイルの選択・"
            "段階的な導入（まず重大なルールのみ有効化）などが有効である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストの弱化",           "is_correct": False, "display_order": 1},
            {"choice_text": "誤検知（フォールスポジティブ）", "is_correct": True,  "display_order": 2},
            {"choice_text": "欠陥クラスタリング",     "is_correct": False, "display_order": 3},
            {"choice_text": "テスト独立性の欠如",     "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第99問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームで、テクニカルレビューを実施することになった。\n\n"
            "テクニカルレビューの主な目的として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テクニカルレビューは技術的な観点から成果物を評価するレビュー形式であり、"
            "アーキテクチャの妥当性・設計の整合性・技術的リスク・セキュリティ上の問題などを主に確認する。"
            "参加者は開発担当者・テストエンジニア・アーキテクトなどの技術的な専門家である。"
            "ウォークスルー（作成者が説明して共有）や"
            "インスペクション（最も形式的）とは目的・進行方法が異なる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "作成者がチームメンバーに成果物の内容を説明して理解を共有すること",                 "is_correct": False, "display_order": 1},
            {"choice_text": "技術的観点から成果物の欠陥を発見し、技術的な品質を評価・改善すること",             "is_correct": True,  "display_order": 2},
            {"choice_text": "プロジェクトマネージャがレビューの進行を管理し、指摘事項を記録すること",           "is_correct": False, "display_order": 3},
            {"choice_text": "ユーザーが成果物を確認して受入可否を判断すること",                               "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第100問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行の開発プロジェクトで、レビュー会議が終了した後に、"
            "レビューアが指摘した問題を作成者が修正した。\n\n"
            "修正後に実施すべき活動として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "形式的なレビュー（インスペクション・テクニカルレビュー等）では、"
            "レビュー会議後に指摘事項が適切に修正されたかを確認する「フォローアップ」活動が含まれる。"
            "フォローアップはモデレータまたは担当レビューアが修正内容を確認し、"
            "指摘が解消されたことを確認したうえでレビューを完了とする。"
            "修正が軽微であれば全体の再レビューは不要だが、"
            "大幅な修正が必要な場合は再レビューを実施することもある。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "修正内容はレビューアには確認させず、作成者の判断で完了とする",                                         "is_correct": False, "display_order": 1},
            {"choice_text": "修正内容が指摘事項を適切に解決しているかをレビューアまたはモデレータが確認する（フォローアップ）", "is_correct": True,  "display_order": 2},
            {"choice_text": "修正後は必ず最初からレビューを全て再実施する",                                                         "is_correct": False, "display_order": 3},
            {"choice_text": "修正内容の確認は次のプロジェクトで実施する",                                                           "is_correct": False, "display_order": 4},
        ],
    },

    # --- テスト技法 7問 ---

    {   # MD第101問
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるECサイトでは、会員ランクに応じてポイント還元率が異なる。仕様は以下の通り。\n\n"
            "・購入金額0円〜9,999円：1%還元\n"
            "・購入金額10,000円〜29,999円：3%還元\n"
            "・購入金額30,000円以上：5%還元\n\n"
            "同値分割法と境界値分析を組み合わせてテストケースを設計する場合、"
            "テストすべき値の組み合わせとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "同値分割法と境界値分析を組み合わせる場合、"
            "「各クラスの代表値（同値分割）」と「各クラスの境界付近の値（境界値分析）」の"
            "両方をテストすることが効果的である。"
            "この仕様では3つの有効クラスが存在し、境界は「0〜9,999」「10,000〜29,999」「30,000〜」"
            "の切り替わり点にある。"
            "境界値（9,999・10,000、29,999・30,000）と無効クラス（負の値、非数値）も"
            "あわせてテストすることで、条件分岐の誤りを効率的に発見できる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "5,000円・15,000円・35,000円（各クラスの中央値のみ）",                                            "is_correct": False, "display_order": 1},
            {"choice_text": "0円・9,999円・10,000円・29,999円・30,000円・30,001円（境界値）および各クラスの代表値", "is_correct": True,  "display_order": 2},
            {"choice_text": "10,000円・30,000円のみ（切り替わり点のみ）",                                                     "is_correct": False, "display_order": 3},
            {"choice_text": "1円・2円・3円（最小値付近のみ）",                                                                "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第102問
        "category": "テスト技法",
        "difficulty": 3,
        "question_text": (
            "あるネット銀行では、ATMの操作フローを状態遷移図で管理している。\n\n"
            "状態：待機中・カード挿入済・PIN入力済・取引選択中・処理中・レシート発行中\n\n"
            "状態遷移テストで「全状態カバレッジ」を達成するために必要な条件として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL v4.0 では状態遷移テストのカバレッジ基準として以下の3つを定義している。\n"
            "全状態カバレッジ: すべての状態を少なくとも1回経由する。\n"
            "有効遷移カバレッジ: すべての有効な遷移を少なくとも1回実行する。\n"
            "全遷移カバレッジ: すべての有効な遷移を実行し、かつすべての無効な遷移について"
            "実行を試みて拒否されることを確認する。\n"
            "全状態カバレッジは最も弱い（達成が容易な）カバレッジ基準であり、全状態を経由するだけでよい。"
            "選択肢Aは有効遷移カバレッジ、Cは全遷移カバレッジの説明である。"
            "なお全遷移カバレッジでは、無効な遷移は「実行を試みて拒否されることを確認する」点が重要であり、"
            "1回のテストで試す無効遷移は1つに絞ることでフォールトマスキングを避けられる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "すべての状態遷移（遷移の組み合わせ）を少なくとも1回実行する",           "is_correct": False, "display_order": 1},
            {"choice_text": "すべての状態を少なくとも1回経由するテストシナリオを設計する",           "is_correct": True,  "display_order": 2},
            {"choice_text": "無効な遷移（発生してはいけない遷移）もすべてテストする",               "is_correct": False, "display_order": 3},
            {"choice_text": "すべての状態からすべての状態への遷移をテストする",                     "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第103問
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスでは、注文の優先度を以下の条件で決定している。\n\n"
            "・プレミアム会員 かつ 雨天 かつ 夜間：最優先\n"
            "・プレミアム会員 かつ 雨天 かつ 日中：優先\n"
            "・プレミアム会員 かつ 晴天：通常\n"
            "・一般会員：通常\n\n"
            "デシジョンテーブルテストを適用する際、最初に行うべき作業として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "デシジョンテーブルテストでは、まず「条件（Condition）」と「アクション（Action）」を"
            "整理してデシジョンテーブルを作成することが出発点となる。"
            "条件は「会員種別」「天候」「時間帯」の3つであり、"
            "それぞれの組み合わせとそれに対応するアクション（優先度）を表にまとめる。"
            "テーブルを作成することで、仕様に記載されていない組み合わせ（テスト漏れ候補）や"
            "矛盾を発見しやすくなる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト環境を構築する",                                                                           "is_correct": False, "display_order": 1},
            {"choice_text": "条件（会員種別・天候・時間帯）とアクション（優先度）を整理し、デシジョンテーブルを作成する", "is_correct": True,  "display_order": 2},
            {"choice_text": "実際に注文してテストケースを実行する",                                                           "is_correct": False, "display_order": 3},
            {"choice_text": "ソースコードの条件分岐を読んで分岐数を確認する",                                                 "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第104問
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるオンライン書店では、テスト担当者が探索的テストを実施している。\n\n"
            "探索的テストの特徴として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "探索的テストは「テスト設計・実行・学習を同時並行で行う」経験ベースのテスト技法である。"
            "テスト担当者はテスト中に得た情報・気づき・直感をもとに"
            "次のテスト方向を動的に決定する。"
            "事前にスクリプトを用意せず、担当者の知識・経験・批判的思考を活用する点が特徴である。"
            "仕様が不明確な新機能・欠陥が潜みやすい複雑な領域・"
            "スクリプトテストでは見つけにくい問題の発見に特に有効である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "事前に全テストケースを定義してから実行する、スクリプトベースのテスト手法である",                                   "is_correct": False, "display_order": 1},
            {"choice_text": "テスト設計・実行・学習を同時並行で行い、テスト中に得た知見をもとに次のテストを動的に決定する手法である", "is_correct": True,  "display_order": 2},
            {"choice_text": "自動化ツールを使ってランダムに入力値を生成してテストする手法である",                                             "is_correct": False, "display_order": 3},
            {"choice_text": "仕様書の網羅率を100%にすることを目的として実施するテスト手法である",                                           "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第105問
        "category": "テスト技法",
        "difficulty": 3,
        "question_text": (
            "あるネット銀行のシステムで、以下の条件が存在する。\n\n"
            "・条件X：残高が1万円以上\n"
            "・条件Y：振込先が登録済み\n"
            "・条件Z：1日の振込上限内\n\n"
            "テスト担当者がデシジョンテーブルを作成し、すべての条件の組み合わせを網羅した。\n\n"
            "この3条件（各Yes/No）について、組み合わせをすべて列挙したデシジョンテーブルの"
            "全ルール数として正しいものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "3つの二値条件（各Yes/No）の組み合わせは 2³ = 8通り存在するため、"
            "すべての組み合わせを列挙した完全なデシジョンテーブルの全ルール数は8である。"
            "デシジョンテーブルの全ルール数は条件数で決まり、条件が n 個あれば 2ⁿ となる。"
            "条件が増えるほどルール数が指数的に増加するため、実務では"
            "「あり得ない組み合わせ」や「結果に影響しない条件（ドントケア）」を整理して"
            "ルールを圧縮することが多い。"
            "なお、このうち実際に「振込可能」となるのは通常X・Y・ZすべてがYesの1ルールのみだが、"
            "本問が問うているのは全ルール数である点に注意。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "1", "is_correct": False, "display_order": 1},
            {"choice_text": "3", "is_correct": False, "display_order": 2},
            {"choice_text": "7", "is_correct": False, "display_order": 3},
            {"choice_text": "8", "is_correct": True,  "display_order": 4},
        ],
    },

    {   # MD第106問
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるECサイトのテスト担当者は、過去に「在庫が0件の商品をカートに追加できてしまう」"
            "欠陥が発生したことを知っていた。\n\n"
            "このためテスト担当者は、在庫0件・在庫1件・在庫上限値の各ケースで"
            "カートへの追加をテストする計画を立てた。\n\n"
            "このテストアプローチで活用している技法として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "エラー推測は「過去の欠陥情報・経験・直感」をもとに"
            "欠陥が潜みやすい箇所を推測し、テストケースを設計する経験ベースの技法である。"
            "「過去に在庫0件で問題が発生した」という実績をもとに、"
            "在庫境界値付近を重点的にテストする計画はエラー推測の典型的な適用例である。"
            "なお「在庫0件・1件・上限値」というテスト値自体は境界値分析の概念も含んでいるが、"
            "「過去の欠陥情報を根拠に設計した」という点でエラー推測として分類される。"
            "技法の分類はテストケースに使用した値ではなく、"
            "テストケースを導出した動機・根拠で判断する点が重要である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "同値分割法",               "is_correct": False, "display_order": 1},
            {"choice_text": "デシジョンテーブルテスト", "is_correct": False, "display_order": 2},
            {"choice_text": "エラー推測",               "is_correct": True,  "display_order": 3},
            {"choice_text": "ユースケーステスト",       "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第107問
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスでは、予約変更フローに複数の状態が存在する。\n\n"
            "「有効遷移カバレッジ（0スイッチカバレッジ）」を達成するために必要なこととして"
            "最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL v4.0 の状態遷移テストのカバレッジ基準において"
            "「有効遷移カバレッジ（0スイッチカバレッジとも呼ばれる）」は、"
            "すべての有効な遷移を少なくとも1回実行することを要件とする。"
            "全状態カバレッジより強く、全遷移カバレッジより弱い中間的な基準であり、"
            "v4.0では最も広く使われるカバレッジ基準とされている。"
            "なお全遷移カバレッジは「有効遷移をすべて実行し、"
            "無効遷移については実行を試みて拒否されることを確認する」基準である。"
            "選択肢Dは1スイッチカバレッジ（連続する2遷移のペアをすべてカバー）の説明である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "すべての状態を1回ずつ経由すればよい",                                              "is_correct": False, "display_order": 1},
            {"choice_text": "すべての有効な遷移（正常に発生する状態の変化）を少なくとも1回実行する",           "is_correct": True,  "display_order": 2},
            {"choice_text": "有効な遷移に加えて、無効な遷移（発生してはいけない遷移）もすべてテストする",       "is_correct": False, "display_order": 3},
            {"choice_text": "2つの遷移を連続して実行するシーケンスをすべてテストする",                         "is_correct": False, "display_order": 4},
        ],
    },

    # --- テストマネジメント 7問 ---

    {   # MD第108問
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発プロジェクトでは、テストマネージャが以下のテストメトリクスを収集している。\n\n"
            "・テストケース実行率：160/200件 = 80%\n"
            "・テストケース合格率：145/160件 = 90.6%\n"
            "・未解決欠陥数：12件（重大度高3件・中6件・低3件）\n"
            "・欠陥検出率（全欠陥中テストで発見した割合）：85%\n\n"
            "「テストの進捗を把握する」目的に最も適したメトリクスはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "各メトリクスの用途は以下の通りである。\n"
            "テストケース実行率: 計画に対してどれだけテストが進んでいるか（進捗把握）。\n"
            "テストケース合格率: 実施したテストのうち合格した割合（品質状況の把握）。\n"
            "未解決欠陥数: 残存する欠陥の状況（リリース判断の材料）。\n"
            "欠陥検出率: テストの有効性評価（テストプロセスの改善）。\n"
            "「テストの進捗を把握する」目的にはテストケース実行率が最も適している。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "欠陥検出率",                 "is_correct": False, "display_order": 1},
            {"choice_text": "テストケース実行率",         "is_correct": True,  "display_order": 2},
            {"choice_text": "テストケース合格率",         "is_correct": False, "display_order": 3},
            {"choice_text": "未解決欠陥数の重大度分布",   "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第109問
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行の開発プロジェクトでは、テストマネージャがプロダクトリスクを評価している。\n\n"
            "リスクの高低を判断する際に考慮すべき要素として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "プロダクトリスクの評価は「発生可能性（Likelihood）× 影響度（Impact）」の2軸で行う。"
            "発生可能性は「過去の欠陥履歴」「機能の複雑さ」「変更規模」「担当者の経験」などから判断する。"
            "影響度は「ビジネスへの損害」「利用者への影響」「法的リスク」「レピュテーションへの影響」"
            "などから判断する。"
            "この評価結果をもとにテストの優先度・深度・リソース配分を決定するのが"
            "リスクベースドテストである。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "開発担当者の経験年数と残業時間",                                                            "is_correct": False, "display_order": 1},
            {"choice_text": "欠陥が発生する可能性（発生確率）と欠陥が発生した場合の影響の大きさ（影響度）", "is_correct": True,  "display_order": 2},
            {"choice_text": "テストケースの件数とテスト担当者の人数",                                                    "is_correct": False, "display_order": 3},
            {"choice_text": "プロジェクトの予算と開発期間の長さ",                                                        "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第110問
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるオンライン書店の開発プロジェクトでは、スプリントレビュー後にプロダクトオーナーから"
            "「今回のスプリントで実装した機能の品質に問題はないか」という質問を受けた。\n\n"
            "テストマネージャがステークホルダーに報告すべき内容として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストの進捗報告では「テストがどれだけ進んでいるか（実行率・合格率）」"
            "「どのような欠陥が発見されたか（重大度・件数・状況）」"
            "「未解決の欠陥が品質・リリースにどう影響するか（リスク）」"
            "「テスト完了後に残存するリスク」を総合的に伝えることが重要である。"
            "「問題ない」と断言することはリスクを過小評価する可能性があり、"
            "欠陥件数のみでは状況判断に必要な情報が不足する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "「テストは完了しているため問題ありません」と断言する",                                                              "is_correct": False, "display_order": 1},
            {"choice_text": "テストの実施状況（実行率・合格率）・発見欠陥の状況・未解決欠陥のリスク・残存リスクを整理して報告する", "is_correct": True,  "display_order": 2},
            {"choice_text": "欠陥件数だけを報告し、詳細は割愛する",                                                                              "is_correct": False, "display_order": 3},
            {"choice_text": "テスト担当者の作業時間を報告する",                                                                                  "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第111問
        "category": "テストマネジメント",
        "difficulty": 3,
        "question_text": (
            "あるフードデリバリーサービスの開発プロジェクトでは、以下の状況が発生した。\n\n"
            "・スプリント3の開始時に、スプリント1・2の機能を対象とした回帰テストで10件の欠陥が発見された\n"
            "・発見された欠陥の原因を調査したところ、スプリント2での機能追加が"
            "スプリント1の機能に影響を与えていたことが判明した\n\n"
            "この状況から得られる教訓として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "アジャイル開発では各スプリントで機能が追加・変更されるため、"
            "既存機能への影響（デグレード）を継続的に確認する回帰テストが特に重要である。"
            "スプリントごとに回帰テストの対象が増えていくため、"
            "手動での実施は工数が増大する一方であり、自動化による効率化が有効である。"
            "CIパイプラインに回帰テストを組み込むことで、"
            "コード変更のたびに自動的に確認できる体制が理想的である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "各スプリント完了時の確認テストを徹底すれば、既存機能への影響は確認テストの範囲で十分にカバーできる",   "is_correct": False, "display_order": 1},
            {"choice_text": "機能追加・変更のたびに既存機能への影響を回帰テストで確認することが重要であり、自動化による効率化が有効である", "is_correct": True,  "display_order": 2},
            {"choice_text": "影響範囲の特定が難しいため、毎スプリント全機能を手動で全件再テストすることが唯一の確実な対策である",   "is_correct": False, "display_order": 3},
            {"choice_text": "統合を各スプリントの末尾にまとめることで、スプリント途中の回帰テストを省略できる",                    "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第112問
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行の開発プロジェクトでは、テストチームが外部の専門テスト会社から派遣されている。\n\n"
            "このような高いテスト独立性が持つデメリットとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト独立性を高めることのデメリットとして JSTQB FL は以下を挙げている。\n"
            "開発担当者とテスト担当者間のコミュニケーションコスト・調整コストが増加する。\n"
            "開発担当者が「テストは別の人がやるもの」と考え、自身の品質への責任意識が低下するリスクがある。\n"
            "外部のテスト担当者はシステムの背景・コンテキストの把握に時間がかかる。\n"
            "選択肢A・B・D はテスト独立性のメリットの説明である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "開発担当者の思い込みに引きずられず、客観的に欠陥を発見できる",                                                                        "is_correct": False, "display_order": 1},
            {"choice_text": "外部のテスト担当者は知識・経験が豊富なため、テストの質が向上する",                                                                    "is_correct": False, "display_order": 2},
            {"choice_text": "開発担当者とテスト担当者間のコミュニケーションコストが増加し、開発担当者が品質への責任意識を持ちにくくなるリスクがある", "is_correct": True,  "display_order": 3},
            {"choice_text": "テスト担当者がシステムの詳細を把握できるため、効率的にテストできる",                                                                  "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第113問
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発プロジェクトで、欠陥の傾向を分析した結果、以下のことが判明した。\n\n"
            "・全欠陥の70%が「カート機能」と「決済機能」の2つのモジュールで発見された\n"
            "・残りの8つのモジュールで30%の欠陥が分散していた\n\n"
            "この状況に関連するテストの原則として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL のテストの原則のひとつに「欠陥クラスタリング」がある。"
            "欠陥は均一に分散せず、特定のモジュール・コンポーネント・機能に集中する傾向がある。"
            "この原則はリスクベースドテストの根拠のひとつであり、"
            "過去に欠陥が多かった領域・複雑な領域・最近変更された領域に"
            "重点的にテストリソースを配分することの正当性を支持する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストの弱化：同じテストを繰り返したため欠陥発見率が低下した",                           "is_correct": False, "display_order": 1},
            {"choice_text": "欠陥クラスタリング：欠陥は少数のモジュールに集中する傾向がある",                         "is_correct": True,  "display_order": 2},
            {"choice_text": "コンテキスト依存：プロジェクトの状況によってテストアプローチは異なる",                   "is_correct": False, "display_order": 3},
            {"choice_text": "早期テスト：欠陥は早期に発見するほど修正コストが低い",                                   "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第114問
        "category": "テストマネジメント",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスのプロジェクトで、テスト担当者が書いた欠陥レポートに対して、"
            "開発担当者から「この欠陥は再現しない・自分では確認できない」と返答が来た。\n\n"
            "欠陥レポートに記載すべき「再現手順」の品質を向上させるための要素として"
            "最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "欠陥レポートの核心は「受け取った人が同じ状況を再現できること」である。"
            "再現できない欠陥は修正できないため、再現手順の品質が最重要である。"
            "具体的には「どの画面から」「どの操作を」「どの順番で」「どのデータを使って」実施したか、"
            "および「OS・ブラウザ・バージョン・ネットワーク環境」などの実行環境情報を"
            "詳細に記載する必要がある。"
            "推定原因や修正方法はあれば有用だが必須ではなく、"
            "日時と氏名は管理情報として補足的なものである。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "欠陥の推定される原因コードの箇所",                                                                       "is_correct": False, "display_order": 1},
            {"choice_text": "欠陥を再現するための具体的な操作手順・使用したデータ・実行環境（OS・ブラウザ・バージョン等）", "is_correct": True,  "display_order": 2},
            {"choice_text": "欠陥を修正するための推奨実装方法",                                                                       "is_correct": False, "display_order": 3},
            {"choice_text": "欠陥が発生した日時とテスト担当者の氏名",                                                                 "is_correct": False, "display_order": 4},
        ],
    },

    # --- ツール支援 6問 ---

    {   # MD第115問
        "category": "ツール支援",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームでは、テスト自動化ツールの導入プロセスを検討している。\n\n"
            "テスト自動化ツールを導入する際の適切なアプローチとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト自動化ツールの導入では「パイロット（試験的導入）→評価→段階的拡大」の"
            "アプローチが推奨される。"
            "最初から全面展開すると、ツールがチームのニーズに合わない場合や"
            "スクリプトの設計方針が誤っている場合に大きな損失が生じる。"
            "パイロットでは少数のテストケースを対象に自動化し、"
            "「ツールの学習コスト」「保守性」「実際の時間削減効果」「チームへの適合性」"
            "を評価することが重要である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "導入初日からすべてのテストケースを自動化する",                                             "is_correct": False, "display_order": 1},
            {"choice_text": "パイロット（試験的な小規模導入）から始め、効果と課題を評価した上で段階的に拡大する", "is_correct": True,  "display_order": 2},
            {"choice_text": "ツールの選定は行わず、最初に見つけたツールをそのまま導入する",                           "is_correct": False, "display_order": 3},
            {"choice_text": "テスト自動化ツールは導入するだけで効果が出るため、計画は不要である",                     "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第116問
        "category": "ツール支援",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行では、欠陥管理ツールを導入している。\n\n"
            "欠陥管理ツールを使用することの主なメリットとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "欠陥管理ツールの主なメリットは「欠陥のライフサイクル管理」「状況の可視化」"
            "「担当者間の情報共有」「トレーサビリティの確保（テストケース・要件との紐付け）」"
            "「傾向分析（欠陥の多いモジュール・時期の把握）」などである。"
            "ツール自体が欠陥を修正・検出する機能はなく、"
            "テスト担当者が欠陥レポートを作成・登録する作業は引き続き必要である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "欠陥管理ツールがあれば欠陥は自動的に修正される",                                                                                          "is_correct": False, "display_order": 1},
            {"choice_text": "欠陥のライフサイクル（発見→登録→割り当て→修正→確認→クローズ）を追跡・管理でき、状況の可視化とトレーサビリティを確保できる", "is_correct": True,  "display_order": 2},
            {"choice_text": "欠陥管理ツールを導入すればテスト担当者は欠陥レポートを書く必要がなくなる",                                                            "is_correct": False, "display_order": 3},
            {"choice_text": "欠陥管理ツールはソースコードの欠陥を自動検出する",                                                                                      "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第117問
        "category": "ツール支援",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発チームでは、テストツールの導入リスクについて議論した。\n\n"
            "テストツール導入に伴うリスクとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストツールの導入リスクには以下が含まれる。\n"
            "ツールへの過度な依存: 「ツールが実行したテストは正しい」という思い込みによる問題の見落とし。\n"
            "保守コスト: スクリプトがシステム変更のたびに修正が必要になる。\n"
            "スキル習得コスト: チームメンバーがツールの使い方を習得するための時間と費用。\n"
            "ベンダーロックイン: 特定ツールに依存すると将来の移行が困難になる。\n"
            "期待値とのギャップ: 自動化で発見できない問題のカテゴリが存在する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストツールを導入すると欠陥が増加するリスクがある",                                                                      "is_correct": False, "display_order": 1},
            {"choice_text": "ツールへの過度な依存・ツールのメンテナンスコスト・チームのスキル習得コスト・ツールが期待通りに機能しない可能性などのリスクがある", "is_correct": True,  "display_order": 2},
            {"choice_text": "テストツールを導入するとチームのモチベーションが向上するため、リスクはない",                                              "is_correct": False, "display_order": 3},
            {"choice_text": "テストツールのリスクは導入コストのみであり、運用後のリスクは存在しない",                                                  "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第118問
        "category": "ツール支援",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームでは、負荷テストを実施するためにツールを使用している。\n\n"
            "負荷テストツールの主な目的として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "負荷テストツール（パフォーマンステストツール）は"
            "「多数の仮想ユーザーが同時にシステムにアクセスする状況を再現し、"
            "応答時間・スループット・エラー率・リソース使用率などを測定する」ためのツールである。"
            "手動では実現困難な大量同時接続を仮想的に生成できる点が最大の特徴である。"
            "コーディング規約の検出は静的解析ツール、"
            "テストケース生成はテスト設計支援ツールの機能である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "コードのコーディング規約違反を自動的に検出する",                                                             "is_correct": False, "display_order": 1},
            {"choice_text": "複数のユーザーが同時にアクセスする状況を仮想的に再現し、システムの性能・応答時間・スループットを測定する", "is_correct": True,  "display_order": 2},
            {"choice_text": "テストケースを自動的に生成する",                                                                             "is_correct": False, "display_order": 3},
            {"choice_text": "ソースコードの欠陥を自動的に修正する",                                                                      "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第119問
        "category": "ツール支援",
        "difficulty": 3,
        "question_text": (
            "あるネット銀行の開発チームでは、テスト自動化の導入から1年が経過した。\n\n"
            "テスト自動化の成熟度を評価する指標として適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テスト自動化の成熟度・効果を評価するには複数の観点から測定することが重要である。\n"
            "自動化率（割合）: 全テストケース中何%が自動化されているか。\n"
            "実行時間の短縮: 手動と比較してどれだけ時間を削減できたか。\n"
            "保守工数: スクリプトの維持・更新にかかるコスト（低いほど良い設計）。\n"
            "欠陥検出への貢献度: 自動テストで検出した欠陥数・割合。\n"
            "コード行数・ベンダー数・合計時間は成熟度の指標として適切ではない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "自動化スクリプトのコード行数",                                                                          "is_correct": False, "display_order": 1},
            {"choice_text": "自動化されたテストケースの割合・自動化による実行時間の短縮・スクリプトの保守工数・欠陥検出への貢献度", "is_correct": True,  "display_order": 2},
            {"choice_text": "テスト自動化に使用したツールのベンダー数",                                                              "is_correct": False, "display_order": 3},
            {"choice_text": "テスト担当者が自動化に費やした合計時間",                                                               "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第120問
        "category": "ツール支援",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発チームでは、"
            "ATDD（受入テスト駆動開発）の導入を検討している。\n\n"
            "ATDDの主な特徴として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ATDD（受入テスト駆動開発）は、実装前に「受入基準（何を達成すればOKか）」を"
            "テストケースとして定義し、その受入基準を満たすようにシステムを開発する手法である。"
            "ビジネスサイド（プロダクトオーナー・ユーザー）と開発サイドが"
            "受入基準の定義に共同で関与するため、要件の共通理解を促進し、"
            "実装完了後の「思っていたものと違う」というミスマッチを防ぐ効果がある。"
            "BDD（振る舞い駆動開発）と関連する概念であり、"
            "コラボレーションベースのテストアプローチとして JSTQB FL v4.0 で新たに追加された。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "実装完了後にテストを設計する手法であり、従来の開発プロセスと同じである",                                                                  "is_correct": False, "display_order": 1},
            {"choice_text": "受入基準をテストケースとして先に定義し、その受入基準を満たすようにシステムを開発する手法であり、ビジネスサイドと開発サイドの共通理解を促進する", "is_correct": True,  "display_order": 2},
            {"choice_text": "ATDDはATM（現金自動預払機）のテストにのみ適用できる手法である",                                                                          "is_correct": False, "display_order": 3},
            {"choice_text": "ATDDは自動テストのみに適用できる手法であり、手動テストには使用できない",                                                                "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # 追加問題（MD第121〜130問）10問 — 静的テスト
    # ══════════════════════════════════════════════════════════════

    {   # MD第121問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームでは、要求仕様書のレビューを計画している。\n\n"
            "レビューを開始する前に「入口基準（エントリークライテリア）」を設定した。\n\n"
            "入口基準として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "レビューの入口基準（エントリークライテリア）は「このレビューを開始してよい状態」を定義するものである。"
            "代表的な入口基準として「レビュー対象の成果物がある程度完成しており安定していること」"
            "「参加者が事前に成果物を入手して確認できること」"
            "「必要な参加者のスケジュールが確保されていること」などが挙げられる。"
            "欠陥の修正完了や合格点の取得は出口基準（エグジットクライテリア）や別の工程に関する条件であり、入口基準ではない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "レビューで発見された欠陥がすべて修正されていること",                                                             "is_correct": False, "display_order": 1},
            {"choice_text": "レビュー対象の成果物が一定の完成度に達しており、参加者が事前に内容を確認できる状態であること", "is_correct": True,  "display_order": 2},
            {"choice_text": "レビュー後にリリース判断が完了していること",                                                                     "is_correct": False, "display_order": 3},
            {"choice_text": "レビュー参加者が全員合格点を取得していること",                                                                   "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第122問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行の開発プロジェクトで、設計書のレビューを実施した。\n\n"
            "レビューアが「事前に成果物を読んでおらず、会議の場で初めて内容を確認している」"
            "という状況が発覚した。\n\n"
            "この状況が引き起こす問題として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "形式的なレビュー（インスペクション・テクニカルレビュー）では、"
            "レビューアが事前に成果物を個別に確認し、欠陥・懸念点・質問を整理してから会議に臨むことが前提である。"
            "この事前準備（個別レビュー）こそがレビュー品質の核心であり、"
            "会議はその結果を集約・議論する場として位置づけられる。"
            "事前確認なしでは会議中の読み合わせに時間を取られ、"
            "深い議論ができず重要な欠陥を見落とすリスクが高まる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "レビュー会議が形式的な確認作業になり、深い欠陥を発見できない可能性がある",                   "is_correct": True,  "display_order": 1},
            {"choice_text": "事前確認なしの方が先入観なく指摘できるため、レビュー品質が向上する",                         "is_correct": False, "display_order": 2},
            {"choice_text": "レビューは会議の場で全員が同時に確認する形式が標準であるため、問題はない",                   "is_correct": False, "display_order": 3},
            {"choice_text": "事前確認の有無はレビューの結果に影響しない",                                                 "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第123問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発チームで、"
            "コードレビューにおける「作成者の認知バイアス」が問題になっていた。\n\n"
            "このバイアスの内容として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "認知バイアスの観点から、人は自分が作成した成果物に対して"
            "「正しく動くはず」「この部分は問題ないはず」という先入観（確証バイアス）を持ちやすい。"
            "このため、自身の書いたコードの欠陥を見落としやすくなる。"
            "これがテスト独立性が重要とされる主な理由のひとつでもある。"
            "レビューにおいて作成者以外の視点を加えることで、このバイアスの影響を軽減できる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "作成者はコードに詳しすぎるため、レビュー会議のファシリテーションが得意になりすぎる",                           "is_correct": False, "display_order": 1},
            {"choice_text": "作成者は自分が書いたコードに対して「こう動くはず」という思い込みを持ちやすく、自身の欠陥を見落としやすい", "is_correct": True,  "display_order": 2},
            {"choice_text": "作成者はレビューに参加するとコードを書き直したくなるため、議論が収束しない",                               "is_correct": False, "display_order": 3},
            {"choice_text": "作成者のバイアスはレビュー結果には影響せず、別の問題が原因である",                                           "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第124問
        "category": "静的テスト",
        "difficulty": 3,
        "question_text": (
            "あるECサイトのプロジェクトで、インスペクションを実施した。\n\n"
            "インスペクションのプロセスとして最も適切な順序はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL v4.0 で定義されているレビュープロセスの標準的な順序は以下の通りである。\n"
            "1. 計画: 対象成果物・参加者・スケジュール・入口基準の確認。\n"
            "2. レビュー開始（キックオフ）: 目的・範囲・役割の確認（形式的なレビューの場合）。\n"
            "3. 個別レビュー: 各レビューアが事前に成果物を確認し欠陥を識別。\n"
            "4. レビュー会議: 個別レビューの結果を持ち寄り議論・合意。\n"
            "5. 修正: 指摘事項に基づき作成者が成果物を修正。\n"
            "6. フォローアップ: 修正が適切に行われたかをモデレータが確認。\n"
            "個別レビューを会議の前に実施する点が重要であり、会議の場で初めて読むのは非効率である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "計画 → 個別レビュー → レビュー会議 → 修正 → フォローアップ",         "is_correct": True,  "display_order": 1},
            {"choice_text": "レビュー会議 → 個別レビュー → 計画 → 修正 → フォローアップ",         "is_correct": False, "display_order": 2},
            {"choice_text": "計画 → レビュー会議 → 個別レビュー → 修正 → フォローアップ",         "is_correct": False, "display_order": 3},
            {"choice_text": "個別レビュー → 計画 → レビュー会議 → フォローアップ → 修正",         "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第125問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行のプロジェクトで、レビューを実施した結果を記録する担当者がいなかった。\n\n"
            "この状況で発生するリスクとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "形式的なレビューでは書記（レコーダー）が指摘事項・決定事項・アクションアイテムを記録する役割を担う。"
            "記録がない場合、「何が指摘されたか」「誰が対応するか」「修正が完了したか」が追跡できなくなり、"
            "修正漏れ・フォローアップ不足・同じ問題の再発につながるリスクがある。"
            "また記録はレビューメトリクスの収集（欠陥密度・レビュー効率の評価）にも使用されるため、"
            "プロセス改善の観点でも重要である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "指摘事項が記録されず、修正漏れ・再発が生じるリスクがある",                               "is_correct": True,  "display_order": 1},
            {"choice_text": "記録がなくてもレビュー参加者の記憶があれば問題ない",                                     "is_correct": False, "display_order": 2},
            {"choice_text": "レビューの記録は任意であり、なくても品質への影響はない",                                 "is_correct": False, "display_order": 3},
            {"choice_text": "記録の担当がいない場合は作成者が記録すべきであり、欠陥発見には影響しない",               "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第126問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスの開発チームで、アーキテクチャ設計書のレビューを実施した。\n\n"
            "このレビューで発見しやすい欠陥の種類として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "アーキテクチャ設計書のレビューは静的テストの一形態であり、"
            "実行を伴わずに成果物を検査することで発見できる欠陥を対象とする。"
            "設計レビューで特に発見しやすいのは「コンポーネント間の整合性の問題」"
            "「拡張性・保守性に関する設計上の欠陥」「セキュリティアーキテクチャの脆弱性」"
            "「非機能要件への対応漏れ」などである。"
            "本番環境でのみ発生する性能問題やネットワーク遅延は動的テストでないと確認できない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "本番環境でのみ発生する性能劣化",                                                                              "is_correct": False, "display_order": 1},
            {"choice_text": "設計段階での矛盾・一貫性のなさ・将来の変更に対する脆弱性・セキュリティアーキテクチャの問題", "is_correct": True,  "display_order": 2},
            {"choice_text": "エンドユーザーが特定操作をした場合にのみ発生する障害",                                                        "is_correct": False, "display_order": 3},
            {"choice_text": "ネットワーク遅延によって発生するタイムアウトエラー",                                                          "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第127問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発プロジェクトで、レビューの効果を測定するためにメトリクスを収集した。\n\n"
            "以下のメトリクスのうち、レビューの「効率」を測定するために最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "レビューメトリクスは「効果（何件の欠陥を発見したか）」と"
            "「効率（どれだけの工数で発見したか）」の2軸で評価する。"
            "効率を測定するメトリクスとしては「1時間あたりのレビューページ数（レビュー速度）」や"
            "「1時間あたりの欠陥発見数」が代表的である。"
            "参加人数やページ数はリソース・規模の情報であり、効率を直接測定するものではない。"
            "重大度「高」の欠陥数は欠陥の重要性を示す指標であり、効率ではなく欠陥の性質を表す。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "レビューで発見された欠陥のうち、重大度「高」の欠陥の件数",     "is_correct": False, "display_order": 1},
            {"choice_text": "1時間あたりのレビューページ数または1時間あたりの欠陥発見数", "is_correct": True,  "display_order": 2},
            {"choice_text": "レビュー会議に参加した人数",                                   "is_correct": False, "display_order": 3},
            {"choice_text": "レビュー対象成果物のページ数",                                 "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第128問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行のプロジェクトで、テスト担当者がテストケースのレビューを実施した。\n\n"
            "テストケースをレビューする主な目的として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストケース自体も静的テストの対象となる成果物である。"
            "テストケースをレビューすることで「テスト条件に対するカバレッジの漏れ」"
            "「期待結果の曖昧さ・不正確さ」「前提条件・手順の不備」「テストデータの不足」などを発見できる。"
            "質の低いテストケースは実行しても有効な欠陥発見につながらないため、"
            "事前のレビューで品質を確保することがテスト全体の有効性向上につながる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストケースの実行を高速化するため",                                                                                   "is_correct": False, "display_order": 1},
            {"choice_text": "テストケースの観点漏れ・期待結果の不備・テスト条件との不一致を発見し、テストの有効性を高めるため", "is_correct": True,  "display_order": 2},
            {"choice_text": "テストケースの数を増やすため",                                                                                         "is_correct": False, "display_order": 3},
            {"choice_text": "テストの自動化スクリプトを生成するため",                                                                               "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第129問
        "category": "静的テスト",
        "difficulty": 3,
        "question_text": (
            "あるフードデリバリーサービスの開発チームで、同一の成果物に対して"
            "「ウォークスルー」と「インスペクション」のどちらを選択するか検討している。\n\n"
            "インスペクションが適しているケースとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "レビュー形式はコンテキストに応じて選択する。\n"
            "ウォークスルー: 作成者が進行し、内容の説明・共有・アイデア発散が目的。"
            "比較的カジュアルな成果物や、チームの理解共有に向いている。\n"
            "インスペクション: モデレータが進行し、チェックリスト・入口/出口基準・メトリクスを使用する最も形式的なレビュー。"
            "高リスク・高重要度の成果物に対して体系的・網羅的に欠陥を発見したい場合に適している。\n"
            "選択肢AとDはウォークスルーが適しており、Bはブレインストーミング的なアプローチが適している。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "チームメンバーが成果物の内容を理解するための勉強会として実施したい場合",                              "is_correct": False, "display_order": 1},
            {"choice_text": "新しいアイデアを発散させ、設計の可能性を広げたい場合",                                               "is_correct": False, "display_order": 2},
            {"choice_text": "高リスクな成果物（基幹系システムの設計書など）に対して、体系的・網羅的に欠陥を発見したい場合", "is_correct": True,  "display_order": 3},
            {"choice_text": "作成者が内容を説明しながら参加者の理解を得たい場合",                                                 "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第130問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームで、静的テストと動的テストの使い分けについて議論した。\n\n"
            "静的テストでのみ発見できる（動的テストでは発見しにくい）欠陥の例として"
            "最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "静的テストはソフトウェアを実行せずに成果物を検査するため、"
            "「要求仕様書・設計書・コード」に存在する欠陥のうち、実行しなくても確認できるものを発見できる。"
            "用語の不統一・参照先不明・矛盾した記述・あいまいな表現はソフトウェアを動作させても"
            "「障害」として顕在化しないことが多く、静的テストでなければ発見しにくい。"
            "選択肢A・C・Dはいずれもソフトウェアを実際に実行することで発見できる欠陥であり、"
            "動的テストの対象である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "特定の入力値の組み合わせでシステムがクラッシュする欠陥",             "is_correct": False, "display_order": 1},
            {"choice_text": "要求仕様書に記載された「用語の不統一」や「参照先不明の記述」",       "is_correct": True,  "display_order": 2},
            {"choice_text": "本番環境の負荷状況でのみ発生するデッドロック",                       "is_correct": False, "display_order": 3},
            {"choice_text": "ユーザーが誤操作したときに発生するエラーメッセージの文言誤り",       "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # 追加問題（MD第131〜140問）10問
    # 静的テスト 6問（MD第131〜136問）+ テスト技法 4問（MD第137〜140問）
    # ══════════════════════════════════════════════════════════════

    {   # MD第131問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行のプロジェクトで、レビューに参加したレビューアが指摘事項を多数提出した。\n\n"
            "レビュー会議中、モデレータが取るべき行動として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "レビュー会議の目的は「欠陥を記録・合意すること」であり、「修正方法を決定すること」ではない。"
            "修正方法の議論を会議中に行うと時間が超過し、本来の欠陥発見に使う時間が失われる。"
            "モデレータはレビュー会議を「欠陥の識別・記録・優先付け」に集中させ、"
            "修正の具体的な方法は作成者と関係者が別途決定するよう議事を整理する責任を持つ。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "すべての指摘について会議中に修正方法を議論して解決する",                                           "is_correct": False, "display_order": 1},
            {"choice_text": "指摘事項を記録し、修正方法の議論は会議の外（作成者と担当者の間）で行うよう整理する", "is_correct": True,  "display_order": 2},
            {"choice_text": "指摘の多いレビューアの発言を制限し、会議時間を短縮する",                                           "is_correct": False, "display_order": 3},
            {"choice_text": "すべての指摘をその場で却下し、次回のレビューに回す",                                               "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第132問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスの開発チームで、コードの静的解析を実施したところ"
            "「循環的複雑度（サイクロマティック複雑度）が高い」という警告が複数出力された。\n\n"
            "循環的複雑度が高いことが示す問題として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "循環的複雑度（Cyclomatic Complexity）はコードの複雑さを定量的に示すメトリクスであり、"
            "分岐・ループ・条件文の数に基づいて計算される。"
            "値が高いほど「理解しにくい」「テストケースが多く必要」「修正時にバグを作り込みやすい」傾向がある。"
            "静的解析ツールはこの値を自動的に計算し、閾値を超えた場合に警告を出力する。"
            "循環的複雑度は実行速度・文法エラー・セキュリティ脆弱性とは直接関係しない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "コードの実行速度が遅いことを示している",                                                                   "is_correct": False, "display_order": 1},
            {"choice_text": "コードの分岐・条件が多く複雑なため、理解・保守・テストが困難になりやすいことを示している", "is_correct": True,  "display_order": 2},
            {"choice_text": "コードに文法エラーがあることを示している",                                                                 "is_correct": False, "display_order": 3},
            {"choice_text": "コードのセキュリティ脆弱性が多いことを示している",                                                         "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第133問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発プロジェクトで、非公式レビュー（インフォーマルレビュー）を実施することにした。\n\n"
            "非公式レビューの特徴として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "JSTQB FL v4.0 では最も形式度が低いレビューとして「非公式レビュー（インフォーマルレビュー）」を定義している。"
            "非公式レビューには決まったプロセス・役割・記録義務がなく、"
            "担当者が気軽に同僚にコードや文書を見てもらう形で実施される。"
            "ペアプログラミング中のコードレビューや、メールで送った文書にコメントをもらう行為も"
            "非公式レビューに含まれる。"
            "形式的な役割・チェックリスト・メトリクスはインスペクションの特徴である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "モデレータが必ず進行を担当し、チェックリストを使用する",                                                         "is_correct": False, "display_order": 1},
            {"choice_text": "形式的な手順・役割・記録が定められておらず、柔軟に実施できる最もカジュアルなレビュー形式である", "is_correct": True,  "display_order": 2},
            {"choice_text": "入口基準と出口基準が必須であり、メトリクスを収集する",                                                           "is_correct": False, "display_order": 3},
            {"choice_text": "参加者全員が事前に成果物を個別確認し、会議で指摘を持ち寄る形式である",                                           "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第134問
        "category": "静的テスト",
        "difficulty": 3,
        "question_text": (
            "あるネット銀行のプロジェクトで、レビューを実施したところ、以下のメトリクスが得られた。\n\n"
            "・レビュー対象：設計書 50ページ\n"
            "・レビュー所要時間：10時間（準備5時間 + 会議5時間）\n"
            "・発見欠陥数：40件\n"
            "・レビュー後に動的テストで発見された欠陥数：10件\n\n"
            "このデータから計算できる「レビューの欠陥検出率」として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "欠陥検出率（Defect Detection Percentage）は「発見された総欠陥数のうち、その手法で発見した割合」を示す。\n"
            "総欠陥数 = レビューで発見した40件 + 動的テストで発見した10件 = 50件。\n"
            "レビューの欠陥検出率 = 40 ÷ 50 × 100 = 80%。\n"
            "この指標はレビューの有効性を評価するために使用され、"
            "値が高いほどレビューで多くの欠陥を早期に発見できていることを示す。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "40%", "is_correct": False, "display_order": 1},
            {"choice_text": "80%", "is_correct": True,  "display_order": 2},
            {"choice_text": "50%", "is_correct": False, "display_order": 3},
            {"choice_text": "25%", "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第135問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスのプロジェクトで、テスト担当者が"
            "ユーザーマニュアルのレビューを実施することになった。\n\n"
            "ユーザーマニュアルをレビューする目的として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "静的テストはソースコードだけでなく、"
            "要求仕様書・設計書・テストケース・ユーザーマニュアル・トレーニング資料など、"
            "さまざまな作業成果物を対象にできる。"
            "ユーザーマニュアルのレビューでは「記載内容が実際のシステム動作と一致しているか」"
            "「手順が正確かつ分かりやすいか」「用語が一貫しているか」などを確認する。"
            "マニュアルの誤りはユーザーの誤操作・問い合わせ増加・信頼低下につながるため、"
            "リリース前のレビューが重要である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ユーザーマニュアルはコードではないため、静的テストの対象外である",                                  "is_correct": False, "display_order": 1},
            {"choice_text": "内容の正確性・一貫性・分かりやすさ・実際のシステム動作との整合性を確認するため", "is_correct": True,  "display_order": 2},
            {"choice_text": "ユーザーマニュアルのレビューは品質に影響しないため、省略してよい",                                  "is_correct": False, "display_order": 3},
            {"choice_text": "ユーザーマニュアルは本番リリース後に作成するものであり、テスト期間中のレビュー対象ではない",        "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第136問
        "category": "静的テスト",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームで、静的解析ツールが出力した警告について議論した。\n\n"
            "「静的解析ツールが警告を出していないコードは安全である」という主張への"
            "評価として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "静的解析ツールには「誤検知（フォールスポジティブ：問題でないものを警告）」と"
            "「見逃し（フォールスネガティブ：実際の問題を検出できない）」の両方が存在する。"
            "すべての欠陥パターンを網羅したルールセットを持つツールは存在せず、"
            "ツールが警告を出さなくてもロジックエラー・セキュリティの脆弱性・設計上の問題が"
            "存在する可能性がある。"
            "静的解析は動的テストの補完であり、代替ではない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "正しい。静的解析ツールが警告を出さなければ欠陥はない",                                                                                       "is_correct": False, "display_order": 1},
            {"choice_text": "誤り。静的解析ツールには検出できないパターンがあり、警告がなくても欠陥が存在する可能性がある（見逃し・フォールスネガティブ）", "is_correct": True,  "display_order": 2},
            {"choice_text": "静的解析ツールの精度は100%であるため、正しい",                                                                                               "is_correct": False, "display_order": 3},
            {"choice_text": "静的解析ツールは動的テストを代替するため、警告がなければテスト不要である",                                                                  "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第137問（ホワイトボックステスト → テスト技法）
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームでは、ホワイトボックステストを実施する目的について議論した。\n\n"
            "ホワイトボックステストの主な目的として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ホワイトボックステストはコードの内部構造を根拠にテストケースを設計するテスト技法である。"
            "テストケースは「どの命令を実行するか」「どの分岐を通るか」「どのパスを辿るか」という"
            "コード構造の観点から設計される。"
            "これに対してブラックボックステストは外部仕様（何ができるか）を根拠にテストケースを設計する。"
            "ホワイトボックスとブラックボックスは補完関係にあり、"
            "両方を組み合わせることで高い品質を実現できる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ソフトウェアの外部から見た機能（何ができるか）を確認すること",                                                                  "is_correct": False, "display_order": 1},
            {"choice_text": "コードの内部構造（分岐・命令・パス）を根拠にテストケースを設計し、コードがどのように動作するかを確認すること", "is_correct": True,  "display_order": 2},
            {"choice_text": "ユーザーがシステムを使いやすいかどうかを評価すること",                                                                          "is_correct": False, "display_order": 3},
            {"choice_text": "セキュリティ診断を外部機関に依頼すること",                                                                                      "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第138問（ホワイトボックステスト → テスト技法）
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行のシステムで、以下のロジックが存在する。\n\n"
            "if (残高 >= 1000) {\n"
            "  振込処理を実行する\n"
            "} else {\n"
            "  エラーメッセージを表示する\n"
            "}\n\n"
            "このコードに対してステートメントカバレッジ（命令網羅）100%を達成するために"
            "必要な最小テストケース数として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ステートメントカバレッジは「すべての命令を少なくとも1回実行すること」を要件とする。"
            "このコードには「振込処理を実行する」と「エラーメッセージを表示する」の"
            "2つの命令がある（条件の両分岐それぞれが必要）。\n"
            "テストケース1：残高 >= 1000（振込処理の命令を実行）。\n"
            "テストケース2：残高 < 1000（エラーメッセージの命令を実行）。\n"
            "両方の命令を実行するには最低2件のテストケースが必要であり、"
            "ブランチカバレッジ100%も同時に達成される。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "1", "is_correct": False, "display_order": 1},
            {"choice_text": "2", "is_correct": True,  "display_order": 2},
            {"choice_text": "3", "is_correct": False, "display_order": 3},
            {"choice_text": "4", "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第139問（ホワイトボックステスト → テスト技法）
        "category": "テスト技法",
        "difficulty": 3,
        "question_text": (
            "あるECサイトの開発チームで、単体テストを実施した結果"
            "「ステートメントカバレッジ100%を達成した」と報告があった。\n\n"
            "テストリーダーは「ステートメントカバレッジ100%でも、まだ確認できていない箇所がある」"
            "と判断し、追加のテストを求めた。\n\n"
            "テストリーダーがこのように判断した根拠として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ステートメントカバレッジは「すべての命令を少なくとも1回実行すること」を要件とする。"
            "if文のtrueブランチにある命令を実行すれば、falseブランチが未実行でも"
            "ステートメントカバレッジ100%を達成できる場合がある。\n"
            "このため「ステートメントカバレッジ100% = すべての分岐を確認した」とはならない。"
            "ブランチカバレッジはすべての分岐（true/false両側）の実行を要件とするより強い基準であり、"
            "ステートメントカバレッジ100%を達成してもブランチカバレッジが100%でない場合がある。\n"
            "テストリーダーはこの点を踏まえ、ブランチカバレッジを達成するための追加テストを求めたと判断できる。"
            "なお逆の関係（ブランチ100% → ステートメント100%）は必ず成立する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ステートメントカバレッジ100%はすべての分岐（true/false両側）を実行したことを意味するため、追加テストは不要である",                                    "is_correct": False, "display_order": 1},
            {"choice_text": "ステートメントカバレッジ100%はすべての命令を実行したことを示すが、if文のfalse側など、実行されていない分岐が存在する場合があり、ブランチカバレッジは達成されていない可能性がある", "is_correct": True,  "display_order": 2},
            {"choice_text": "ステートメントカバレッジ100%を達成すれば、パスカバレッジも自動的に100%になる",                                                                        "is_correct": False, "display_order": 3},
            {"choice_text": "ステートメントカバレッジはホワイトボックステストの最も強い基準であるため、100%達成で十分である",                                                      "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第140問（ホワイトボックステスト → テスト技法）修正版
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行のシステムで、ホワイトボックステストを担当するテスト担当者が"
            "「パスカバレッジ」について説明している。\n\n"
            "パスカバレッジ（経路網羅）の説明として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "カバレッジ基準には以下の種類がある（強い順）。\n"
            "ステートメントカバレッジ: すべての命令を1回実行。\n"
            "ブランチカバレッジ: すべての分岐（true/false）を1回実行。\n"
            "パスカバレッジ: すべての実行パス（分岐の組み合わせ経路）を実行。\n"
            "パスカバレッジは最も強い基準だが、"
            "ループや分岐の組み合わせが増えると実行パス数が指数的に増加するため、"
            "実務での完全達成は現実的でない場合が多い。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "すべての命令を少なくとも1回実行すること",                                 "is_correct": False, "display_order": 1},
            {"choice_text": "すべての分岐（true/false）を少なくとも1回実行すること",                   "is_correct": False, "display_order": 2},
            {"choice_text": "コード中のすべての実行パス（命令の組み合わせ経路）を少なくとも1回実行すること", "is_correct": True,  "display_order": 3},
            {"choice_text": "コード中のすべての条件式のすべての真偽値の組み合わせを実行すること",       "is_correct": False, "display_order": 4},
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # 追加問題（MD第141〜150問）10問
    # テスト技法 8問（MD第141〜148問）+ ツール支援 2問（MD第149〜150問）
    # ══════════════════════════════════════════════════════════════

    {   # MD第141問（ホワイトボックステスト → テスト技法）
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発チームで、"
            "ホワイトボックステストとブラックボックステストの補完関係について議論した。\n\n"
            "両者の組み合わせが効果的である理由として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ホワイトボックステストはコードの内部構造を根拠とするため"
            "「実装されたコードのどの部分が実行されていないか」を確認するのに優れている。"
            "ブラックボックステストは外部仕様を根拠とするため"
            "「要求仕様で定義された機能が正しく動作するか」を確認するのに優れている。"
            "ホワイトボックステストでは「仕様にはないが実装されてしまったコード」は発見しにくく、"
            "ブラックボックステストでは「実行されていないコードパス」を把握できない。"
            "両者を組み合わせることで互いの弱点を補完できる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ホワイトボックステストだけで十分であり、ブラックボックステストは不要である",                                                                          "is_correct": False, "display_order": 1},
            {"choice_text": "ホワイトボックステストはコードの網羅性を確認でき、ブラックボックステストは仕様の観点から確認でき、互いに異なる種類の欠陥を発見しやすい", "is_correct": True,  "display_order": 2},
            {"choice_text": "ブラックボックステストだけで十分であり、ホワイトボックステストは上級者向けである",                                                                  "is_correct": False, "display_order": 3},
            {"choice_text": "両者は同じ欠陥を発見するため、どちらか一方を選べばよい",                                                                                            "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第142問（ホワイトボックステスト → テスト技法）
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームで、単体テストにホワイトボックステストを適用している。\n\n"
            "単体テストでホワイトボックステストを適用する主な利点として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "単体テストはコンポーネントレベルの内部動作を確認するテストレベルであり、"
            "ホワイトボックステストとの親和性が高い。"
            "開発担当者はコードの内部構造を熟知しているため、"
            "どの分岐・パスをテストすべきかを効率的に判断できる。"
            "またカバレッジ計測ツールと組み合わせることで「テストされていないコードパス」を可視化し、"
            "テスト漏れを発見できる。"
            "受入テストはユーザーが実施するテストレベルであり、単体テストで代替できるものではない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ユーザーの操作を忠実に再現できる",                                                                                               "is_correct": False, "display_order": 1},
            {"choice_text": "コードを書いた担当者が内部構造を知っているため、効率的にテストケースを設計でき、テストされていないコードパスを早期に発見できる", "is_correct": True,  "display_order": 2},
            {"choice_text": "外部仕様だけを見ればよいため、コードの知識が不要である",                                                                         "is_correct": False, "display_order": 3},
            {"choice_text": "受入テストの代わりとして機能する",                                                                                               "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第143問（ホワイトボックステスト → テスト技法）
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発チームで、"
            "ホワイトボックステストのカバレッジ基準について議論した。\n\n"
            "「ブランチカバレッジ（分岐網羅）」の説明として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ブランチカバレッジは「コード中のすべての分岐を少なくとも1回実行すること」を"
            "要件とするカバレッジ基準である。"
            "if文であればtrueとfalseの両方を、ループであればループ内と迂回の両方を実行することが求められる。\n"
            "FL v4.0のホワイトボックステスト技法における主要な基準の区別は以下の通りである。\n"
            "ステートメントカバレッジ（A）: すべての命令を実行。ブランチカバレッジより弱い基準。\n"
            "ブランチカバレッジ（B）: すべての分岐を実行。ステートメントカバレッジを包含する。\n"
            "パスカバレッジ（C）: すべての実行パスを実行。ブランチカバレッジより強い基準。\n"
            "選択肢Dはブラックボックステストの説明であり、ホワイトボックステストとは逆の考え方である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "コード中のすべての命令を少なくとも1回実行すること",                             "is_correct": False, "display_order": 1},
            {"choice_text": "コード中のすべての分岐（if文のtrue側・false側など）を少なくとも1回実行すること", "is_correct": True,  "display_order": 2},
            {"choice_text": "コード中のすべての実行パス（分岐の組み合わせ経路）を実行すること",             "is_correct": False, "display_order": 3},
            {"choice_text": "テスト担当者がコードを読まずに仕様書だけを根拠にテストすること",               "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第144問（ホワイトボックステスト → テスト技法）
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるホテル予約サービスの開発チームで、"
            "ホワイトボックステストの適用時期について議論した。\n\n"
            "ホワイトボックステストが最も適しているテストレベルとして最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ホワイトボックステストはコードの内部構造を根拠とするため、"
            "コードへのアクセスと理解が前提となる。"
            "単体テストでは個別コンポーネントのコードを直接参照してテストケースを設計し、"
            "結合テストではコンポーネント間のインターフェースのコードレベルの動作を確認する。"
            "システムテスト・受入テストでは通常、外部仕様（ユーザーから見た動作）を根拠とする"
            "ブラックボックステストが主体となる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "システムテストおよび受入テスト（ユーザーが機能を確認する段階）",         "is_correct": False, "display_order": 1},
            {"choice_text": "単体テストおよび結合テスト（開発担当者がコードレベルで確認する段階）", "is_correct": True,  "display_order": 2},
            {"choice_text": "ホワイトボックステストはすべてのテストレベルで同等に適用される",       "is_correct": False, "display_order": 3},
            {"choice_text": "ホワイトボックステストは本番リリース後のモニタリングフェーズにのみ適用される", "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第145問（ホワイトボックステスト → テスト技法）
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームで、コードカバレッジ計測ツールを単体テストに導入した。\n\n"
            "カバレッジ計測ツールを使用する主な目的として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "カバレッジ計測ツール（コードカバレッジツール）は、"
            "テスト実行中にどの命令・分岐・パスが実行されたかを記録し、"
            "ステートメントカバレッジやブランチカバレッジなどの達成率をレポートするツールである。"
            "このツールを使うことで「テストされていないコードパス」を可視化し、テスト漏れを発見できる。"
            "ただしカバレッジが高いことは「多くのコードが実行された」ことを示すが"
            "「バグがない」ことを保証するわけではない点に注意が必要である。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストが合格したことを証明するため",                                                            "is_correct": False, "display_order": 1},
            {"choice_text": "テストによって実行されたコードの割合を可視化し、テストされていないコードパスを特定するため", "is_correct": True,  "display_order": 2},
            {"choice_text": "コードを自動的に修正するため",                                                                  "is_correct": False, "display_order": 3},
            {"choice_text": "テストケースを自動的に生成するため",                                                            "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第146問（ホワイトボックステスト → テスト技法）
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行の開発チームで、"
            "「ブランチカバレッジ100%を達成したので品質は十分」という主張が出た。\n\n"
            "この主張への評価として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "カバレッジはテストの網羅性の一側面を示す指標であり、"
            "100%を達成してもすべての欠陥を発見できる保証はない。"
            "ブランチカバレッジ100%が意味するのは「すべての分岐（true/false）が少なくとも1回実行された」ことであり、"
            "「すべての入力値の組み合わせをテストした」"
            "「仕様に基づくすべての観点を確認した」ことではない。"
            "また、カバレッジは「どのコードが実行されたか」を示すが、"
            "「実行されたコードが正しく動作したか」はテストの期待結果との比較で判断する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "正しい。ブランチカバレッジ100%はすべての欠陥を発見することを保証する",                                                                                                               "is_correct": False, "display_order": 1},
            {"choice_text": "誤り。ブランチカバレッジ100%は「すべての分岐を少なくとも1回実行した」ことを示すが、全テスト値の組み合わせや仕様に基づく観点を網羅するわけではなく、欠陥の不在を保証しない", "is_correct": True,  "display_order": 2},
            {"choice_text": "ブランチカバレッジ100%は不可能であるため、この主張自体が成立しない",                                                                                                               "is_correct": False, "display_order": 3},
            {"choice_text": "ブランチカバレッジ100%を達成すれば、動的テストはそれ以上不要である",                                                                                                               "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第147問（ホワイトボックステスト → テスト技法）
        "category": "テスト技法",
        "difficulty": 2,
        "question_text": (
            "あるフードデリバリーサービスの開発チームで、"
            "ホワイトボックステストを実施する担当者を決める議論をしている。\n\n"
            "ホワイトボックステストを実施する担当者として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "ホワイトボックステストはコードの内部構造（分岐・命令・パス）を根拠にテストケースを設計するため、"
            "コードを読み理解できることが前提となる。"
            "通常は「コードを書いた開発担当者」または"
            "「コードレビューや技術的なテスト設計が得意なテスト担当者」が担当する。"
            "エンドユーザーは外部仕様のみを見て確認するブラックボックステスト（受入テスト等）に適しており、"
            "コードの内部構造を知る必要はない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "エンドユーザー（システムの利用者）",                                     "is_correct": False, "display_order": 1},
            {"choice_text": "コードの内部構造を理解している開発担当者またはテスト担当者", "is_correct": True,  "display_order": 2},
            {"choice_text": "プロジェクトマネージャ",                                                 "is_correct": False, "display_order": 3},
            {"choice_text": "外部の監査機関",                                                         "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第148問（ホワイトボックステスト → テスト技法）
        "category": "テスト技法",
        "difficulty": 3,
        "question_text": (
            "あるECサイトの開発チームで、"
            "ステートメントカバレッジとブランチカバレッジの違いを説明している。\n\n"
            "以下の説明のうち最も正確なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "2つのカバレッジ基準の関係を正確に理解することが重要である。\n"
            "ステートメントカバレッジ: すべての命令（ステートメント）を少なくとも1回実行する。"
            "if文でtrueブランチだけを通っても、命令が実行されれば達成できる場合がある。\n"
            "ブランチカバレッジ: すべての分岐（true/false両方）を少なくとも1回実行する。より強い（厳しい）基準。\n"
            "ブランチカバレッジ100%を達成すれば、すべての分岐を通るため"
            "すべての命令も実行され、ステートメントカバレッジ100%も自動的に達成される。"
            "逆（ステートメント100% → ブランチ100%）は成立しない。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "ステートメントカバレッジとブランチカバレッジは同じ意味であり、区別は不要である",                                                                                                        "is_correct": False, "display_order": 1},
            {"choice_text": "ステートメントカバレッジはすべての命令を実行することを目標とし、ブランチカバレッジはすべての分岐（true/false）を実行することを目標とする。ブランチカバレッジ100%を達成するとステートメントカバレッジ100%も達成されるが、逆は成立しない", "is_correct": True,  "display_order": 2},
            {"choice_text": "ブランチカバレッジを達成しても、ステートメントカバレッジは達成されない場合がある",                                                                                                      "is_correct": False, "display_order": 3},
            {"choice_text": "ステートメントカバレッジはブランチカバレッジより強い基準であり、より多くのテストケースが必要である",                                                                                   "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第149問（ツール支援）
        "category": "ツール支援",
        "difficulty": 2,
        "question_text": (
            "あるECサイトの開発チームで、テストツールの種類について整理している。\n\n"
            "「テストケースの設計を支援するツール」として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストツールはその用途によって分類できる。"
            "テスト設計支援ツールはテスト条件の識別・テストケースの設計・テストデータの生成などを支援するツールであり、"
            "同値分割・境界値分析・モデルベースドテストなどに基づいて"
            "テストケースや入力データを自動生成する機能を持つものがある。"
            "欠陥管理ツールは欠陥ライフサイクルの追跡、"
            "負荷テストツールは性能測定、"
            "CIサーバーはビルド・テスト実行の自動化に使用する。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "欠陥管理ツール",                                                           "is_correct": False, "display_order": 1},
            {"choice_text": "負荷テストツール",                                                         "is_correct": False, "display_order": 2},
            {"choice_text": "同値分割・境界値分析の入力データを生成・管理するテスト設計支援ツール", "is_correct": True,  "display_order": 3},
            {"choice_text": "CIサーバー（継続的インテグレーションツール）",                             "is_correct": False, "display_order": 4},
        ],
    },

    {   # MD第150問（ツール支援）
        "category": "ツール支援",
        "difficulty": 2,
        "question_text": (
            "あるネット銀行の開発チームで、継続的インテグレーション（CI）ツールを導入した。\n\n"
            "CIツールがテスト活動に与える主な効果として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "CIツール（JenkinsやGitHub Actionsなど）は、"
            "開発担当者がコードをリポジトリにプッシュするたびに"
            "自動的にビルド・単体テスト・静的解析などを実行するツールである。"
            "これにより「コード変更が既存の動作を壊していないか」を継続的・自動的に確認でき、"
            "欠陥の早期発見とシフトレフトの実践につながる。"
            "CIツール自体はテストケースを設計せず、既存の自動テストスクリプトを実行するものである。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テストケースを自動的に設計してくれるため、テスト担当者の設計作業が不要になる",                         "is_correct": False, "display_order": 1},
            {"choice_text": "コードの変更をトリガーに自動的にビルド・テストを実行し、欠陥を継続的かつ早期に検出できる", "is_correct": True,  "display_order": 2},
            {"choice_text": "本番環境へのデプロイを手動で管理できるため、リリースの安全性が向上する",                         "is_correct": False, "display_order": 3},
            {"choice_text": "CIツールを導入すると手動テストが自動化されるため、テスト担当者が不要になる",                       "is_correct": False, "display_order": 4},
        ],
    },
]
