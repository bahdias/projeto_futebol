from django.db import models

from ..choices import CARTAO
from .jogador import Jogador
from .jogo import Jogo


class CartaoJogador(models.Model):
    jogador = models.ForeignKey(
        Jogador,
        verbose_name="Time",
        on_delete=models.CASCADE,
        related_name='time_jogador_cartao',
        null=False,
        blank=False
    )
    jogo = models.ForeignKey(
        Jogo,
        verbose_name="Jogo",
        on_delete=models.CASCADE,
        related_name='jogo_cartao_jogador',
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
        return f'{self.jogador} em {self.jogo}'

    class Meta:
        verbose_name = u'Cartão do Jogador'
        verbose_name_plural = u'Cartões do Jogador'
        app_label = 'core'
