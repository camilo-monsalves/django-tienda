from django import forms

from django.contrib.auth.forms import UserCreationForm

# models.py
from .models import Usuario, User

class RegistrarUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')
    rut = forms.CharField(required=True, label='Ingrese su rut')
    nombre = forms.CharField(required=True, label='Ingrese su nombre')
    apellido = forms.CharField(required=True, label='Ingrese su apellido')

    class Meta:
        model = Usuario
        fields = ['username','email', 'rut', 'nombre', 'apellido']