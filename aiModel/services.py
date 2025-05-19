import requests
from dotenv import load_dotenv
import os
from professions.models import Profession

load_dotenv()
API_IA_URL = os.getenv("API_IA_URL")

def get_predicted_salary(job_title, experience, year):
    payload = {
        "job_title": job_title,
        "experience_level": experience,
        "work_year": year
    }

    try:
        response = requests.post(f"{API_IA_URL}/predict", json=payload)
        response.raise_for_status()  # Lanza excepción si el status no es 200
        return response.json().get("predicted_salary")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al conectar con API (predict): {e}")
        return {"error": str(e)}
    except ValueError:
        return {"error": "Respuesta no es JSON válido"}

def get_predicted_salary_2(job_title, experience, year):
    payload = {
        "job_title": job_title,
        "experience_level": experience,
        "work_year": year
    }

    try:
        response = requests.post(f"{API_IA_URL}/predict_2", json=payload)
        response.raise_for_status()
        return response.json().get("predicted_salary")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al conectar con API (predict_2): {e}")
        return {"error": str(e)}
    except ValueError:
        return {"error": "Respuesta no es JSON válido"}

def load_data():
    print("Cargando datos desde la API IA...")
    try:
        response = requests.get(f"{API_IA_URL}/send_data")
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list):
            for item in data:
                fields = item["fields"]
                pk = item["pk"]

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
            return {"success": True}
        else:
            print("⚠️ El JSON recibido no es una lista.")
            return {"error": "Respuesta no es una lista"}
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al conectar con API (send_data): {e}")
        return {"error": str(e)}

def load_data_2():
    print("Cargando datos desde la API IA (v2)...")
    try:
        response = requests.get(f"{API_IA_URL}/send_data_2")
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list):
            for item in data:
                fields = item["fields"]
                pk = item["pk"]

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
            return {"success": True}
        else:
            print("⚠️ El JSON recibido no es una lista.")
            return {"error": "Respuesta no es una lista"}
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al conectar con API (send_data_2): {e}")
        return {"error": str(e)}
