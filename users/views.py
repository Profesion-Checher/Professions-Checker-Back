from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from professions.models import Profession
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

# users/views.py
class AddInterestedProfessionView(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request):
    profession_id = request.data.get('profession_id')
    if not profession_id:
      return Response({'error': 'Se requiere el ID de la profesión'}, status=status.HTTP_400_BAD_REQUEST)

    try:
      profession = Profession.objects.get(id=profession_id)
    except Profession.DoesNotExist:
      return Response({'error': 'Profesión no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    request.user.interested_professions.add(profession)
    return Response({'message': f'Te interesa la profesión {profession.profession_name}'}, status=status.HTTP_200_OK)
