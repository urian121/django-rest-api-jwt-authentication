from django.contrib import admin
from .models import Task # Importando Task de models

# Registrando el modelo Task en el admin
admin.site.register(Task)