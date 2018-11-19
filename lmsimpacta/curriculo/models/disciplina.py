from django.db import models

STATUS = (
    ('ABERTO','Aberta'),
    ('FECHADO', 'Fechada')
)

class Disciplina(models.Model):

    nome = models.CharField(
        'Nome',
        max_length=30,
        unique=True
    )

    identificador = models.CharField(
        'Identificador',
        max_length=30,
        unique=True
    )

    data = models.DateField(
        "Data de Início",
        auto_now_add=True
    )

    status = models.CharField(
        "Status",
        max_length=10,
        choices=STATUS
    )

    carga_horaria = models.SmallIntegerField(
        "Carga Horária"
    )

    percentual_pratico = models.SmallIntegerField(
        "Percentual Prático"
    )

    percentual_teorico = models.SmallIntegerField(
        "Percentual Teórico"
    )

    plano_de_ensino = models.TextField(
        "Plano de Ensino",
        blank=True
    )

    competencias = models.TextField(
        "Competências",
        blank=True
    )

    habilidades = models.TextField(
        "Habilidades",
        blank=True
    )
    
    ementa = models.TextField(
        "Ementa",
        blank=True
    )

    conteudo_programatico = models.TextField(
        "Conteúdo Programático",
        blank=True
    )

    bibliografia_basica = models.TextField(
        "Bibliografia Básica",
        blank=True
    )

    bibliografia_complementar = models.TextField(
        "Bibliografia Complementar",
        blank=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'DISCIPLINA'
