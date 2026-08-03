from django.db import models


class SexoChoices(models.TextChoices):
    MASC = 'M', 'Masculino'
    FEM = 'F', 'Feminino'


class PessoaModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=180, blank=False, null=False)
    matricula = models.CharField(max_length=20, unique=True, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SexoChoices, null=False, blank=False)

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
