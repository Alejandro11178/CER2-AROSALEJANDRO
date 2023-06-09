from django.db import models
from django.contrib.auth.models import User # Se importa el modelo User del módulo auth de Django, 
                                            # User es proporcionado por Django y se utiliza para gestionar la autenticación 
                                            # y autorización de usuarios en una aplicación web. 

# Create your models here.

class Categoria(models.Model):
    nombre = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=200)

    def __str__(self):          # Se utiliza para representar en cadena de texto un objeto, dándole el valor más significativo para imprimir.     
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
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)# Al eliminarse una Categoria, pregunta si es que está seguro de eliminarla.
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    publicado_por = models.ForeignKey(User, on_delete=models.PROTECT)# Al eliminarse un Usuario, pregunta si es que está seguro de eliminarla.
    
    def __str__(self):
        return self.titulo
    

