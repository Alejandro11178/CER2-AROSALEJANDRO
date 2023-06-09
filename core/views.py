from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado # Importamos desde el archivo models el modelo de Comunicado
# Create your views here.


def home(request): # Estas funciones sirven para renderizar plantillas, en este caso home.html
    return render(request, 'core/home.html')


def comunicados(request): # Estas funciones sirven para renderizar plantillas, en este comunicados.html. Aparte también aquí ordenamos los comunicados por fecha de envío
    comunicados = Comunicado.objects.order_by('fecha_envio') #Se realiza una consulta a la base de datos para obtener todos los objetos de la clase 
                                                             # según su fecha de envío.
    
    data={   # Se crea un diccionario llamado data que contiene los comunicados obtenidos de la base de datos.
        'comunicados': comunicados
    }
    
    return render(request, 'core/comunicados.html', data) #Aquí se renderiza la plantilla y el diccionario data.


