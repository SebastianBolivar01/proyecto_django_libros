from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
    # Inicio
    path('', views.inicio, name='inicio'),

    # Gestión de autores
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/nuevo/', views.crear_autor, name='crear_autor'),
    path('autores/<int:pk>/editar/', views.editar_autor, name='editar_autor'),
    path('autores/<int:pk>/eliminar/', views.eliminar_autor, name='eliminar_autor'),

    # Gestión de libros
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/nuevo/', views.crear_libro, name='crear_libro'),
    path('libros/<int:pk>/editar/', views.editar_libro, name='editar_libro'),
    path('libros/<int:pk>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
]
