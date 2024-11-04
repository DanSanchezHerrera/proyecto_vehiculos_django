# Proyecto Vehículos Django

Este proyecto es una aplicación web desarrollada en Django para gestionar un catálogo de vehículos. Los usuarios registrados pueden listar los vehículos, y aquellos con permisos específicos pueden agregar nuevos vehículos a la base de datos.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)

## Descripción

La aplicación de vehículos permite a los usuarios autenticados:
- Listar los vehículos disponibles en el catálogo.
- Si tienen el permiso y son staff, agregar vehículos al catálogo

## Instalación

### Prerrequisitos

- Python 3.12.4 o superior, pip (incluido)
- Django 5.1.1
- Otros requisitos definidos en `requirements.txt`

### Clonar el Repositorio

Por favor clonar en tu máquina local :) :

```bash
git clone https://github.com/DanSanchezHerrera/proyecto_vehiculos_django
cd proyecto_vehiculos_django
```

### Crear y Activar el Entorno Virtual

```bash
# En Windows
python -m venv entorno_virtual
entorno_virtual\Scripts\activate
```

### Instalar Dependencias

```bash
pip install -r requirements.txt
```
## Configuración

### Aplicar Migraciones
```bash
python manage.py migrate
```
### Crear superusuario
```bash
python manage.py createsuperuser
```
## Ejecución
Para ejecutar por favor usar:
```bash
python manage.py runserver
```
