from django.db import models

from ..choices import CARTAO
from .jogo import Jogo
from .time import Time


class CartaoTime(models.Model):
    time = models.ForeignKey(
        Time,
        verbose_name="Time",
        on_delete=models.CASCADE,
        related_name='time_cartao',
        null=False,
        blank=False
    )
    jogo = models.ForeignKey(
        Jogo,
        verbose_name="Jogo",
        on_delete=models.CASCADE,
        related_name='jogo_cartao_time',
        null=False,
        blank=False
    )
    tempo = models.DateTimeField(
        verbose_name="Tempo em que registrou",
        null=False,
        blank=False
    )
    tipo = models.SmallIntegerField(
        verbose_name="Tipo de Cartão",
        choices=CARTAO,
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.time} em {self.jogo}'

    class Meta:
        verbose_name = u'Cartão do Time'
        verbose_name_plural = u'Cartões do Time'
        app_label = 'core'
