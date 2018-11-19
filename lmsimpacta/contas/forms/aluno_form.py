from django import forms
from django.contrib.auth.forms import UserCreationForm

from contas.models import Usuario, Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('nome', 'email', 'celular', 'foto')