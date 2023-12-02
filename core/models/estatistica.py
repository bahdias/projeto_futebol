
from django.db import models

from .time import Time
from .torneio import Torneio


class Estatistica(models.Model):
    time = models.ForeignKey(
        Time,
        verbose_name="Time",
        on_delete=models.CASCADE,
        related_name='estatistica_time',
        null=False,
        blank=False
    )
    torneio = models.ForeignKey(
        Torneio,
        verbose_name="Torneio",
        on_delete=models.CASCADE,
        related_name='estatistica_torneio',
        null=False,
        blank=False
    )
    vitorias = models.IntegerField(
        verbose_name="Vitorias",
        default=0
    )
    derrotas = models.IntegerField(
        verbose_name="Derrotas",
        default=0
    )
    empates = models.IntegerField(
        verbose_name="Empates",
        default=0
    )
    gols_marcados = models.IntegerField(
        verbose_name="Gols Marcados",
        default=0
    )
    gols_sofridos = models.IntegerField(
        verbose_name="Gols Sofridos",
        default=0
    )
    cartao_amarelo = models.IntegerField(
        verbose_name="Cartão Amarelo",
        default=0
    )
    cartao_vermelho = models.IntegerField(
        verbose_name="Cartão Vermelho",
        default=0
    )
    saldo_gols = models.IntegerField(
        verbose_name="Saldo de Gols",
        default=0
    )
    pontuacao = models.IntegerField(
        verbose_name="Pontuação",
        default=0
    )

    def set_saldo_gols(self):
        if self.gols_marcados and self.gols_sofridos:
            self.saldo_gols = self.gols_marcados-self.gols_sofridos

    def save(self, *args, **kwargs):
        self.set_saldo_gols()
        self.clean()
        super().save()

    def __str__(self):
        return f'{self.time} ({self.torneio})'

    class Meta:
        verbose_name = u'Estatistica'
        verbose_name_plural = u'Estatisticas'
        app_label = 'core'
