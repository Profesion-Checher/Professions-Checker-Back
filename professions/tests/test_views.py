from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import Profession

class ProfessionAPITestCase(APITestCase):
    def setUp(self):
        self.profession = Profession.objects.create(
            profession_name="Desarrollador Backend",
            current_salary=8000000.00,
            future_salaries=[9000000, 10000000],
            companies=["Arquitectura S.A."],
            experience="SR"
        )

    def test_list_professions(self):
        url = reverse('profession-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
