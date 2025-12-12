from django.contrib import admin
from .models import (
    Trabajador,
    Asistencia,
    Accidente,
    EficienciaTrabajador,
    DesempenoTrabajador,
    SueldoTrabajador
)

admin.site.register(Trabajador)
admin.site.register(Asistencia)
admin.site.register(Accidente)
admin.site.register(EficienciaTrabajador)
admin.site.register(DesempenoTrabajador)
admin.site.register(SueldoTrabajador)
