from django.urls import path, include
# Router para el modelo Task
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet # Importando TaskViewSet de views

# TaskViewSet: Vista para el modelo Task
router = DefaultRouter()
router.register(r'tasks', TaskViewSet) # Registro de TaskViewSet en el router

# urlpatterns: Patrones de URL para la API
urlpatterns = [
    path('', include(router.urls)),
]