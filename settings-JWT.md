# Configurar JWT con djangorestframework-simplejwt

## 1. Instalar djangorestframework-simplejwt
```bash
pip install djangorestframework-simplejwt
```

## 2. Agregar a INSTALLED_APPS (settings.py) - OPCIONAL
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'rest_framework_simplejwt',  # Opcional (solo para traducciones)
    'myapp',
]
```

## 3. Importar timedelta en settings.py
```python
from datetime import timedelta
```

## 4. Configurar REST_FRAMEWORK (settings.py)
```python
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
```

## 5. Configurar SIMPLE_JWT (settings.py)
```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
```

## 6. Agregar rutas JWT (myproject/urls.py)
```python
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    
    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```

## 7. Crear usuario de prueba (si no existe)
```bash
python manage.py createsuperuser
```

## 8. Actualizar requirements.txt
```bash
pip freeze > requirements.txt
```

## 9. Ejecutar servidor
```bash
python manage.py runserver
```

## 10. Probar JWT con cURL o Postman

### Obtener tokens (Login)
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "tu_usuario", "password": "tu_contraseña"}'
```

**Respuesta:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Refrescar token (cuando expire el access)
```bash
curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "tu_refresh_token"}'
```

### Verificar token
```bash
curl -X POST http://127.0.0.1:8000/api/token/verify/ \
  -H "Content-Type: application/json" \
  -d '{"token": "tu_access_token"}'
```

### Acceder a endpoint protegido
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Bearer tu_access_token"
```

## 11. Configurar permisos en views (OPCIONAL)

Si quieres que algunos endpoints NO requieran autenticación:

```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Requiere autenticación
    
    # O para permitir acceso público a ciertos métodos:
    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]
```

## 12. Probar en Swagger UI
1. Ve a `http://127.0.0.1:8000/api/docs/`
2. Haz clic en **Authorize** (candado verde)
3. Obtén un token en `/api/token/`
4. Ingresa: `Bearer tu_access_token`
5. Prueba los endpoints protegidos

Documentación extra:
- `https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html`