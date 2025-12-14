from django.contrib import admin
from django.urls import path
from core import views

from rest_framework.authtoken.views import obtain_auth_token

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),

    # Token DRF
    path('api/token/', obtain_auth_token, name='api_token_auth'),

    # Endpoints API
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

    # ✅ drf-spectacular schema + Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
