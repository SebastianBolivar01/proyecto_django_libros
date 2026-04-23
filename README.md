# LetraViva - Gestión de Libros y Autores

Aplicación web desarrollada con Django para la administración de un catálogo de libros y autores.

## Tecnologías

- Python 3.11
- Django 6.0.4
- Bootstrap 5.3
- SQLite

## Instalación

```bash
python -m venv venv
venv\Scripts\activate
pip install -r proyecto/requirements.txt
```

## Ejecución

```bash
cd proyecto
python manage.py migrate
python manage.py runserver
```

## Estructura del proyecto

```
proyecto/
├── manage.py
├── proyecto/          # Configuración global
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── gestion/           # App principal
    ├── models.py      # Modelos Autor y Libro
    ├── views.py       # Vistas CRUD
    ├── forms.py       # Formularios
    ├── urls.py        # Rutas de la app
    ├── admin.py       # Panel administrativo
    └── templates/     # Plantillas HTML
```

## Equipo

- **SebastianBolivar01** - Estructura, Modelos e Interfaz
- **Jujuks** - Lógica de Negocio, Rutas y Despliegue
