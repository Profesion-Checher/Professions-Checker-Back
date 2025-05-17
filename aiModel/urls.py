# aiModel/urls.py
from django.urls import path
from .views import SalaryPredictionView, LoadDataView, LoadData2View, AiHomeView, SalaryPrediction2View

urlpatterns = [
    path('', AiHomeView.as_view()),  # ← Esta es la raíz de /api/ai/
    path("predict_salary/", SalaryPredictionView.as_view()),
    path("predict_salary_2/", SalaryPrediction2View.as_view()),
    path("load_data/", LoadDataView.as_view()),
    path("load_data_2/", LoadData2View.as_view()),
]
