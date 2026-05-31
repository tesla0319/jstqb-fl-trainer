"""POST /api/v1/answers のAPIテスト（JSTQB FL 版: 単一選択）。"""


class TestSubmitAnswer:

    # ---- 正常系 ----

    def test_correct_answer_returns_true(self, client, seeded_db):
        """正解の choice_id を送信すると is_correct=True が返る。"""
        res = client.post("/api/v1/answers", json={
            "question_id": seeded_db["q1_id"],
            "choice_id":   seeded_db["q1_correct_choice_id"],
        })
        assert res.status_code == 200
        assert res.json()["is_correct"] is True

    def test_incorrect_answer_returns_false(self, client, seeded_db):
        """不正解の choice_id を送信すると is_correct=False が返る。"""
        res = client.post("/api/v1/answers", json={
            "question_id": seeded_db["q1_id"],
            "choice_id":   seeded_db["q1_incorrect_choice_id"],
        })
        assert res.status_code == 200
        assert res.json()["is_correct"] is False

    def test_response_contains_required_fields(self, client, seeded_db):
        """レスポンスに必須フィールドが含まれる。"""
        res = client.post("/api/v1/answers", json={
            "question_id": seeded_db["q1_id"],
            "choice_id":   seeded_db["q1_correct_choice_id"],
        })
        data = res.json()
        assert "is_correct" in data
        assert "correct_choice_id" in data
        assert "correct_choice_text" in data
        assert "selected_choice_id" in data
        assert "selected_choice_text" in data
        assert "explanation" in data

    def test_selected_choice_matches_sent_choice(self, client, seeded_db):
        """selected_choice_id がリクエストの choice_id と一致する。"""
        cid = seeded_db["q1_incorrect_choice_id"]
        res = client.post("/api/v1/answers", json={
            "question_id": seeded_db["q1_id"],
            "choice_id":   cid,
        })
        assert res.status_code == 200
        assert res.json()["selected_choice_id"] == cid

    # ---- 異常系: 404 ----

    def test_nonexistent_question_id_returns_404(self, client, seeded_db):
        """存在しない question_id は 404。"""
        res = client.post("/api/v1/answers", json={
            "question_id": 99999,
            "choice_id":   seeded_db["q1_correct_choice_id"],
        })
        assert res.status_code == 404

    def test_nonexistent_choice_id_returns_404(self, client, seeded_db):
        """存在しない choice_id は 404。"""
        res = client.post("/api/v1/answers", json={
            "question_id": seeded_db["q1_id"],
            "choice_id":   99999,
        })
        assert res.status_code == 404

    # ---- 異常系: 400 ----

    def test_cross_question_choice_returns_400(self, client, seeded_db):
        """他の問題に属する choice_id を送ると 400。"""
        res = client.post("/api/v1/answers", json={
            "question_id": seeded_db["q1_id"],
            "choice_id":   seeded_db["q2_choice_for_cross_test"],
        })
        assert res.status_code == 400
        assert "choice_id does not belong" in res.json()["detail"]

    # ---- 異常系: 422 ----

    def test_missing_question_id_returns_422(self, client, seeded_db):
        """question_id を省略すると 422。"""
        res = client.post("/api/v1/answers", json={
            "choice_id": seeded_db["q1_correct_choice_id"],
        })
        assert res.status_code == 422

    def test_missing_choice_id_returns_422(self, client, seeded_db):
        """choice_id を省略すると 422。"""
        res = client.post("/api/v1/answers", json={
            "question_id": seeded_db["q1_id"],
        })
        assert res.status_code == 422

    def test_string_question_id_returns_422(self, client, seeded_db):
        """question_id に文字列を渡すと 422。"""
        res = client.post("/api/v1/answers", json={
            "question_id": "abc",
            "choice_id":   seeded_db["q1_correct_choice_id"],
        })
        assert res.status_code == 422

    def test_string_choice_id_returns_422(self, client, seeded_db):
        """choice_id に文字列を渡すと 422。"""
        res = client.post("/api/v1/answers", json={
            "question_id": seeded_db["q1_id"],
            "choice_id":   "xyz",
        })
        assert res.status_code == 422
