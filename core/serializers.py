# core/serializers.py
from rest_framework import serializers
from .models import ( Trabajador, TipoTrabajador, Asistencia,  Accidente,  EficienciaTrabajador,  DesempenoTrabajador,  SueldoTrabajador,
)

# ---------------------- TipoTrabajador ---------------------- #
class TipoTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTrabajador
        fields = "__all__"

    def validate_rol_cargo(self, value):
        if not value.strip():
            raise serializers.ValidationError("El rol/cargo es obligatorio.")
        return value

    def validate_tipo_contrato(self, value):
        if not value.strip():
            raise serializers.ValidationError("El tipo de contrato es obligatorio.")
        return value


# ------------------------ Trabajador ------------------------ #
class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = "__all__"

    def validate_rut(self, value):
       
        if "-" not in value:
            raise serializers.ValidationError(
                "El RUT debe incluir guion. Ejemplo: '199952632-4'."
            )
        if len(value) < 8:
            raise serializers.ValidationError("El RUT es demasiado corto.")
        return value

    def validate_email(self, value):
      
        if "@" not in value:
            raise serializers.ValidationError("Correo inválido.")
        return value

    def validate_sueldo_base(self, value):
        if value < 0:
            raise serializers.ValidationError("El sueldo base no puede ser negativo.")
        return value

    def validate_estado(self, value):
        estados_validos = ["ACTIVO", "INACTIVO"]
        if value not in estados_validos:
            raise serializers.ValidationError(
                f"Estado inválido. Use uno de: {', '.join(estados_validos)}."
            )
        return value

    def validate_telefono(self, value):
        if value and len(value) < 8:
            raise serializers.ValidationError("El teléfono debe tener al menos 8 dígitos.")
        return value

    def validate(self, attrs):
      
        fecha_nac = attrs.get("fecha_nacimiento")
        fecha_ingreso = attrs.get("fecha_ingreso")

        if fecha_nac and fecha_ingreso and fecha_ingreso < fecha_nac:
            raise serializers.ValidationError(
                "La fecha de ingreso no puede ser anterior a la fecha de nacimiento."
            )
        return attrs


# ------------------------ Asistencia ------------------------ #
class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = "__all__"

    def validate_estado(self, value):
        estados_validos = ["PRESENTE", "AUSENTE", "LICENCIA", "VACACIONES"]
        if value not in estados_validos:
            raise serializers.ValidationError(
                f"Estado de asistencia inválido. Use uno de: {', '.join(estados_validos)}."
            )
        return value

    def validate_fecha(self, value):
        from datetime import date

        if value > date.today():
            raise serializers.ValidationError(
                "La fecha de asistencia no puede ser futura."
            )
        return value

    def validate_horas_extras(self, value):
        if value < 0:
            raise serializers.ValidationError("Las horas extras no pueden ser negativas.")
        return value

    def validate_minutos_atraso(self, value):
        if value < 0:
            raise serializers.ValidationError("Los minutos de atraso no pueden ser negativos.")
        return value

    def validate(self, attrs):
        entrada = attrs.get("hora_entrada")
        salida = attrs.get("hora_salida")

        if entrada and salida and salida < entrada:
            raise serializers.ValidationError(
                "La hora de salida no puede ser menor que la hora de entrada."
            )
        return attrs


# ------------------------ Accidente ------------------------- #
class AccidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accidente
        fields = "__all__"

    def validate_fecha(self, value):
        from datetime import date

        if value > date.today():
            raise serializers.ValidationError(
                "La fecha del accidente no puede ser futura."
            )
        return value

    def validate_gravedad(self, value):
        niveles = ["LEVE", "MODERADA", "GRAVE", "FATAL"]
        if value not in niveles:
            raise serializers.ValidationError(
                f"Gravedad inválida. Use uno de: {', '.join(niveles)}."
            )
        return value

    def validate_dias_licencia(self, value):
        if value < 0:
            raise serializers.ValidationError("Los días de licencia no pueden ser negativos.")
        if value > 365:
            raise serializers.ValidationError("Los días de licencia no pueden superar 365.")
        return value

    def validate_costo_estimado(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("El costo estimado no puede ser negativo.")
        return value


# ------------------ EficienciaTrabajador -------------------- #
class EficienciaTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EficienciaTrabajador
        fields = "__all__"

    def validate_id_eficiencia(self, value):
        if value <= 0:
            raise serializers.ValidationError("El id_eficiencia debe ser positivo.")
        return value

    def validate_trabajos_completados_en_1_mes(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Los trabajos completados no pueden ser negativos."
            )
        return value

    def validate_sueldo_promedio_informado(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "El sueldo promedio informado no puede ser negativo."
            )
        return value


# ------------------ DesempenoTrabajador --------------------- #
class DesempenoTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesempenoTrabajador
        fields = "__all__"

    def validate_id_desempeno(self, value):
        if value <= 0:
            raise serializers.ValidationError("El id_desempeño debe ser positivo.")
        return value


# --------------------- SueldoTrabajador --------------------- #
class SueldoTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SueldoTrabajador
        fields = "__all__"

    def validate_mes(self, value):
       
        if len(value) < 7 or "-" not in value:
            raise serializers.ValidationError(
                "El mes debe tener un formato tipo '2025-11'."
            )
        return value

    def validate_sueldo_total_mes(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "El sueldo total del mes no puede ser negativo."
            )
        return value

    def validate_cantidad_trabajos_mes(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "La cantidad de trabajos del mes no puede ser negativa."
            )
        return value

    def validate(self, attrs):
   
        trabajos = attrs.get("cantidad_trabajos_mes", 0)
        if trabajos == 0 and attrs.get("sueldo_total_mes", 0) > 0:
            raise serializers.ValidationError(
                "Si no hay trabajos en el mes, el sueldo total debería ser 0."
            )
        return attrs
