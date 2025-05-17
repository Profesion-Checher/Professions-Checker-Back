import requests
from dotenv import load_dotenv
import os
from professions.models import Profession
load_dotenv()
API_IA_URL = os.getenv("API_IA_URL")
def get_predicted_salary(job_title,experience, year):
    
    payload = {
        "job_title": job_title,  # Cambia esto según sea necesario
        "experience_level": experience,
        "work_year": year
    }
    response = requests.post(API_IA_URL+"/predict", json=payload)
    
    if response.status_code == 200:
        return response.json().get("predicted_salary")
    else:
        return None
    
def load_data():
    response = requests.get(API_IA_URL + "/send_data")

    if response.status_code == 200:
        data = response.json()

        if isinstance(data, list):
            for item in data:
                fields = item["fields"]
                pk = item["pk"]

                # Crear o actualizar el objeto
                Profession.objects.update_or_create(
                    pk=pk,
                    defaults={
                        "profession_name": fields["profession_name"],
                        "current_salary": fields["current_salary"],
                        "future_salaries": fields["future_salaries"],
                        "companies": fields["companies"],
                        "experience": fields["experience"],
                    }
                )
            print("✅ Datos cargados exitosamente.")
        else:
            print("⚠️ El JSON recibido no es una lista.")
    else:
        print(f"❌ Error al cargar datos: {response.status_code}")