from django.contrib import admin
from .models import equipo
from .models import Jugador
from .models import PosicionJuego
from .models import Nacionalidad
from .models import Tecnico

# Register your models here.

admin.site.register(equipo)
admin.site.register(Jugador)
admin.site.register(PosicionJuego)
admin.site.register(Nacionalidad)
admin.site.register(Tecnico)