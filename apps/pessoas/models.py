from django.db import models

from apps.base.models import ModeloAuditavel


class UnidadeDeLotacao(models.Model):
    sigla = models.CharField(max_length=60, blank=True, null=True)
    nome = models.CharField(max_length=180, blank=False, null=False)
    


class PessoaModel(ModeloAuditavel):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        max_length=180,
        blank=False,
        null=False
    )
    matricula = models.CharField(
        max_length=20, 
        unique=True, 
        blank=True, 
        null=True
    )
    unidade_de_lotacao = models.ForeignKey(
        UnidadeDeLotacao, 
        on_delete=models.SET_NULL,
        blank=False,
        null=True
    )

    class Meta:
        db_table = 'Pessoas'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def clean(self):
        super().clean()

        if self.matricula:
            self.matricula = self.matricula.strip()

            if self.matricula == '':  # ruff: ignore[compare-to-empty-string]
                self.matricula = None
