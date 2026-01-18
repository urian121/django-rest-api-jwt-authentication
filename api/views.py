from rest_framework import viewsets

# Importando AllowAny y IsAuthenticated para permisos de acceso
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Task # Importando Task de models
from .serializers import TaskSerializer # Importando TaskSerializer de serializers

# TaskViewSet: Vista para el modelo Task
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    # Serializador para el modelo Task
    serializer_class = TaskSerializer
    
    # Permitir acceso público a la lista de tareas (AllowAny), sobreescribiendo el método get_permissions
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]
