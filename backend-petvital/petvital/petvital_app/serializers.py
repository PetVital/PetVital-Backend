from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    contraseña = serializers.CharField(max_length=20)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nombres', 'apellidos', 'email', 'contraseña']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'nombres', 'apellidos', 'email']

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'nombres', 'apellidos', 'email', 'fecha_registro']


class MascotaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'
        depth = 1

class CitaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'
        depth = 1

class RevisionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revision
        fields = '__all__'

class RevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revision
        fields = '__all__'
        depth = 1

class MensajeIAInputSerializer(serializers.Serializer):
    currentMessage = serializers.CharField()
    previousMessages = serializers.ListField(
        child=serializers.DictField(), required=False
    )
    memoryBank = serializers.ListField(
        child=serializers.DictField(), required=False
    )
