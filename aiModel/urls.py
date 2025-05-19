from django.urls import path
from .views import (
    AiHomeView,
    SalaryPredictionView,
    SalaryPrediction2View,
    LoadDataView,
    LoadData2View
)

urlpatterns = [
    path('', AiHomeView.as_view(), name="ai_home"),
    path("predict_salary/", SalaryPredictionView.as_view(), name="predict_salary"),
    path("predict_salary_2/", SalaryPrediction2View.as_view(), name="predict_salary_2"),
    path("load_data/", LoadDataView.as_view(), name="load_data"),
    path("load_data_2/", LoadData2View.as_view(), name="load_data_2"),
]
