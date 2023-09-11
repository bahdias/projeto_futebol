from django.db import models

from ..models.jogador import Jogador


class Carreira(models.Model):
    equipe = models.CharField(
        verbose_name="Equipe",
        max_length=200
    )
    jogador = models.ForeignKey(
        Jogador,
        on_delete=models.CASCADE,
        related_name='carreiras'
    )
    jogos = models.IntegerField(
        verbose_name="Jogos",
    )
    gols = models.IntegerField(
        verbose_name="Gols",
    )

    class Meta:
        verbose_name = u'Carreira'
        verbose_name_plural = u'Carreiras'
        app_label = 'core'
