from rest_framework import serializers
from .models import Client
from professions.models import Profession
from professions.serializers import ProfessionSerializer

class UserSerializer(serializers.ModelSerializer):
  # Lectura (devuelve los detalles de cada profesión)
  interested_professions = ProfessionSerializer(many=True, read_only=True)

  # Escritura (permite enviar solo los IDs de profesiones)
  interested_professions_ids = serializers.PrimaryKeyRelatedField(
    queryset=Profession.objects.all(),
    many=True,
    write_only=True,
    required=False
  )

  class Meta:
    model = Client
    fields = [
      'first_name',
      'last_name',
      'email',
      'password',
      'company',
      'profession',
      'salary',
      'interested_professions',      # Solo lectura
      'interested_professions_ids'   # Solo escritura
    ]
    extra_kwargs = {
      'password': {'write_only': True}
    }

  def create(self, validated_data):
    professions = validated_data.pop('interested_professions_ids', [])
    user = Client.objects.create_user(
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      company=validated_data.get('company'),
      profession=validated_data.get('profession'),
      salary=validated_data.get('salary'),
      password=validated_data['password'],
    )
    if professions:
        user.interested_professions.set(professions)
    return user

  def update(self, instance, validated_data):
    professions = validated_data.pop('interested_professions_ids', None)

    for attr, value in validated_data.items():
      setattr(instance, attr, value)

    if professions is not None:
      instance.interested_professions.set(professions)

    instance.save()
    return instance
