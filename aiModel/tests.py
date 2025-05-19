from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class AiViewTests(APITestCase):

    def test_home_view(self):
        url = reverse('ai_home')  # Necesitas registrar el name='ai_home' en urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("message", response.data)

    def test_salary_prediction_view(self):
        url = reverse('predict_salary')
        payload = {
            "job_title": "Data Scientistt",
            "experience_level": "SE",
            "work_year": 2025
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("predicted_salary", response.data)

    def test_salary_prediction_2_view(self):
        url = reverse('predict_salary_2')
        payload = {
            "job_title": "Machine Learning Engineer",
            "experience_level": "MI",
            "work_year": 2025
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("predicted_salary", response.data)

    def test_load_data_view(self):
        url = reverse('load_data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Data loaded successfully")

    def test_load_data_2_view(self):
        url = reverse('load_data_2')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Data2 loaded successfully")
