from django.db import models

from .jogador import Jogador
from ..choices import CLASSIFICACAO


class Time(models.Model):
    nome = models.CharField(
        verbose_name="Nome da Equipe",
        max_length=200
    )
    sigla = models.CharField(
        verbose_name="Sigla da Equipe",
        max_length=200
    )
    fundacao = models.DateField(
        verbose_name='Fundado em',
        null=True,
        blank=True
    )
    cidade = models.CharField(
        verbose_name="Cidade sede da equipe",
        max_length=200
    )
    estadio = models.CharField(
        verbose_name="Estádio",
        max_length=200,
        help_text='Estádio em que a equipe joga'
    )
    cores = models.CharField(
        verbose_name="Cores da Equipe",
        max_length=200
    )
    escudo_url = models.URLField(
        verbose_name='URL do Escudo',
        max_length=500,
        null=True,
        blank=True
    )
    escudo = models.FileField(
        verbose_name='Escudo',
        null=True, blank=True,
        upload_to='cliente'
    )
    anexado_em = models.DateField(
        verbose_name='Anexado em',
        null=True,
        blank=True
    )
    jogadores = models.ManyToManyField(
        Jogador,
        verbose_name='Goleiros',
    )
    treinador = models.CharField(
        verbose_name="Treinador da Equipe",
        max_length=200
    )
    classificacao = models.SmallIntegerField(
        verbose_name="Classificação",
        choices=CLASSIFICACAO,
    )
    pontos = models.IntegerField(
        verbose_name="Pontuação",
    )

    def __str__(self):
        return f'{self.nome} - {self.sigla}'

    class Meta:
        verbose_name = u'Time'
        verbose_name_plural = u'Times'
        app_label = 'core'
