from datetime import datetime
from django.db import models

class Aluno(models.Model):

    nome = models.CharField(
        "Nome Completo",
        max_length=155
    )

    email = models.EmailField("E-mail")

    celular = models.CharField(
        "Celular", 
        max_length=11
    )

    ra = models.IntegerField(
        "RA"
    )

    foto = models.ImageField(
        "Foto",
        null=True,
        blank=True
    )

    usuario = models.ForeignKey(
        'contas.Usuario',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.ra:
            hoje = datetime.now()
            ano = (hoje.year % 1000).__str__()
            semestre = '1' if hoje.month <=6 else '2'
            ra_prefixo = ano + semestre
            
            ra_max = Aluno.objects.filter(ra__startswith=ra_prefixo).aggregate(models.Max('ra'))['ra__max']
            self.ra = ra_max + 1 if ra_max else int(ra_prefixo+'0001')
            
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'ALUNO'