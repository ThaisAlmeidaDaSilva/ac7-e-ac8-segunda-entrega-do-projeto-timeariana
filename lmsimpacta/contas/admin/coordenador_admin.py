from django.contrib import admin

from contas.admin import UsuarioAdmin
from contas.models import Coordenador, Usuario

class CoordenadorUsuario(Usuario):
    class Meta:
        proxy = True
        verbose_name = 'coordenador'
        verbose_name_plural = 'coordenadores'

class CoordenadorInline(admin.StackedInline):
    model = Coordenador
    max_num = 1

@admin.register(CoordenadorUsuario)
class CoordenadorAdmin(UsuarioAdmin):
    inlines = (CoordenadorInline,)
    _tipo = 'C'