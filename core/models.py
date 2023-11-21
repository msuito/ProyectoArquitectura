from django.db import models

class Cliente(models.Model):
    nombre_apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_apellido
    
class Medico(models.Model):
    nombre_apellido = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_apellido
    
class CitaMedica(models.Model):
    especialidad = models.CharField(max_length=255)
    medico = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.especialidad} - {self.medico} - {self.fecha} - {self.hora}"