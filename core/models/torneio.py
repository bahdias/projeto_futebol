from django.db import models


class Torneio(models.Model):
    nome = models.CharField(
        verbose_name="Nome do Torneio",
        max_length=200,
        null=False,
        blank=False
    )
    ano = models.DateField(
        verbose_name="Ano do Torneio",
        null=False,
        blank=True,
    )

    def __str__(self):
        return f'{self.nome} {self.ano}'

    class Meta:
        verbose_name = u'Torneio'
        verbose_name_plural = u'Torneios'
        app_label = 'core'
