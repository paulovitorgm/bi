from django.db import models


class EntidadeModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=14, blank=False, null=False)

    class Meta:
        db_table = 'Entidade'
        verbose_name = 'Entidade'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return self.nome
