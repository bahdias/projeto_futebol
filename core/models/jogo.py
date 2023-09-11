from django.db import models

from .time import Time


class Jogo(models.Model):
    data_partida = models.DateTimeField(
        verbose_name="Data da Partida",
        null=False,
        blank=True
    )
    equipe_casa = models.ForeignKey(
        Time,
        verbose_name="Equipe da Casa",
        on_delete=models.CASCADE,
        related_name='equipe_casa'
    )
    equipe_visitante = models.ForeignKey(
        Time,
        verbose_name="Equipe Visitante",
        on_delete=models.CASCADE,
        related_name='equipe_visitante'
    )
    placar_casa = models.IntegerField(
        verbose_name="Placar da Equipe da Casa",
        null=True,
        blank=True
    )
    placar_visitante = models.IntegerField(
        verbose_name="Placar da Equipe Visitante",
        null=True,
        blank=True
    )
    local = models.CharField(
        verbose_name="Local do Jogo",
        max_length=200
    )
    arbitro = models.CharField(
        verbose_name="Nome do Árbitro Pricipal",
        max_length=200
    )
    tempo_jogo = models.IntegerField(
        verbose_name="Tempo do Jogo (em minutos)",
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.equipe_casa} x {self.equipe_visitante}'

    class Meta:
        verbose_name = u'Jogo'
        verbose_name_plural = u'Jogos'
        app_label = 'core'
