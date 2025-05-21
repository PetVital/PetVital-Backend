from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=20)

    def __str__(self):
        return self.nombres

class Mascota(models.Model):
    mascota_id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    raza = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso = models.IntegerField()

class Cita(models.Model):
    tipo_recordatorio = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    nota = models.CharField(max_length=200)
    recordatorio = models.CharField(max_length=100)
    
    usuario = models.ForeignKey(Mascota, on_delete=models.CASCADE)