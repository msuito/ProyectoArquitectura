from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente,Medico,CitaMedica
from .serializers import ClienteSerializer,MedicoSerializer,CitaMedicaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class CitaMedicaViewSet(viewsets.ModelViewSet):
    queryset = CitaMedica.objects.all()
    serializer_class = CitaMedicaSerializer