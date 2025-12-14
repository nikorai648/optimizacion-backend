from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from drf_yasg.utils import swagger_auto_schema

from .models import (
    Trabajador, Asistencia, Accidente,
    EficienciaTrabajador, DesempenoTrabajador, SueldoTrabajador
)
from .serializers import (
    TrabajadorSerializer, AsistenciaSerializer, AccidenteSerializer,
    EficienciaTrabajadorSerializer, DesempenoTrabajadorSerializer, SueldoTrabajadorSerializer
)


# -----------------------
# TRABAJADORES
# -----------------------
@swagger_auto_schema(
    method='get',
    responses={200: TrabajadorSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    request_body=TrabajadorSerializer,
    responses={201: TrabajadorSerializer}
)
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def trabajador_list(request):
    """
    GET  /api/trabajadores/  → lista todos
    POST /api/trabajadores/  → crea uno nuevo
    """
    if request.method == 'GET':
        trabajadores = Trabajador.objects.all()
        serializer = TrabajadorSerializer(trabajadores, many=True)
        return Response(serializer.data)

    serializer = TrabajadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={200: TrabajadorSerializer}
)
@swagger_auto_schema(
    method='put',
    request_body=TrabajadorSerializer,
    responses={200: TrabajadorSerializer}
)
@swagger_auto_schema(
    method='delete',
    responses={204: 'No Content'}
)
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def trabajador_detail(request, pk):
    """
    GET    /api/trabajadores/<pk>/ → detalle
    PUT    /api/trabajadores/<pk>/ → actualizar
    DELETE /api/trabajadores/<pk>/ → borrar
    """
    try:
        trabajador = Trabajador.objects.get(pk=pk)
    except Trabajador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrabajadorSerializer(trabajador)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TrabajadorSerializer(trabajador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    trabajador.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# -----------------------
# ASISTENCIAS
# -----------------------
@swagger_auto_schema(
    method='get',
    responses={200: AsistenciaSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    request_body=AsistenciaSerializer,
    responses={201: AsistenciaSerializer}
)
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def asistencia_list(request):
    """
    GET  /api/asistencias/ → lista todas
    POST /api/asistencias/ → crea una nueva
    """
    if request.method == 'GET':
        asistencias = Asistencia.objects.all()
        serializer = AsistenciaSerializer(asistencias, many=True)
        return Response(serializer.data)

    serializer = AsistenciaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={200: AsistenciaSerializer}
)
@swagger_auto_schema(
    method='put',
    request_body=AsistenciaSerializer,
    responses={200: AsistenciaSerializer}
)
@swagger_auto_schema(
    method='delete',
    responses={204: 'No Content'}
)
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def asistencia_detail(request, pk):
    """
    GET    /api/asistencias/<pk>/ → detalle
    PUT    /api/asistencias/<pk>/ → actualizar
    DELETE /api/asistencias/<pk>/ → borrar
    """
    try:
        asistencia = Asistencia.objects.get(pk=pk)
    except Asistencia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AsistenciaSerializer(asistencia)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = AsistenciaSerializer(asistencia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    asistencia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# -----------------------
# ACCIDENTES
# -----------------------
@swagger_auto_schema(
    method='get',
    responses={200: AccidenteSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    request_body=AccidenteSerializer,
    responses={201: AccidenteSerializer}
)
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def accidente_list(request):
    """
    GET  /api/accidentes/ → lista todos
    POST /api/accidentes/ → crea uno nuevo
    """
    if request.method == 'GET':
        accidentes = Accidente.objects.all()
        serializer = AccidenteSerializer(accidentes, many=True)
        return Response(serializer.data)

    serializer = AccidenteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={200: AccidenteSerializer}
)
@swagger_auto_schema(
    method='put',
    request_body=AccidenteSerializer,
    responses={200: AccidenteSerializer}
)
@swagger_auto_schema(
    method='delete',
    responses={204: 'No Content'}
)
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def accidente_detail(request, pk):
    """
    GET    /api/accidentes/<pk>/ → detalle
    PUT    /api/accidentes/<pk>/ → actualizar
    DELETE /api/accidentes/<pk>/ → borrar
    """
    try:
        accidente = Accidente.objects.get(pk=pk)
    except Accidente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccidenteSerializer(accidente)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = AccidenteSerializer(accidente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    accidente.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# -----------------------
# EFICIENCIAS
# -----------------------
@swagger_auto_schema(
    method='get',
    responses={200: EficienciaTrabajadorSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    request_body=EficienciaTrabajadorSerializer,
    responses={201: EficienciaTrabajadorSerializer}
)
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def eficiencia_list(request):
    if request.method == 'GET':
        eficiencias = EficienciaTrabajador.objects.all()
        serializer = EficienciaTrabajadorSerializer(eficiencias, many=True)
        return Response(serializer.data)

    serializer = EficienciaTrabajadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', responses={200: EficienciaTrabajadorSerializer})
@swagger_auto_schema(method='put', request_body=EficienciaTrabajadorSerializer, responses={200: EficienciaTrabajadorSerializer})
@swagger_auto_schema(method='delete', responses={204: 'No Content'})
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def eficiencia_detail(request, pk):
    try:
        eficiencia = EficienciaTrabajador.objects.get(pk=pk)
    except EficienciaTrabajador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EficienciaTrabajadorSerializer(eficiencia)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = EficienciaTrabajadorSerializer(eficiencia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    eficiencia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# -----------------------
# DESEMPEÑOS
# -----------------------
@swagger_auto_schema(method='get', responses={200: DesempenoTrabajadorSerializer(many=True)})
@swagger_auto_schema(method='post', request_body=DesempenoTrabajadorSerializer, responses={201: DesempenoTrabajadorSerializer})
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def desempeno_list(request):
    if request.method == 'GET':
        desempenos = DesempenoTrabajador.objects.all()
        serializer = DesempenoTrabajadorSerializer(desempenos, many=True)
        return Response(serializer.data)

    serializer = DesempenoTrabajadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', responses={200: DesempenoTrabajadorSerializer})
@swagger_auto_schema(method='put', request_body=DesempenoTrabajadorSerializer, responses={200: DesempenoTrabajadorSerializer})
@swagger_auto_schema(method='delete', responses={204: 'No Content'})
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def desempeno_detail(request, pk):
    try:
        desempeno = DesempenoTrabajador.objects.get(pk=pk)
    except DesempenoTrabajador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DesempenoTrabajadorSerializer(desempeno)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DesempenoTrabajadorSerializer(desempeno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    desempeno.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# -----------------------
# SUELDOS
# -----------------------
@swagger_auto_schema(method='get', responses={200: SueldoTrabajadorSerializer(many=True)})
@swagger_auto_schema(method='post', request_body=SueldoTrabajadorSerializer, responses={201: SueldoTrabajadorSerializer})
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def sueldo_list(request):
    if request.method == 'GET':
        sueldos = SueldoTrabajador.objects.all()
        serializer = SueldoTrabajadorSerializer(sueldos, many=True)
        return Response(serializer.data)

    serializer = SueldoTrabajadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', responses={200: SueldoTrabajadorSerializer})
@swagger_auto_schema(method='put', request_body=SueldoTrabajadorSerializer, responses={200: SueldoTrabajadorSerializer})
@swagger_auto_schema(method='delete', responses={204: 'No Content'})
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def sueldo_detail(request, pk):
    try:
        sueldo = SueldoTrabajador.objects.get(pk=pk)
    except SueldoTrabajador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SueldoTrabajadorSerializer(sueldo)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SueldoTrabajadorSerializer(sueldo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    sueldo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# -----------------------
# HOME
# -----------------------
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
            "/api/token/",
            "/swagger/"
        ]
    })
