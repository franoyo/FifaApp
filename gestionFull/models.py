from django.db import models

# Create your models here.
class equipo(models.Model):
    nombre_equipo = models.CharField(max_length=255)
    img_bandera=models.ImageField(upload_to='imagenes/')
    escudo_equipo=models.ImageField(upload_to='imagenes/')
    def __str__(self):
        return self.nombre_equipo
    class meta:
        verbose_name = "equipo"
        verbose_name_plural = "equipos"
        db_table = "equipos"
        ordering = ["nombre_equipo"]
from django.db import models


class PosicionJuego(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class meta:
        verbose_name = "posicion"
        verbose_name_plural = "pocisiones"
        db_table = "pocisiones"
class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='imagenes/')
    fecha_nacimiento = models.DateField()
    posicion = models.ForeignKey(PosicionJuego, on_delete=models.CASCADE)
    numero_camiseta = models.PositiveIntegerField()
    titular = models.BooleanField(default=False)
    equipo = models.ForeignKey(equipo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class meta:
        verbose_name = "jugador"
        verbose_name_plural = "jugadores"
        db_table = "jugadores"
        ordering = ["nombre"]
class Nacionalidad(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'nacionalidad'
        verbose_name_plural = 'Nacionalidades'

class Tecnico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    
    ROLES = [
        ('TEC', 'Técnico'),
        ('ASI', 'Asistente'),
        ('MED', 'Médico'),
        ('PRE', 'Preparador'),
    ]
    rol = models.CharField(max_length=3, choices=ROLES)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'tecnico'
        verbose_name_plural = 'Técnicos'
