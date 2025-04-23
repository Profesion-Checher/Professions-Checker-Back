from django.urls import path
from .views import SalaryPredictionView

urlpatterns = [
    path("predict-salary/", SalaryPredictionView.as_view(), name="predict_salary"),
]
