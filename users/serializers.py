from rest_framework import serializers
from .models import Client  # Asegúrate de importar tu modelo

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Client
    fields = ['first_name', 'last_name', 'email', 'password', 'company', 'profession', 'salary']
    extra_kwargs = {
      'password': {'write_only': True}  # La contraseña no será leída en las respuestas
    }

  def create(self, validated_data):
    user = Client.objects.create_user(
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      company=validated_data.get('company'),
      profession=validated_data.get('profession'),
      salary=validated_data.get('salary')
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
