from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class TipoTrabajador(models.Model):

    rol_cargo = models.CharField(max_length=60)
    tipo_contrato = models.CharField(max_length=20)

def __str__(self):
        return f"{self.rol_cargo} ({self.tipo_contrato})"



class Trabajador(models.Model):
      rut = models.CharField(max_length=12, unique=True)
      nombre = models.CharField(max_length=60)
      apellido = models.CharField(max_length=60)
      fecha_nacimiento = models.DateField()
      email = models.EmailField(unique=True)
      telefono = models.CharField(max_length=20, blank=True)
      rol_cargo = models.CharField(max_length=60, help_text="Rol o cargo del trabajador")
      tipo_contrato = models.CharField(
        max_length=20,
        help_text="Tipo de contrato (Plazo fijo, Indefinido, Honorarios, etc.)"
    )

      area = models.CharField(max_length=60, blank=True)
      turno = models.CharField(max_length=20)  # DIURNO / NOCTURNO / ROTATIVO
      fecha_ingreso = models.DateField()
      sueldo_base = models.DecimalField(max_digits=12, decimal_places=2, default=0)
      estado = models.CharField(
        max_length=10,
        help_text="ACTIVO / INACTIVO"
    )
      contacto_emergencia = models.CharField(max_length=100, blank=True)
      telefono_emergencia = models.CharField(max_length=20, blank=True)

      def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"    


class Accidente(models.Model):
     fecha = models.DateField()
     tipo = models.CharField(max_length=60)
     gravedad = models.CharField(max_length=10)  # LEVE / MODERADA / GRAVE / FATAL
     lugar = models.CharField(max_length=120)
     hora_suceso = models.TimeField(null=True, blank=True)
     descripcion = models.TextField(blank=True)
     requiere_licencia = models.BooleanField(default=False)
     dias_licencia = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(365)]
    )
    
     costo_estimado = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )
     reportado_a = models.CharField(max_length=120, blank=True)
     observaciones = models.CharField(max_length=255, blank=True)

   
     trabajadores_involucrados = models.TextField(
        blank=True,
        help_text="Lista de RUTs o nombres de trabajadores involucrados, separados por coma."
    )
     
     def __str__(self):
        return f"{self.fecha} - {self.tipo} ({self.gravedad})"
     

class Asistencia(models.Model):
    
    trabajador_rut = models.CharField(max_length=12)
    trabajador_nombre = models.CharField(max_length=120)

    fecha = models.DateField()
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    minutos_atraso = models.PositiveIntegerField(default=0)
    horas_extras = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )  
    estado = models.CharField(
        max_length=12,
        help_text="PRESENTE / AUSENTE / LICENCIA / VACACIONES"
    )
    observaciones = models.CharField(max_length=255, blank=True)   

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.trabajador_nombre} ({self.trabajador_rut}) - {self.fecha} ({self.estado})"

class EficienciaTrabajador(models.Model):
   
    trabajador_rut = models.CharField(max_length=12)
    trabajador_nombre = models.CharField(max_length=120)

    id_eficiencia = models.IntegerField()
    trabajos_completados_en_1_mes = models.IntegerField(default=0)
    sueldo_promedio_informado = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.trabajador_nombre} ({self.trabajador_rut}) - efic {self.id_eficiencia}"

class DesempenoTrabajador(models.Model):
   
    trabajador_rut = models.CharField(max_length=12)
    trabajador_nombre = models.CharField(max_length=120)

    id_desempeno = models.IntegerField()
    forma_de_hacer_trabajos = models.CharField(max_length=255, blank=True)
    posibles_quejas = models.CharField(max_length=255, blank=True)    

    def __str__(self):
        return f"{self.trabajador_nombre} ({self.trabajador_rut}) - desp {self.id_desempeno}"
    
class SueldoTrabajador(models.Model):
   
    trabajador_rut = models.CharField(max_length=12)
    trabajador_nombre = models.CharField(max_length=120)   
    mes = models.CharField(max_length=20, help_text="Mes de cálculo, por ejemplo: 2025-11")
    cantidad_trabajos_mes = models.PositiveIntegerField(default=0)
    tipo_trabajos_mes = models.CharField(max_length=255)
    sueldo_total_mes = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    id_eficiencia_asociada = models.IntegerField(
        null=True,
        blank=True,
        help_text="ID de eficiencia asociada (si aplica)."
    )

    def __str__(self):
        return f"{self.trabajador_nombre} ({self.trabajador_rut}) - {self.mes} (${self.sueldo_total_mes})"