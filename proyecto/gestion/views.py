from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro
from .forms import AutorForm, LibroForm


def inicio(request):
    """Página principal con resumen del catálogo."""
    context = {
        'autores_count': Autor.objects.count(),
        'libros_count': Libro.objects.count(),
    }
    return render(request, 'gestion/inicio.html', context)


# ──────────── Vistas de Autores ────────────

def lista_autores(request):
    """Muestra el directorio completo de autores."""
    autores = Autor.objects.all().order_by('nombre')
    return render(request, 'gestion/lista_autores.html', {'autores': autores})


def crear_autor(request):
    """Formulario para registrar un autor nuevo en el sistema."""
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestion:lista_autores')
    return render(request, 'gestion/autor_form.html', {'form': form})


def editar_autor(request, pk):
    """Permite modificar la información de un autor existente."""
    autor = get_object_or_404(Autor, pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('gestion:lista_autores')
    return render(request, 'gestion/autor_form.html', {'form': form})


def eliminar_autor(request, pk):
    """Confirmación y eliminación de un autor del sistema."""
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('gestion:lista_autores')
    return render(request, 'gestion/autor_confirm_delete.html', {'autor': autor})


# ──────────── Vistas de Libros ────────────

def lista_libros(request):
    """Muestra el catálogo completo de obras registradas."""
    libros = Libro.objects.select_related('autor').order_by('titulo')
    return render(request, 'gestion/lista_libros.html', {'libros': libros})


def crear_libro(request):
    """Formulario para agregar una nueva obra al catálogo."""
    form = LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestion:lista_libros')
    return render(request, 'gestion/libro_form.html', {'form': form})


def editar_libro(request, pk):
    """Permite actualizar los datos de un libro existente."""
    libro = get_object_or_404(Libro, pk=pk)
    form = LibroForm(request.POST or None, instance=libro)
    if form.is_valid():
        form.save()
        return redirect('gestion:lista_libros')
    return render(request, 'gestion/libro_form.html', {'form': form})


def eliminar_libro(request, pk):
    """Confirmación y eliminación de un libro del catálogo."""
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('gestion:lista_libros')
    return render(request, 'gestion/libro_confirm_delete.html', {'libro': libro})
