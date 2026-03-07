from django.http import HttpResponse
import datetime

# Creacion vista
def saludo(request):
    contenido = "<html><body><h1>Hola Mundo primera pagina con Django</h1></body></html>"

    return HttpResponse(contenido)

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
    resultado = "<html><body><h2>En el año %s tendremos %s años.<h2></body></html>" % (agno,edadFutura)

    return HttpResponse(resultado)