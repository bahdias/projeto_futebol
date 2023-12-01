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
        max_length=3,
        null=False,
        blank=False
    )
    fundacao = models.DateField(
        verbose_name='Fundado em',
        null=True,
        blank=True
    )
    pais = models.CharField(
        verbose_name="País da equipe",
        max_length=2,
    )
    escudo_url = models.URLField(
        verbose_name='URL do Escudo',
        max_length=500,
        null=True,
        blank=True
    )
    tecnico = models.CharField(
        verbose_name="Técnico da Equipe",
        max_length=200
    )
    cor_primaria = ColorField()
    cor_secundaria = ColorField()

    def __str__(self):
        return f'{self.nome} - {self.abreviacao}'

    def save(self, *args, **kwargs):
        self.pais = self.pais.upper()
        self.abreviacao = self.abreviacao.upper()
        super(Time, self).save(*args, **kwargs)

    def get_nome(self):
        return self.abreviacao

    class Meta:
        verbose_name = u'Time'
        verbose_name_plural = u'Times'
        app_label = 'core'
