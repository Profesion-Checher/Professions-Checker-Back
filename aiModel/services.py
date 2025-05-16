import requests
from dotenv import load_dotenv
import os
load_dotenv()
def get_predicted_salary(job_title,experience, year):
    API_IA_URL = os.getenv("API_IA_URL")
    payload = {
        "job_title": job_title,  # Cambia esto según sea necesario
        "experience_level": experience,
        "work_year": year
    }
    response = requests.post(API_IA_URL, json=payload)
    
    if response.status_code == 200:
        return response.json().get("predicted_salary")
    else:
        return None