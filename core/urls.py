from django.urls import path,include
from rest_framework import routers
from core import views

router=routers.DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'medicos', views.MedicoViewSet)
router.register(r'citas', views.CitaMedicaViewSet)
urlpatterns = [
    path('', include(router.urls))
    # Agrega más URLs según sea necesario
]
