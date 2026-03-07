from django.http import HttpResponse
import datetime
from django.template import Template, Context

# Creacion vista
def saludo(request):
    # Cargamos nuestra plantilla 
    doc_externo = open("C:/Users/danim/Proyectos/Django_pildoras/Proyecto1/Proyecto1/Plantillas/miplantilla1.html")
    #Creamos el objeto tipo Template
    platilla = Template(doc_externo.read())
    
    doc_externo.close()

    # Crear contexto
    contexto = Context()

    # Renderizar plantilla (variable)
    documento = platilla.render(contexto)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Adios buena practica para django ")

# Vista Fecha
def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    contenido = "<html><body><h1>Fecha y Hora actuales: %s </h1></body></html>" %fecha_actual
    return HttpResponse(contenido)

# Vista Calculadora Edad
def calculaEdad(request, edad, agno):
    #edadActual = 28
    periodo = agno - 1998
    edadFutura = edad + periodo
    resultado = "<html><body><h2>En el año %s tendremos %s años.</h2></body></html>" % (agno,edadFutura)

    return HttpResponse(resultado)