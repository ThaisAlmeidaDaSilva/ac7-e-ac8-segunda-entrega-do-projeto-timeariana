from django.db import models

SEMESTRES = (
    (1, '1º Semestre'),
    (2, '2º Semestre')
)

class DisciplinaOfertada(models.Model):

    curso = models.ForeignKey(
        'curriculo.Curso',
        on_delete=models.DO_NOTHING
    )

    disciplina = models.ForeignKey(
        'curriculo.Disciplina',
        on_delete=models.DO_NOTHING
    )

    ano = models.SmallIntegerField('Ano')

    semestre = models.SmallIntegerField(
        'Semestre',
        choices=SEMESTRES
    )

    turma = models.CharField('Turma', max_length=1)

    data_inicio = models.DateField(
        "Data Ínicio",
        null=True,
        blank=True
    )

    data_fim = models.DateField(
        "Data Fim",
        null=True,
        blank=True
    )

    metodologia = models.TextField("Metodologia", blank=True)

    recursos = models.TextField("Recursos", blank=True)

    criterio_de_avaliacao = models.TextField("Critério de Avaliação", blank=True)

    plano_de_aulas = models.TextField("Plano de Aulas", blank=True)

    def __str__(self):
        return '{}-{}-{}-{}'.format(self.ano, self.semestre, self.curso.sigla, self.disciplina.nome)

    class Meta:
        db_table = 'DISCIPLINA_OFERTADA'