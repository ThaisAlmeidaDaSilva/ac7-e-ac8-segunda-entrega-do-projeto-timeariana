from django import forms
from django.core.mail import send_mail

ASSUNTOS = (
    ('', 'Selecione'),
    ('A', 'Atendimento ao Cliente'),
    ('S', 'Secretaria de Graduação'),
    ('SPG', 'Secretaria de Pós Graduação'),
    ('F', 'Financeiro'),
    ('M', 'Matrícula'),
    ('O', 'Ouvidoria')
)

class ContatoForm(forms.Form):

    email = forms.EmailField(
        label='E-Mail'
    )

    nome = forms.CharField(
        label='Nome Completo'
    )

    assunto = forms.ChoiceField(
        label='Assunto',
        choices=ASSUNTOS
    )

    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea
    )

    def is_valid(self):
        valido = super(ContatoForm, self).is_valid()

        if valido:
            assunto = ''
            for tupla in ASSUNTOS:
                if tupla[0] == self.cleaned_data['assunto']:
                    assunto = tupla[1]
                    break

            send_mail(
                'Mensagem do Site - Assunto: '+assunto,
                self.cleaned_data['mensagem'],
                self.cleaned_data['email'],
                ['contato@impacta.com.br']
            )

        return valido