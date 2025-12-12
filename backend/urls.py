"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from core import views
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Optimización Logística",
        default_version='v1',
        description="API para gestionar Trabajadores, Asistencias, Accidentes, Eficiencia, Desempeño y Sueldos.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="nicolasmenevillegas@gmail.com"),
        license=openapi.License(name="Uso académico"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/trabajadores/', views.trabajador_list, name='trabajador_list'),
    path('api/trabajadores/<int:pk>/', views.trabajador_detail, name='trabajador_detail'),
    path('api/asistencias/', views.asistencia_list, name='asistencia_list'),
    path('api/asistencias/<int:pk>/', views.asistencia_detail, name='asistencia_detail'),
    path('api/accidentes/', views.accidente_list, name='accidente_list'),
    path('api/accidentes/<int:pk>/', views.accidente_detail, name='accidente_detail'),
    path('api/eficiencias/', views.eficiencia_list, name='eficiencia_list'),
    path('api/eficiencias/<int:pk>/', views.eficiencia_detail, name='eficiencia_detail'),
    path('api/desempenos/', views.desempeno_list, name='desempeno_list'),
    path('api/desempenos/<int:pk>/', views.desempeno_detail, name='desempeno_detail'),
    path('api/sueldos/', views.sueldo_list, name='sueldo_list'),
    path('api/sueldos/<int:pk>/', views.sueldo_detail, name='sueldo_detail'),

    # 👉 Swagger UI
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),

    # 👉 ReDoc (documentación alternativa)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),

    path('api/schema/', schema_view.without_ui(cache_timeout=0),
     name='api-schema-json'),
    path('api/schema/swagger-ui/', schema_view.with_ui('swagger', cache_timeout=0),
     name='api-schema-swagger-ui'),
    path('api/schema/redoc/', schema_view.with_ui('redoc', cache_timeout=0),
     name='api-schema-redoc'),     
]
