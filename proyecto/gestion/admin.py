from django.contrib import admin
from .models import Autor, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'correo', 'fecha_nacimiento')
    search_fields = ('nombre', 'nacionalidad')
    list_per_page = 15


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'isbn', 'fecha_publicacion')
    list_filter = ('genero', 'autor')
    search_fields = ('titulo', 'isbn')
    list_per_page = 15
