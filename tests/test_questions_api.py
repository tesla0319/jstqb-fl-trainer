"""GET /api/v1/questions・/api/v1/questions/{id}・/api/v1/categories のAPIテスト。"""


class TestGetQuestions:
    """GET /api/v1/questions の正常系・異常系テスト。"""

    def test_returns_questions_list(self, client, seeded_db):
        """問題一覧が取得できる。"""
        res = client.get("/api/v1/questions")
        assert res.status_code == 200
        data = res.json()
        assert "questions" in data
        assert len(data["questions"]) >= 1

    def test_response_has_required_fields(self, client, seeded_db):
        """レスポンスに必須フィールドが含まれる。"""
        res = client.get("/api/v1/questions")
        assert res.status_code == 200
        q = res.json()["questions"][0]
        assert "id" in q
        assert "category_name" in q
        assert "difficulty" in q
        assert "question_text" in q
        assert "choices" in q

    def test_is_correct_not_in_choices(self, client, seeded_db):
        """choices に is_correct が含まれない（カンニング防止）。"""
        res = client.get("/api/v1/questions")
        assert res.status_code == 200
        for q in res.json()["questions"]:
            for c in q["choices"]:
                assert "is_correct" not in c

    def test_choices_ordered_by_display_order(self, client, seeded_db):
        """選択肢が display_order 昇順に並んでいる。"""
        res = client.get("/api/v1/questions")
        assert res.status_code == 200
        q = res.json()["questions"][0]
        orders = [c["display_order"] for c in q["choices"]]
        assert orders == sorted(orders)

    def test_filter_by_category_id(self, client, seeded_db):
        """category_id=1 でテストの基礎カテゴリの問題のみ返る。"""
        res = client.get("/api/v1/questions?category_id=1")
        assert res.status_code == 200
        questions = res.json()["questions"]
        assert len(questions) >= 1
        for q in questions:
            assert q["category_name"] == "テストの基礎"

    def test_category_filter_no_match_returns_empty(self, client, seeded_db):
        """存在しない category_id で空配列が返る（404ではない）。"""
        res = client.get("/api/v1/questions?category_id=999")
        assert res.status_code == 200
        assert res.json()["questions"] == []

    def test_random_returns_exactly_one(self, client, seeded_db):
        """random=true のとき1問だけ返る（limit を無視する）。"""
        res = client.get("/api/v1/questions?random=true&limit=10")
        assert res.status_code == 200
        assert len(res.json()["questions"]) == 1

    def test_random_with_category_id(self, client, seeded_db):
        """random=true と category_id=1 を同時指定してもテストの基礎から1問返る。"""
        res = client.get("/api/v1/questions?random=true&category_id=1")
        assert res.status_code == 200
        questions = res.json()["questions"]
        assert len(questions) == 1
        assert questions[0]["category_name"] == "テストの基礎"

    def test_random_empty_category_returns_empty(self, client, seeded_db):
        """random=true で対象0件なら空配列が返る。"""
        res = client.get("/api/v1/questions?random=true&category_id=999")
        assert res.status_code == 200
        assert res.json()["questions"] == []

    def test_limit_zero_returns_422(self, client, seeded_db):
        """limit=0 は 422。"""
        res = client.get("/api/v1/questions?limit=0")
        assert res.status_code == 422

    def test_limit_negative_returns_422(self, client, seeded_db):
        """limit=-1 は 422。"""
        res = client.get("/api/v1/questions?limit=-1")
        assert res.status_code == 422

    def test_invalid_category_id_type_returns_422(self, client, seeded_db):
        """category_id に文字列を渡すと 422。"""
        res = client.get("/api/v1/questions?category_id=abc")
        assert res.status_code == 422


class TestGetQuestionById:
    """GET /api/v1/questions/{question_id} のテスト。"""

    def test_get_existing_question(self, client, seeded_db):
        """存在する question_id で1問返る。"""
        q_id = seeded_db["q1_id"]
        res = client.get(f"/api/v1/questions/{q_id}")
        assert res.status_code == 200
        questions = res.json()["questions"]
        assert len(questions) == 1
        assert questions[0]["id"] == q_id

    def test_is_correct_not_in_response(self, client, seeded_db):
        """1件取得レスポンスにも is_correct が含まれない。"""
        q_id = seeded_db["q1_id"]
        res = client.get(f"/api/v1/questions/{q_id}")
        assert res.status_code == 200
        for c in res.json()["questions"][0]["choices"]:
            assert "is_correct" not in c

    def test_nonexistent_question_returns_404(self, client, seeded_db):
        """存在しない question_id は 404。"""
        res = client.get("/api/v1/questions/99999")
        assert res.status_code == 404

    def test_invalid_id_type_returns_422(self, client, seeded_db):
        """question_id に文字列を渡すと 422。"""
        res = client.get("/api/v1/questions/abc")
        assert res.status_code == 422


class TestGetCategories:
    """GET /api/v1/categories のテスト（DB 不要・config から返す）。"""

    def test_returns_six_categories(self, client):
        """全6カテゴリが返る。"""
        res = client.get("/api/v1/categories")
        assert res.status_code == 200
        data = res.json()
        assert "categories" in data
        assert len(data["categories"]) == 6

    def test_category_names(self, client):
        """6カテゴリの名称がすべて含まれる。"""
        res = client.get("/api/v1/categories")
        names = {c["name"] for c in res.json()["categories"]}
        expected = {
            "テストの基礎",
            "テスト活動とプロセス",
            "静的テスト",
            "テスト技法",
            "テストマネジメント",
            "ツール支援",
        }
        assert names == expected

    def test_category_has_id_and_name(self, client):
        """各カテゴリに id と name が含まれる。"""
        res = client.get("/api/v1/categories")
        for cat in res.json()["categories"]:
            assert "id" in cat
            assert "name" in cat
