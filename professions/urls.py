from django.urls import path
from .views import profession_list_create, profession_detail, ProfessionListApiView

urlpatterns = [
    # path('professions/', profession_list_create, name='profession_list_create'),
    path('professions/<int:id>/', profession_detail, name='profession_detail'),

    path('professions/', ProfessionListApiView.as_view(), name='profession-list'),
]
