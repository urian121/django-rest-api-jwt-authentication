from rest_framework import viewsets # Importando viewsets de rest_framework
from .models import Task # Importando Task de models
from .serializers import TaskSerializer # Importando TaskSerializer de serializers

# TaskViewSet: Vista para el modelo Task
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    # Serializador para el modelo Task
    serializer_class = TaskSerializer
