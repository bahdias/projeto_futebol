from django.db import models

from ..choices import POSICAO_JOGADOR, DESEMPENHO, PREFERENCIA_PE


class Jogador(models.Model):
    nome = models.CharField(
        verbose_name="Nome do Jogador",
        max_length=200
    )
    idade = models.IntegerField(
        verbose_name="Idade",
    )
    nacionalidade = models.CharField(
        verbose_name="Nacionalidade",
        max_length=200
    )
    posicao = models.SmallIntegerField(
        verbose_name="Posição do Jogador",
        choices=POSICAO_JOGADOR,
    )
    peso = models.FloatField(
        verbose_name="Peso",
    )
    altura = models.FloatField(
        verbose_name="Altura",
    )
    preferencia_pe = models.SmallIntegerField(
        verbose_name="Preferência de pé",
        choices=PREFERENCIA_PE,
    )
    avaliacao_desempenho = models.SmallIntegerField(
        verbose_name="Avaliação de Desempenho",
        choices=DESEMPENHO,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.nome} - {self.nacionalidade}'

    class Meta:
        verbose_name = u'Jogador'
        verbose_name_plural = u'Jogadores'
        app_label = 'core'
