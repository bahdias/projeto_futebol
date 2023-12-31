

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .estatistica import Estatistica
from .time import Time
from .torneio import Torneio


class Jogo(models.Model):
    data_hora_inicio = models.DateTimeField(
        verbose_name="Data de Início da Partida",
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
    acabou = models.BooleanField(
        verbose_name="O Jogo Acabou?",
        default=False
    )

    def __str__(self):
        return f'{self.time_casa} x {self.time_visitante}'

    class Meta:
        verbose_name = u'Jogo'
        verbose_name_plural = u'Jogos'
        app_label = 'core'


@receiver(post_save, sender=Jogo)
def atualizar_pontuacao(sender, instance, created, **kwargs):
    from .gol import Gol
    if instance.acabou:
        time_casa_gols = Gol.objects.filter(jogo=instance, time_marcou=instance.time_casa).count()
        time_visitante_gols = Gol.objects.filter(jogo=instance, time_marcou=instance.time_visitante).count()
        if time_casa_gols > time_visitante_gols:
            estatistica_casa, _ = Estatistica.objects.update_or_create(time=instance.time_casa)
            estatistica_visitante, _ = Estatistica.objects.update_or_create(time=instance.time_visitante)
            estatistica_casa.vitorias += 1
            estatistica_casa.pontuacao = (estatistica_casa.vitorias * 3) + estatistica_casa.empates
            estatistica_visitante.derrotas += 1
            estatistica_visitante.save()
            estatistica_casa.save()
        elif time_casa_gols < time_visitante_gols:
            estatistica_visitante, _ = Estatistica.objects.update_or_create(time=instance.time_visitante)
            estatistica_casa, _ = Estatistica.objects.update_or_create(time=instance.time_casa)
            estatistica_visitante.vitorias += 1
            estatistica_visitante.pontuacao = (estatistica_visitante.vitorias * 3) + estatistica_visitante.empates
            estatistica_casa.derrotas += 1
            estatistica_visitante.save()
            estatistica_casa.save()
        else:
            estatistica_visitante, _ = Estatistica.objects.update_or_create(time=instance.time_visitante)
            estatistica_casa, _ = Estatistica.objects.update_or_create(time=instance.time_casa)
            estatistica_visitante.empates += 1
            estatistica_casa.empates += 1
            estatistica_visitante.pontuacao = (estatistica_visitante.vitorias * 3) + estatistica_visitante.empates
            estatistica_casa.pontuacao = (estatistica_casa.vitorias * 3) + estatistica_casa.empates
            estatistica_visitante.save()
            estatistica_casa.save()
