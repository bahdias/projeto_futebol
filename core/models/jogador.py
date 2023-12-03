from datetime import date

from django.db import models

from .time import Time
from ..choices import POSICAO_JOGADOR, PREFERENCIA_PE


class Jogador(models.Model):
    time = models.ForeignKey(
        Time,
        verbose_name="Time",
        on_delete=models.CASCADE,
        related_name='time_jogador',
        null=True,
        blank=True
    )
    nome = models.CharField(
        verbose_name="Nome do Jogador",
        max_length=200
    )
    apelido = models.CharField(
        verbose_name="Apelido do Jogador",
        max_length=200
    )
    idade = models.IntegerField(
        verbose_name="Idade",
        null=False,
        blank=True
    )
    pais = models.CharField(
        verbose_name="País",
        max_length=2,
    )
    dt_nascimento = models.DateField(
        verbose_name='Data de nascimento',
        null=False,
        blank=False
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
    numero_camisa = models.IntegerField(
        verbose_name="Número da Camisa",
        null=True,
        blank=True
    )
    imagem = models.URLField(
        verbose_name='Imagem do Jogador',
        max_length=500,
        null=True,
        blank=True
    )

    def calcular_idade(self):
        if self.dt_nascimento:
            today = date.today()
            delta = today - self.dt_nascimento
            years = delta.days // 365
            return years
        return None

    def save(self, *args, **kwargs):
        self.pais = self.pais.upper()
        self.idade = self.calcular_idade()
        super(Jogador, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.nome} - {self.time.get_nome()}'

    class Meta:
        verbose_name = u'Jogador'
        verbose_name_plural = u'Jogadores'
        app_label = 'core'
