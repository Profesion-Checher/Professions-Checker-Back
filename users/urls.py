from django.urls import path
from .views import RegisterUserView, UserProfileView, AddInterestedProfessionView
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)

urlpatterns = [
  path('register/', RegisterUserView.as_view(), name='register'),
  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('profile/', UserProfileView.as_view(), name='user-profile'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('profile/interested/', AddInterestedProfessionView.as_view(), name='user-profile-interested'),
]
