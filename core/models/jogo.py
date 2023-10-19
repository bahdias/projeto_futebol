from django.db import models

from .time import Time
from .torneio import Torneio


class Jogo(models.Model):
    data_partida = models.DateTimeField(
        verbose_name="Data da Partida",
        null=False,
        blank=True
    )
    estadio = models.CharField(
        verbose_name="Estádio",
        max_length=200,
        help_text='Estádio em que o jogo ocorreu',
        null=False,
        blank=False
    )
    time_casa = models.ForeignKey(
        Time,
        verbose_name="Time da Casa",
        on_delete=models.CASCADE,
        related_name='time_casa'
    )
    time_visitante = models.ForeignKey(
        Time,
        verbose_name="Time Visitante",
        on_delete=models.CASCADE,
        related_name='time_visitante',
        null=False,
        blank=False
    )
    torneio = models.ForeignKey(
        Torneio,
        verbose_name="Torneio",
        on_delete=models.CASCADE,
        related_name='torneio_jogo',
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.time_casa} x {self.time_visitante}'

    class Meta:
        verbose_name = u'Jogo'
        verbose_name_plural = u'Jogos'
        app_label = 'core'
