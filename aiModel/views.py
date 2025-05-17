from rest_framework.views import APIView
from rest_framework.response import Response
from .services import get_predicted_salary, load_data

class SalaryPredictionView(APIView):
    def post(self, request):
        job_title = request.data.get("job_title")
        experience = request.data.get("experience_level")
        work_year = request.data.get("work_year")
        print(f"Received data: job_title={job_title}, experience={experience}, year={work_year}")
        predicted_salary =  get_predicted_salary(job_title,experience, work_year)

        return Response({
            "job_title": job_title,
            "experience": experience,
            "year": work_year,
            "predicted_salary": predicted_salary
        })
    def get(self, request):
        load_data()
        return Response({"message": "Data loaded successfully"})
        