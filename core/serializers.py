from rest_framework import serializers
from .models import Cliente,Medico,CitaMedica

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre_apellido', 'fecha_nacimiento', 'correo', 'contraseña')

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('id', 'nombre_apellido', 'especialidad', 'correo', 'contraseña', 'sueldo')

class CitaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitaMedica
        fields = ('id', 'especialidad', 'medico', 'fecha', 'hora', 'valor')