from django.db import models

from .time import Time


class GolTime(models.Model):
    time = models.ForeignKey(
        Time,
        verbose_name="Time",
        on_delete=models.CASCADE,
        related_name='gol_time',
        null=False,
        blank=False
    )
    tempo = models.DateTimeField(
        verbose_name="Tempo em que registrou",
        null=False,
        blank=False
    )
    contra = models.BooleanField(
        verbose_name="Foi Contra?",
    )
    marcado = models.BooleanField(
        verbose_name="Marcado?",
    )
    sofrido = models.BooleanField(
        verbose_name="Sofrido?",
    )

    def __str__(self):
        return f'{self.time}'

    class Meta:
        verbose_name = u'Gol do Time'
        verbose_name_plural = u'Gols do Time'
        app_label = 'core'
