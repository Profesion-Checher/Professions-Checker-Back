from django.test import TestCase
from professions.models import Profession

class ProfessionModelTest(TestCase):
    def test_create_profession(self):
        data = {
            "profession_name": "Desarrollador Backend",
            "current_salary": 5056000.00,
            "future_salaries": [750000, 800000, 850000],
            "companies": ["Tuya S.A."],
            "experience": "SR"
        }
        profession = Profession.objects.create(**data)
        self.assertEqual(profession.profession_name, "Desarrollador Backend")
        self.assertEqual(profession.current_salary, 5056000.00)
        self.assertEqual(profession.future_salaries, [750000, 800000, 850000])
        self.assertEqual(profession.companies, ["Tuya S.A."])
        self.assertEqual(profession.experience, "SR")
