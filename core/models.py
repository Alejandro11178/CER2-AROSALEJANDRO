from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=200)

    def __str__(self):
        return self.nombre

class Comunicado(models.Model):
    NIVEL_CHOICES = [("GEN", "General"),
                     ("PRE", "Ciclo Preescolar"),
                     ("BAS", "Ciclo Básico"),
                     ("MED", "Ciclo Medio")]
    
    correlativo = models.AutoField(primary_key=True)
    titulo = models.TextField(max_length=50)
    detalle = models.TextField(max_length=200)
    nivel = models.CharField(max_length=5, choices=NIVEL_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT) # Al eliminarse una categoria, pregunta si es que está seguro de eliminarla.
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    publicado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.titulo
    

