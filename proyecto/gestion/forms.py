from django import forms
from .models import Autor, Libro


class AutorForm(forms.ModelForm):
    """Formulario para el registro y edición de autores."""

    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
        labels = {
            'nombre': 'Nombre completo',
            'correo': 'Correo electrónico',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'biografia': 'Biografía',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Gabriel García Márquez',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'autor@correo.com',
            }),
            'nacionalidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Colombiana',
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'biografia': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Breve reseña sobre el autor...',
                'rows': 3,
            }),
        }


class LibroForm(forms.ModelForm):
    """Formulario para el registro y edición de libros."""

    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
        labels = {
            'titulo': 'Título de la obra',
            'fecha_publicacion': 'Fecha de publicación',
            'genero': 'Género literario',
            'isbn': 'Código ISBN',
            'autor': 'Autor asociado',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Cien años de soledad',
            }),
            'fecha_publicacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'genero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Novela, Poesía, Ensayo',
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 978-3-16-148410-0',
            }),
            'autor': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
