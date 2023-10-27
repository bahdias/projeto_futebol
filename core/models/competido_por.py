from django.db import models

from .cartao import Cartao
from .time import Time
from .torneio import Torneio


class CompetidoPor(models.Model):
    time = models.ForeignKey(
        Time,
        verbose_name="Time",
        on_delete=models.CASCADE,
        related_name='competido_time',
        null=False,
        blank=False
    )
    torneio = models.ForeignKey(
        Torneio,
        verbose_name="Torneio",
        on_delete=models.CASCADE,
        related_name='competido_torneio',
        null=False,
        blank=False
    )
    vitorias = models.IntegerField(
        verbose_name="Vitorias",
    )
    derrotas = models.IntegerField(
        verbose_name="Derrotas",
    )
    empates = models.IntegerField(
        verbose_name="Empates",
    )
    gols_marcados = models.IntegerField(
        verbose_name="Gols Marcados",
    )
    gols_sofridos = models.IntegerField(
        verbose_name="Gols Sofridos",
    )
    cartao = models.ForeignKey(
        Cartao,
        verbose_name="Cartao",
        on_delete=models.CASCADE,
        related_name='cartao',
    )
    saldo_gols = models.IntegerField(
        verbose_name="Saldo de Gols",
    )
    pontuacao = models.IntegerField(
        verbose_name="Pontuação",
    )

    def __str__(self):
        return f'{self.time} ({self.torneio})'

    class Meta:
        verbose_name = u'Competido por'
        verbose_name_plural = u'Competidos por'
        app_label = 'core'
