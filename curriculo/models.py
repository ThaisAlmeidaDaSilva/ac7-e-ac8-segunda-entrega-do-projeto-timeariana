from django.db import models

# Create your models here.
TIPOS = (
('TECNICO','Técnico'),
('GRADUACAO','Graduação'),
('PGRADUACAO',' Pós-graduação')
)

class Curso(models.Model):
    

    nome = models.CharField(
        'Nome', 
        max_length=120
        )
    sigla = models.CharField(
        'Sigla', 
        max_length=5, 
        unique =True
        )
    tipo = models.CharField(
        'Tipo de Curso', 
        max_length=30,
        choices=TIPOS
        )

    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'CURSO'


class Disciplina(models.Model):
    nome = models.CharField('nome', max_length=120)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome
        
    class Meta:
        db_table = 'DISCIPLINA'