# Django_V1 version-01

# Django Pildoras - Proyectos de Práctica, aqui encontraras los primeros pasos que tendrias que tener encuenta a la hora de inciar con django.

# Patron de diseño: Model-View-Template (MVT)

# Dependencias
Todas las dependencias están en requirements.txt en la carpeta raíz.

Este repositorio contiene dos proyectos Django para aprendizaje por el momento, va ir creciendo con el tiempo.:

## 1️⃣ Proyecto1
Proyecto básico para conocer:
- Estructura de un proyecto Django
- Enlazar Views, URLs, plantillas HTML, condicionales.

### Cómo ejecutar: (Clonar)
```bash
- cd Proyecto1
- python -m venv venv
- # Activar entorno virtual #
- venv\Scripts\activate       # Windows
- source venv/bin/activate    # Linux/Mac
- pip install -r ../requirements.txt - Ö - pip install -r requirements.txt
- python manage.py runserver
```
# Rutas a navegar:
http://127.0.0.1:8000/saludo/
http://127.0.0.1:8000/edadFutura/28/2040
http://127.0.0.1:8000/plantillaHija/
http://127.0.0.1:8000/plantillaHija2/
## ======================================================

## 2️⃣ TiendaOnline

Proyecto que se conecta a PostgreSQL y gestiona artículos.
# Nota: asegúrate de que PostgreSQL esté corriendo y que los datos de conexión en settings.py sean correctos.

Cómo ejecutar:
```cd TiendaOnline
- python -m venv venv
- venv\Scripts\activate       # Windows
- source venv/bin/activate    # Linux/Mac
- pip install -r ../requirements.txt
- # Por si realizas algun cambio en los modelos ejecuta: python manage.py makemigrations #
- python manage.py migrate
- # Seguir los pasos del archivo para que hagas pruebas: # # insert_datos.mk 
- # Recuerda validar en PostgreSQL
```
