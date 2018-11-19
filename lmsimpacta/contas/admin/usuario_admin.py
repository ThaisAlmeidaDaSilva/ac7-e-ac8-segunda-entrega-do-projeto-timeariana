from django.contrib.auth.admin import UserAdmin
#from contas.forms import UsuarioAlteracaoForm, UsuarioCriacaoForm

class UsuarioAdmin(UserAdmin):
 #   form = UsuarioAlteracaoForm
 #   add_form = UsuarioCriacaoForm
    list_filter = ()
    list_display = ('username', 'tipo')
    fieldsets = (
        (None, {'fields': ('username', 'data_expiracao')}),
    )
    add_fieldsets = (
        (None, { 'fields': ('username',) } ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    _tipo = None

    def save_model(self, request, obj, form, change):
        obj.tipo = self._tipo
        super(UsuarioAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        resultado = super(UsuarioAdmin, self).get_queryset(request)
        return resultado.filter(tipo=self._tipo)
