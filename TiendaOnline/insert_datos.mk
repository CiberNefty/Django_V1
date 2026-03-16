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