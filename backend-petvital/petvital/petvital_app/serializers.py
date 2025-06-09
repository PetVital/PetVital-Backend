from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    contraseña = serializers.CharField(max_length=20)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nombres', 'apellidos', 'email', 'contraseña']

class MascotaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'
        depth = 1

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'
        depth = 1