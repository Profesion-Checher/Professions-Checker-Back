from django.test import TestCase
from ..serializers import ProfessionSerializer

class TestProfessionSerializer(TestCase):  
    def test_valid_data(self):
        data = {
            "profession_name": "Desarrollador Backend",
            "current_salary": "5056000.00",  # Asegúrate que sea string para DecimalField
            "future_salaries": [750000, 800000, 850000],
            "companies": ["Tuya S.A."],
            "experience": "SR"
        }
        serializer = ProfessionSerializer(data=data)
        is_valid = serializer.is_valid()
        print(serializer.errors)
        self.assertTrue(is_valid)