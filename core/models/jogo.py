

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .competido_por import CompetidoPor
from .time import Time
from .torneio import Torneio


class Jogo(models.Model):
    data_inicio = models.DateTimeField(
        verbose_name="Data de Início da Partida",
        null=False,
        blank=False
    )
    data_final = models.DateTimeField(
        verbose_name="Data de Término da Partida",
        null=False,
        blank=False
    )
    estadio = models.CharField(
        verbose_name="Estádio",
        max_length=200,
        help_text='Estádio em que o jogo ocorreu',
        null=False,
        blank=False
    )
    time_casa = models.ForeignKey(
        Time,
        verbose_name="Time da Casa",
        on_delete=models.CASCADE,
        related_name='time_casa'
    )
    time_visitante = models.ForeignKey(
        Time,
        verbose_name="Time Visitante",
        on_delete=models.CASCADE,
        related_name='time_visitante',
        null=False,
        blank=False
    )
    torneio = models.ForeignKey(
        Torneio,
        verbose_name="Torneio",
        on_delete=models.CASCADE,
        related_name='torneio_jogo',
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.time_casa} x {self.time_visitante}'

    class Meta:
        verbose_name = u'Jogo'
        verbose_name_plural = u'Jogos'
        app_label = 'core'


def pontuacao(quantidade):
    if quantidade.gols_marcados > quantidade.gols_sofridos:
        quantidade.vitorias += 1
    elif quantidade.gols_marcados < quantidade.gols_sofridos:
        quantidade.derrotas += 1
    else:
        quantidade.empates += 1
    quantidade.pontuacao = (quantidade.vitorias * 3) + quantidade.empates
    quantidade.save()


@receiver(post_save, sender=Jogo)
def atualizar_pontuacao(sender, instance, created, **kwargs):
    tempo_atual = timezone.now()
    if instance.data_final <= tempo_atual:
        marcou, _ = CompetidoPor.objects.update_or_create(time=instance.time_casa)
        pontuacao(marcou)

        sofreu, _ = CompetidoPor.objects.update_or_create(time=instance.time_visitante)
        pontuacao(sofreu)
