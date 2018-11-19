from django import forms

from django.contrib.auth.forms import UserCreationForm

from contas.models import Usuario

class UsuarioForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields = ('username','password1', 'password2')