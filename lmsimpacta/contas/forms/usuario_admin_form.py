from django import forms
from contas.models import Usuario

class UsuarioAdminForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ('username', 'data_expiracao')