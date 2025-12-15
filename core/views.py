# core/views.py
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from drf_spectacular.utils import extend_schema

from .models import (
    Trabajador, Asistencia, Accidente,
    EficienciaTrabajador, DesempenoTrabajador, SueldoTrabajador
)
from .serializers import (
    TrabajadorSerializer, AsistenciaSerializer, AccidenteSerializer,
    EficienciaTrabajadorSerializer, DesempenoTrabajadorSerializer, SueldoTrabajadorSerializer
)

# ===================== HOME =====================
def home(request):
    return JsonResponse({
        "mensaje": "API Optimización Logística activa",
        "endpoints": [
            "/api/trabajadores/",
            "/api/asistencias/",
            "/api/accidentes/",
            "/api/eficiencias/",
            "/api/desempenos/",
            "/api/sueldos/",
            "/api/token/"
        ]
    })


# ===================== TRABAJADORES =====================

@extend_schema(
    request=TrabajadorSerializer,
    responses={200: TrabajadorSerializer(many=True), 201: TrabajadorSerializer}
)
@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def trabajador_list(request):

    if request.method == "GET":
        trabajadores = Trabajador.objects.all()
        serializer = TrabajadorSerializer(trabajadores, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = TrabajadorSerializer(data=request.data)

        # ✅ AQUÍ ESTÁ EL CAMBIO CLAVE
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(
    request=TrabajadorSerializer,
    responses={200: TrabajadorSerializer, 204: None}
)
@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def trabajador_detail(request, pk):

    try:
        trabajador = Trabajador.objects.get(pk=pk)
    except Trabajador.DoesNotExist:
        return Response({"detail": "Trabajador no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TrabajadorSerializer(trabajador)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = TrabajadorSerializer(trabajador, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == "DELETE":
        trabajador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ===================== ASISTENCIAS =====================

@extend_schema(
    request=AsistenciaSerializer,
    responses={200: AsistenciaSerializer(many=True), 201: AsistenciaSerializer}
)
@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def asistencia_list(request):

    if request.method == "GET":
        asistencias = Asistencia.objects.all()
        serializer = AsistenciaSerializer(asistencias, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = AsistenciaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(
    request=AsistenciaSerializer,
    responses={200: AsistenciaSerializer, 204: None}
)
@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def asistencia_detail(request, pk):

    try:
        asistencia = Asistencia.objects.get(pk=pk)
    except Asistencia.DoesNotExist:
        return Response({"detail": "Asistencia no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AsistenciaSerializer(asistencia)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = AsistenciaSerializer(asistencia, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == "DELETE":
        asistencia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ===================== ACCIDENTES =====================

@extend_schema(
    request=AccidenteSerializer,
    responses={200: AccidenteSerializer(many=True), 201: AccidenteSerializer}
)
@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def accidente_list(request):

    if request.method == "GET":
        accidentes = Accidente.objects.all()
        serializer = AccidenteSerializer(accidentes, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = AccidenteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(
    request=AccidenteSerializer,
    responses={200: AccidenteSerializer, 204: None}
)
@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def accidente_detail(request, pk):

    try:
        accidente = Accidente.objects.get(pk=pk)
    except Accidente.DoesNotExist:
        return Response({"detail": "Accidente no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AccidenteSerializer(accidente)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = AccidenteSerializer(accidente, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == "DELETE":
        accidente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ===================== EFICIENCIAS =====================

@extend_schema(
    request=EficienciaTrabajadorSerializer,
    responses={200: EficienciaTrabajadorSerializer(many=True), 201: EficienciaTrabajadorSerializer}
)
@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def eficiencia_list(request):

    if request.method == "GET":
        data = EficienciaTrabajador.objects.all()
        serializer = EficienciaTrabajadorSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = EficienciaTrabajadorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(
    request=EficienciaTrabajadorSerializer,
    responses={200: EficienciaTrabajadorSerializer, 204: None}
)
@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def eficiencia_detail(request, pk):

    try:
        obj = EficienciaTrabajador.objects.get(pk=pk)
    except EficienciaTrabajador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(EficienciaTrabajadorSerializer(obj).data)

    if request.method == "PUT":
        serializer = EficienciaTrabajadorSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == "DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ===================== DESEMPEÑOS =====================

@extend_schema(
    request=DesempenoTrabajadorSerializer,
    responses={200: DesempenoTrabajadorSerializer(many=True), 201: DesempenoTrabajadorSerializer}
)
@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def desempeno_list(request):

    if request.method == "GET":
        data = DesempenoTrabajador.objects.all()
        return Response(DesempenoTrabajadorSerializer(data, many=True).data)

    if request.method == "POST":
        serializer = DesempenoTrabajadorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(
    request=DesempenoTrabajadorSerializer,
    responses={200: DesempenoTrabajadorSerializer, 204: None}
)
@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def desempeno_detail(request, pk):

    try:
        obj = DesempenoTrabajador.objects.get(pk=pk)
    except DesempenoTrabajador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(DesempenoTrabajadorSerializer(obj).data)

    if request.method == "PUT":
        serializer = DesempenoTrabajadorSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == "DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ===================== SUELDOS =====================

@extend_schema(
    request=SueldoTrabajadorSerializer,
    responses={200: SueldoTrabajadorSerializer(many=True), 201: SueldoTrabajadorSerializer}
)
@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def sueldo_list(request):

    if request.method == "GET":
        data = SueldoTrabajador.objects.all()
        return Response(SueldoTrabajadorSerializer(data, many=True).data)

    if request.method == "POST":
        serializer = SueldoTrabajadorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(
    request=SueldoTrabajadorSerializer,
    responses={200: SueldoTrabajadorSerializer, 204: None}
)
@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def sueldo_detail(request, pk):

    try:
        obj = SueldoTrabajador.objects.get(pk=pk)
    except SueldoTrabajador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(SueldoTrabajadorSerializer(obj).data)

    if request.method == "PUT":
        serializer = SueldoTrabajadorSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == "DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
