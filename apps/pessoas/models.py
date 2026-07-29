from django.db import models

SEXO = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)


class PessoaModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=180, blank=False, null=False)
    matricula = models.CharField(max_length=8, unique=True, blank=False, null=False)
    sexo = models.CharField(max_length=1, choices=SEXO, null=False, blank=False)

    class Meta:
        db_table = 'Pessoas'

    def __str__(self):
        return self.nome
