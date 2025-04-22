from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

class RegisterUserView(APIView):
  def post(self, request, *args, **kwargs):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    # Usar el serializer para convertir el objeto 'request.user' a JSON
    serializer = UserSerializer(request.user)
    return Response(serializer.data)