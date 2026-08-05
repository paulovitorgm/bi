from django.db import models


class TipoInstrumento(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome
