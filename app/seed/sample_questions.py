"""JSTQB Foundation Level 向けオリジナル問題データ（82問）。

全問単一選択・4択・正解1つ。公式問題のコピーは含まない。
category は config.JSTQB_CATEGORIES の name と一致させること。
DBテーブル変更なし。questions.category（文字列）で管理する既存方式を維持。

カテゴリ配分:
  テストの基礎         18問（Q01–Q10、Q38、Q43–Q49）
  テスト活動とプロセス  17問（Q11、Q12、Q17、Q21–Q26、Q39、Q50–Q56）
  静的テスト            9問（Q13、Q32、Q33、Q57–Q62）
  テスト技法           15問（Q14–Q16、Q29、Q34–Q36、Q63–Q69、Q82）
  テストマネジメント   16問（Q18–Q20、Q27、Q28、Q30、Q31、Q37、Q40、Q70–Q76）
  ツール支援            7問（Q41、Q42、Q77–Q81）
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
]
