from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render

from .models import *
from .serializers import *

#Login
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            contraseña = serializer.validated_data['contraseña']

            try:
                user = User.objects.get(email=email, contraseña=contraseña)
                return Response({
                    'message': 'Login exitoso',
                    'user_id': user.user_id,
                    'nombres': user.nombres,
                    'apellidos': user.apellidos,
                    'email': user.email,
                }, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Register
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=serializer.validated_data['email']).exists():
                return Response({'error': 'El email ya está registrado'}, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.save()
            return Response({
                'message': 'Usuario registrado exitosamente',
                'user_id': user.user_id,
                'nombres': user.nombres,
                'apellidos': user.apellidos
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Crear Mascota
class MascotaCreateView(generics.CreateAPIView):
    serializer_class = MascotaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Mascota creada exitosamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar Mascotas con user_id en query param
class MascotaListView(generics.ListAPIView):
    serializer_class = MascotaSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Mascota.objects.filter(usuario__user_id=user_id)
        return Mascota.objects.none()

# Update y Delete de Mascota
class MascotaUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    lookup_field = 'mascota_id'

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response({"message": "Mascota actualizada exitosamente"}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Mascota eliminada exitosamente"}, status=status.HTTP_204_NO_CONTENT)

# Crear Cita
class CitaCreateView(generics.CreateAPIView):
    serializer_class = CitaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Cita creada exitosamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar Citas por query param: user_id, mascota_id
class CitaListView(generics.ListAPIView):
    serializer_class = CitaSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        mascota_id = self.request.query_params.get('mascota_id')

        queryset = Cita.objects.all()

        if mascota_id:
            queryset = queryset.filter(mascota__mascota_id=mascota_id)
        if user_id:
            queryset = queryset.filter(mascota__usuario__user_id=user_id)

        return queryset

# Update y Delete de Cita
class CitaUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response({"message": "Cita actualizada exitosamente"}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Cita eliminada exitosamente"}, status=status.HTTP_204_NO_CONTENT)

    

