from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase


class TestPolls(APITestCase):
    def test_create_question(self):
        question = {
            "question_text": "my first question",
            "pub_date": datetime.now().isoformat(),
        }
        response = self.client.post("/api/v1/polls/questions/", data=question)
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_update_question(self):
        question = {
            "question_text": "my first question",
            "pub_date": datetime.now().isoformat(),
        }

        response = self.client.post("/api/v1/polls/questions/", data=question)
        assert response.status_code == status.HTTP_201_CREATED

        pk = response.data.get("id")
        question["question_text"] = "my new first question text"
        response = self.client.patch(f"/api/v1/polls/questions/{pk}/", data=question)
        assert response.status_code == status.HTTP_200_OK

        assert response.data["question_text"] == question["question_text"]

    def test_create_delete_question(self):
        question = {
            "question_text": "my first question",
            "pub_date": datetime.now().isoformat(),
        }

        response = self.client.post("/api/v1/polls/questions/", data=question)
        assert response.status_code == status.HTTP_201_CREATED

        pk = response.data.get("id")

        response = self.client.delete(f"/api/v1/polls/questions/{pk}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT

        response = self.client.get(f"/api/v1/polls/questions/{pk}/")
        assert response.status_code == status.HTTP_404_NOT_FOUND
