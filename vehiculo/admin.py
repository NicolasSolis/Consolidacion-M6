from django.contrib import admin
from .models import VehiculoModel

admin.site.site_header = 'Consolidacion 6 Django'
admin.site.index_title = 'Panel de control Proyecto Vehiculos'
admin.site.site_title = 'Administrador Django'

class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_de_creacion', 'fecha_de_modificacion')
    list_display = ('modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'condicion_precio', 'fecha_de_creacion', 'fecha_de_modificacion')

admin.site.register(VehiculoModel, VehiculoAdmin)