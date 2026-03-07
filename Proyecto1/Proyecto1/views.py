from django.http import HttpResponse

# Creacion vista
def saludo(request):
    contenido = "<html><body><h1>Hola Mundo primera pagina con Django</h1></body></html>"

    return HttpResponse(contenido)

def despedida(request):
    return HttpResponse("Adios buena practica para django ")

