from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import get_predicted_salary, load_data, load_data_2, get_predicted_salary_2

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

        if not job_title or not experience or not work_year:
            return Response({"error": "Faltan campos obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        print(f"Received data: job_title={job_title}, experience={experience}, year={work_year}")
        result = get_predicted_salary(job_title, experience, work_year)

        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "job_title": job_title,
            "experience": experience,
            "year": work_year,
            "predicted_salary": result
        })


class SalaryPrediction2View(APIView):
    def post(self, request):
        job_title = request.data.get("job_title")
        experience = request.data.get("experience_level")
        work_year = request.data.get("work_year")

        if not job_title or not experience or not work_year:
            return Response({"error": "Faltan campos obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        print(f"Received data in SalaryPrediction2View: job_title={job_title}, experience={experience}, year={work_year}")
        result = get_predicted_salary_2(job_title, experience, work_year)

        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "job_title": job_title,
            "experience": experience,
            "year": work_year,
            "predicted_salary": result
        })


class LoadDataView(APIView):
    def get(self, request):
        result = load_data()

        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "Data loaded successfully"})


class LoadData2View(APIView):
    def get(self, request):
        result = load_data_2()

        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "Data2 loaded successfully"})
