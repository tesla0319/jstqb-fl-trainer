"""JSTQB Foundation Level 向けオリジナル問題データ（42問）。

全問単一選択・4択・正解1つ。公式問題のコピーは含まない。
category は config.JSTQB_CATEGORIES の name と一致させること。
DBテーブル変更なし。questions.category（文字列）で管理する既存方式を維持。

カテゴリ配分:
  テストの基礎         11問（Q01–Q10、Q38）
  テスト活動とプロセス  10問（Q11、Q12、Q17、Q21–Q26、Q39）
  静的テスト            3問（Q13、Q32、Q33）
  テスト技法            7問（Q14–Q16、Q29、Q34–Q36）
  テストマネジメント    9問（Q18–Q20、Q27、Q28、Q30、Q31、Q37、Q40）
  ツール支援            2問（Q41、Q42）
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
            "具体的な入力値・期待結果・テストケースの定義に取り掛かろうとしている。\n\n"
            "この「この後に取り掛かろうとしている」活動として最も適切なものはどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "問題文に記載されている「要求仕様書を確認し、テスト観点を整理した」活動がテスト分析にあたる。"
            "「この後に取り掛かろうとしている」のは、整理した内容をもとに"
            "「具体的な入力値・期待結果・テストケースを定義する」活動であり、これはテスト設計に相当する。"
            "テスト実装はテストスクリプトやテストデータを準備する段階、"
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
            "次の作業として、具体的な入力値・期待結果・テストケースを定義しようとしている。\n\n"
            "最も適切な活動はどれか。"
        ),
        "multi_select_count": 1,
        "explanation": (
            "テストプロセスにおいて、テスト条件を識別する活動はテスト分析に相当する。"
            "識別したテスト条件をもとに「具体的な入力値・期待結果・テストケースを定義する」活動はテスト設計である。"
            "A（テスト条件を識別する）はすでに完了した活動、"
            "C（テスト環境・テストデータの準備）はテスト実装、"
            "D（テスト結果の評価）はテスト実行後の活動にあたる。"
        ),
        "trap_reason": None,
        "choices": [
            {"choice_text": "テスト条件を識別する活動",              "is_correct": False, "display_order": 1},
            {"choice_text": "テストケースと期待結果を設計する活動",    "is_correct": True,  "display_order": 2},
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
            {"choice_text": "反復実行（回帰テスト等）の効率化と一貫性のあるテスト実行を実現できる", "is_correct": True,  "display_order": 2},
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
]
