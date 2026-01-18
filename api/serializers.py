from rest_framework import serializers # Importando serializers de rest_framework
from .models import Task # Importando Task de models

# TaskSerializer: Serializador para el modelo Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'