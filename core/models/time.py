from colorfield.fields import ColorField
from django.db import models


class Time(models.Model):
    nome = models.CharField(
        verbose_name="Nome da Equipe",
        max_length=200,
        null=False,
        blank=False
    )
    abreviacao = models.CharField(
        verbose_name="Sigla/Abreviação da Equipe",
        max_length=200,
        null=False,
        blank=False
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
    tecnico = models.CharField(
        verbose_name="Técnico da Equipe",
        max_length=200
    )
    primeira_cor = ColorField()
    segunda_cor = ColorField()

    def __str__(self):
        return f'{self.nome} - {self.abreviacao}'

    class Meta:
        verbose_name = u'Time'
        verbose_name_plural = u'Times'
        app_label = 'core'
