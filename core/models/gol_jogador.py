from django.db import models

from .jogador import Jogador


class GolJogador(models.Model):
    jogador = models.ForeignKey(
        Jogador,
        verbose_name="Jogador",
        on_delete=models.CASCADE,
        related_name='gol_jogador',
        null=False,
        blank=False
    )
    tempo = models.DateTimeField(
        verbose_name="Tempo em que registrou",
        null=False,
        blank=False
    )
    contra = models.BooleanField(
        verbose_name="Foi Contra?",
    )
    marcado = models.BooleanField(
        verbose_name="Marcado?",
    )
    assistido = models.BooleanField(
        verbose_name="Assistido?",
    )

    def __str__(self):
        return f'{self.jogador}'

    class Meta:
        verbose_name = u'Gol do Jogador'
        verbose_name_plural = u'Gols do Jogador'
        app_label = 'core'
