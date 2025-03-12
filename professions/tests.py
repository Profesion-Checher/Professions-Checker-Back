from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profession

class ProfessionAPITestCase(APITestCase):
    def setUp(self):
        # Crear algunos registros de ejemplo
        Profession.objects.create(
            profession_name="Ingeniero de Software",
            current_salary=5000000.00,
            future_salaries=[7000000.00, 7500000.00],
            companies=["Google", "Microsoft"],
            experience="JR"
        )

        Profession.objects.create(
            profession_name="Data Scientist",
            current_salary=6000000.00,
            future_salaries=[8000000.00, 8500000.00],
            companies=["Facebook", "Amazon"],
            experience="SR"
        )

    def test_get_professions_list(self):
        # Hacer una petición GET al endpoint
        response = self.client.get("/api/professions/")

        # Validar que la respuesta sea 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Validar que se devuelvan dos objetos
        self.assertEqual(len(response.data), 2)

        # Validar que los datos del primer objeto sean correctos
        self.assertEqual(response.data[0]["profession_name"], "Ingeniero de Software")
        self.assertEqual(response.data[0]["current_salary"], "5000000.00")
        self.assertEqual(response.data[0]["future_salaries"], [7000000.00, 7500000.00])
        self.assertEqual(response.data[0]["companies"], ["Google", "Microsoft"])
        self.assertEqual(response.data[0]["experience"], "JR")

    # def test_create_profession(self):
    #     # Crear una nueva profesión
    #     data = {
    #         "profession_name": "DevOps Engineer",
    #         "current_salary": 7000000.00,
    #         "future_salaries": [9000000.00, 9500000.00],
    #         "companies": ["AWS", "Azure"],
    #         "experience": "MD"
    #     }
    #     response = self.client.post("/api/professions/", data, format="json")

    #     # Validar que la creación sea exitosa
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Profession.objects.count(), 3)
    #     self.assertEqual(response.data["profession_name"], "DevOps Engineer")

    def test_get_profession_detail(self):
        profession = Profession.objects.first()

        # Obtener detalles de una profesión específica
        response = self.client.get(f"/api/professions/{profession.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["profession_name"], "Ingeniero de Software")

    def test_update_profession(self):
        profession = Profession.objects.first()

        # Actualizar una profesión
        data = {
            "profession_name": "Senior Software Engineer",
            "current_salary": 5500000.00,
            "future_salaries": [8000000.00],
            "companies": ["Google"],
            "experience": "SR"
        }
        response = self.client.put(f"/api/professions/{profession.id}/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        profession.refresh_from_db()
        self.assertEqual(profession.profession_name, "Senior Software Engineer")

    def test_delete_profession(self):
        profession = Profession.objects.first()

        # Eliminar una profesión
        response = self.client.delete(f"/api/professions/{profession.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profession.objects.count(), 1)

    # def test_create_duplicate_profession(self):
    #     # Intentar crear una profesión duplicada
    #     data = {
    #         "profession_name": "Ingeniero de Software",
    #         "current_salary": 7000000.00,
    #         "future_salaries": [9000000.00],
    #         "companies": ["AWS"],
    #         "experience": "MD"
    #     }
    #     response = self.client.post("/api/professions/", data, format="json")

    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertIn("profession_name", response.data)
