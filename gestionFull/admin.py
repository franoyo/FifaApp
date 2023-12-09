from django.contrib import admin
from .models import equipo
from django.utils.html import format_html
from .models import Jugador
from .models import PosicionJuego
from .models import Nacionalidad
from .models import Tecnico

# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre_equipo',
                    'imagen_bandera',
                    'escudo_del_equipo')
    def imagen_bandera(self,obj):
        return format_html('<img src={} width=100px;height=100px />',obj.img_bandera.url)
    def escudo_del_equipo(self,obj):
        return format_html('<img src={} width=100px;height=100px />',obj.escudo_equipo.url)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre',
                    'apellido',
                    'imagen',
                    'fecha_nacimiento',
                    'equipo')
    def imagen(self,obj):
        return format_html('<img src={} width=100px;height=100px />',obj.foto.url)

admin.site.register(equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(PosicionJuego)
admin.site.register(Nacionalidad)
admin.site.register(Tecnico)