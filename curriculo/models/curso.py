from django.db import models

TIPOS_CURSOS = (
    ('T', 'Tecnólogo'),
    ('G', 'Graduação')
)

class Curso(models.Model):

    nome = models.CharField('Nome', max_length=120)

    sigla = models.CharField('Sigla', max_length=5, unique=True)

    sobre = models.TextField('Sobre o curso', null=True)

    duracao = models.SmallIntegerField('Semestres')

    tipo = models.CharField('Tipo', max_length=1, choices=TIPOS_CURSOS)

    noturno = models.BooleanField('Noturno?')

    diurno = models.BooleanField('Diurno?')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'CURSO'
