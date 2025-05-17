from rest_framework.views import APIView
from rest_framework.response import Response
from .services import get_predicted_salary, load_data, load_data_2, get_predicted_salary_2

# views.py
class AiHomeView(APIView):
    def get(self, request):
        return Response({
            "message": "AI API is up!",
            "endpoints": [
                "/api/ai/predict_salary/",
                "/api/ai/predict_salary_2/",
                "/api/ai/load_data/",
                "/api/ai/load_data_2/"
            ]
        })
class SalaryPredictionView(APIView):
    def post(self, request):
        job_title = request.data.get("job_title")
        experience = request.data.get("experience_level")
        work_year = request.data.get("work_year")
        print(f"Received data: job_title={job_title}, experience={experience}, year={work_year}")
        predicted_salary = get_predicted_salary(job_title, experience, work_year)

        return Response({
            "job_title": job_title,
            "experience": experience,
            "year": work_year,
            "predicted_salary": predicted_salary
        })
class SalaryPrediction2View(APIView):
    def post(self, request):
        print("Received data in SalaryPrediction2View")
        job_title = request.data.get("job_title")
        experience = request.data.get("experience_level")
        work_year = request.data.get("work_year")
        print(f"Received data: job_title={job_title}, experience={experience}, year={work_year}")
        predicted_salary = get_predicted_salary_2(job_title, experience, work_year)

        return Response({
            "job_title": job_title,
            "experience": experience,
            "year": work_year,
            "predicted_salary": predicted_salary
        })

class LoadDataView(APIView):
    def get(self, request):
        load_data()
        return Response({"message": "Data loaded successfully"})

class LoadData2View(APIView):
    def get(self, request):
        load_data_2()
        return Response({"message": "Data2 loaded successfully"})

        