Ingresamos datos desde consola de python, para ello ejecutamos el siguiente comando:


# bash: RUTA: Django_pildoras/TiendaOnline
python manage.py shell

#Una vez dentro de la consola de python, importamos el modelo y creamos un nuevo objeto:
>> from gestionPedidos.models import Articulos
>> art = Artiuculos(nombre = "Ventana", seccion = "Contruccion", precio = 100)
>> art.save()
>> art2 = Articulos(nombre = "Puerta", seccion = "Contruccion", precio = 150)
art2.save()
#Metodo create para guardar un nuevo registro
>> art3 = Articulos.objects.create(nombre='Taladro',seccion='Ferreteria',precio=134)

# INSERTAR VARIOS REGISTROS A LA VEZ
articulos = [
	Articulos(nombre="Lampara",seccion= "Decoracion", precio= 70),
	Articulos(nombre="Pantalon",seccion= "Confeccion", precio= 45),
	Articulos(nombre="Destornillador",seccion= "Ferreteria", precio= 35),
	Articulos(nombre="Balon",seccion= "Deportes", precio= 25),
	Articulos(nombre="Raqueta",seccion= "Deportes", precio= 105),
	Articulos(nombre="Muñeco",seccion= "Jugueteria", precio= 15),
	Articulos(nombre="Tren Electrico",seccion= "Jugueteria", precio= 135),
]
Articulos.objects.bulk_create(articulos)

# Como actualizar un registro
>> art.precio = 120
>> art.save()

# Para eliminar un registro

# Para eliminar un registro, primero lo buscamos, obtenemos su valor y, luego lo eliminamos
>> artEliminar = Articulos.objects.get(nombre='Puerta')
>> artEliminar.delete()

# Metodo all para mostrar todos los registros
>> Lista = Articulos.objects.all()
>> Lista

>> Lista.query.__str__()

# FILTRADO DE OBJETOS METODO (FILTER)

# WHERE
Articulos.objects.filter(seccion = 'Deportes')

# 1. Modificamos el modelo en el cual agregamos un metodo que devuelve un string de nuestros campos en models.py (def __str__)
# 2. Cuando modificamos los modelos toca hacer la migrgacion: 
# 	2.1. python manage.py makemigrations
#	2.2. python manage.py migrate
# 3. Ahora si entramos al shell de python nuevamente y ingresamos valores y vemos como nos devuelve un valor en mensaje.

# where con criterio
Articulos.objects.filter(seccion = 'Deportes', nombre='Mesa')

# criterio de mayor que (>) es igual a (campo__gte=) (__gte= valor)
Articulos.objects.filter(precio__gte=90)
# criterio de menor que (<) es igual a (campo__lte=) (__lte= valor)
Articulos.objects.filter(precio__lte=90)

# Rangos entre tal a tal numero: __range(10,106)
Articulos.objects.filter(precio__range=(40,100))

# ORDENEAR (ORDER BY)
Articulos.objects.filter(precio__gte=50).order_by('precio') # ASC
Articulos.objects.filter(precio__gte=50).order_by('-precio') # DESC
