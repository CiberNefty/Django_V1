from django.http import HttpResponse
import datetime
from django.template import Template, Context
#from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render
class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Creacion vista
def saludo(request):

    p1 = Persona("Santiago", "Gomez")

    nombre = "Dani"
    apellido = "Vera"
    fecha_ahora = datetime.datetime.now()
    temas2 = ["Indice 0","Indice 1", "Indice 2","Indice 3", "Indice 4"]

    # Cargamos nuestra plantilla 
    #doc_externo = open("C:/Users/danim/Proyectos/Django_pildoras/Proyecto1/Proyecto1/Plantillas/miplantilla1.html")
    #Creamos el objeto tipo Template
    #platilla = Template(doc_externo.read())
    
    #doc_externo.close()
    
    # Cargar plantilla mas elegante desde eel metodo loader con django
    #doc_externo = loader.get_template("miplantilla1.html")
    #doc_externo = get_template("miplantilla1.html")


    # Crear contexto
    #contexto = Context({"nombre_persona": nombre, "apellido_persona": apellido, "apellido_2": "Arias", "fecha_ahora": fecha_ahora,
    #                    "objeto_persona1_nom": p1.nombre, "objeto_persona1_ap": p1.apellido, "temas":["Plantillas","Modelos", "FOrmularios","Listas", "Despliegue"],
    #                    "temas2": temas2})
    # EL CONTEXTO AHORA CON EL METODO get_template recibe un diccionario directamente sin necesidad de crear un objeto tipo Context
    diccionario_contexto = {"nombre_persona": nombre, "apellido_persona": apellido, "apellido_2": "Arias", "fecha_ahora": fecha_ahora,
                        "objeto_persona1_nom": p1.nombre, "objeto_persona1_ap": p1.apellido, "temas":["Plantillas","Modelos", "FOrmularios","Listas", "Despliegue"],
                        "temas2": temas2}
    
    # Renderizar plantilla (variable)
    #documento = platilla.render(contexto)
    #documento = doc_externo.render({"nombre_persona": nombre, "apellido_persona": apellido, "apellido_2": "Arias", "fecha_ahora": fecha_ahora,
    #                    "objeto_persona1_nom": p1.nombre, "objeto_persona1_ap": p1.apellido, "temas":["Plantillas","Modelos", "FOrmularios","Listas", "Despliegue"],
    #                    "temas2": temas2})

    # return HttpResponse(documento)

    # AHora vamos a usar el metodo render de django.shortcuts para renderizar la plantilla y pasarle el contexto
    return render(request, "miplantilla1.html",{"nombre_persona": nombre, "apellido_persona": apellido, "apellido_2": "Arias", "fecha_ahora": fecha_ahora,
                        "objeto_persona1_nom": p1.nombre, "objeto_persona1_ap": p1.apellido, "temas":["Plantillas","Modelos", "FOrmularios","Listas", "Despliegue"],
                        "temas2": temas2})

def plantillaHija(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "plantillaHija.html", {"fecha_ahora": fecha_actual})

def plantillaHija2(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "plantillaHija2.html", {"fecha_ahora": fecha_actual})

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