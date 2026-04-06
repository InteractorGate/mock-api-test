from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class RegisterSerializer(serializers.ModelSerializer):
    # Definimos explícitamente los campos que no están en el modelo User original
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(write_only=True) # Para recibirlo desde el JSON

    class Meta:
        model = User
        # Agregamos 'username' porque Django lo exige obligatoriamente
        fields = ('username', 'email', 'password', 'name', 'last_name')

    def create(self, validated_data):
        # Creamos el usuario base usando 'first_name' en lugar de 'name'
        user = User.objects.create_user(
            username=validated_data['username'], # Obligatorio en Django
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('name', ''), # 'name' se mapea a 'first_name'
            last_name=validated_data.get('last_name', '')
        )

        # Se crea el UserProfile vinculado para tu arquitectura relacional
        UserProfile.objects.create(
            name=user.first_name,
            last_name=user.last_name,
            email=user.email
        )
        return user