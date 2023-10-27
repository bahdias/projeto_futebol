from django.db import models

from .jogador import Jogador
from ..choices import CARTAO, ENTIDADE
from .jogo import Jogo
from .time import Time
from ..constants import EnumEntidade


class Cartao(models.Model):
    time = models.ForeignKey(
        Time,
        verbose_name="Time",
        on_delete=models.CASCADE,
        related_name='time_cartao',
        null=True,
        blank=True,
        default=None
    )
    jogador = models.ForeignKey(
        Jogador,
        verbose_name="Jogador",
        on_delete=models.CASCADE,
        related_name='jogador_cartao',
        null=True,
        blank=True,
        default=None
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

    def save(self, *args, **kwargs):
        if self is not None:
            if self.time is not None:
                self.jogador = None
            if self.jogador is not None:
                self.time = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.time} em {self.jogo}'

    class Meta:
        verbose_name = u'Cartão do Time'
        verbose_name_plural = u'Cartões do Time'
        app_label = 'core'
