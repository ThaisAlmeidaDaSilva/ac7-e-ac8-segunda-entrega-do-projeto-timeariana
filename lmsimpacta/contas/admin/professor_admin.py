from django.contrib import admin

from contas.admin import UsuarioAdmin
from contas.models import Professor, Usuario

class ProfessorUsuario(Usuario):
    class Meta:
        proxy = True
        verbose_name = 'professor'
        verbose_name_plural = 'professores'

class ProfessorInline(admin.StackedInline):
    model = Professor
    max_num = 1

@admin.register(ProfessorUsuario)
class ProfessorAdmin(UsuarioAdmin):
    inlines = (ProfessorInline,)
    _tipo = 'P'