from django.contrib import admin
from .models import Categoria, Comunicado # Importamos desde models.py los modelos Categoria y Comunicado.

# Register your models here.

class ComunicadoAdmin(admin.ModelAdmin):  # Esta clase se usará para filtrar los Comunicados dentro del administrador de Django.
    list_filter = ["fecha_envio"]         # Puedo elegir filtrar los datos por fecha de envío .
    ordering = ("fecha_envio",)           # Puedo ordenar los datos por orden ascendente o descendente según su fecha de envío.
    
admin.site.register(Categoria) # Registra el modelo Categoria en el panel de administración de Django.
admin.site.register(Comunicado, ComunicadoAdmin) # Registra el modelo Categoria y la clase ComunicadoAdmin en el panel de administración de Django.

