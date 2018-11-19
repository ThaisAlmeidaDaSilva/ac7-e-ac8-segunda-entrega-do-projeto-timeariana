from django.contrib import admin
from .models import Curso, Disciplina, DisciplinaOfertada
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "tipo", "noturno", "diurno")
    list_filter = ("tipo", "noturno", "diurno")
    search_fields = ("nome", "sigla")

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("nome", "identificador", "status", "carga_horaria")

class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ("disciplina", "curso", "ano", "semestre", "turma")
    list_filter = ("curso", "ano", "semestre")
    


admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(DisciplinaOfertada, DisciplinaOfertadaAdmin)
