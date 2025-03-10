from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Profession
from .serializers import ProfessionSerializer

@api_view(['GET', 'POST'])
def profession_list_create(request):
    if request.method == 'GET':
        professions = Profession.objects.all()
        serializer = ProfessionSerializer(professions, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProfessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def profession_detail(request, id):
    profession = Profession.objects.filter(id=id).first()
    if not profession:
        return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfessionSerializer(profession)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProfessionSerializer(profession, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        profession.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
