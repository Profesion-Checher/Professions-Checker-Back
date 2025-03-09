from django.urls import path
from .views import profession_list_create, profession_detail

urlpatterns = [
    path('api/professions/', profession_list_create, name='profession_list_create'),
    path('api/professions/<int:id>/', profession_detail, name='profession_detail'),
]
