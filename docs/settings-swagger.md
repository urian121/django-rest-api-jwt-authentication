# Configurar drf-spectacular (Swagger/OpenAPI)

## 1. Instalar drf-spectacular
```bash
pip install drf-spectacular
```

## 2. Agregar a INSTALLED_APPS (settings.py)
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'drf_spectacular',  # Agregar
    'myapp',
]
```

## 3. Configurar REST_FRAMEWORK (settings.py)
```python
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

## 4. Configurar SPECTACULAR_SETTINGS (settings.py)
```python
SPECTACULAR_SETTINGS = {
    'TITLE': 'My API',
    'DESCRIPTION': 'API documentation',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
```

## 5. Agregar URLs (myproject/urls.py)
```python
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    
    # Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # ReDoc UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```

## 7. Ejecutar servidor
```bash
python manage.py runserver
```

## 8. Acceder a la documentación
- **Swagger UI**: `http://127.0.0.1:8000/api/docs/`
- **ReDoc**: `http://127.0.0.1:8000/api/redoc/`
- **Schema JSON**: `http://127.0.0.1:8000/api/schema/`

Documentación extra:
- `https://pypi.org/project/drf-spectacular/`