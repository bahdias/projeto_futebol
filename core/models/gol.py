from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.exceptions import ValidationError

from .competido_por import CompetidoPor
from .jogador import Jogador
from .jogo import Jogo
from .time import Time


class Gol(models.Model):
    jogador = models.ForeignKey(
        Jogador,
        verbose_name="Jogador",
        on_delete=models.CASCADE,
        related_name='gol_jogador',
        null=False,
        blank=False
    )
    time_marcou = models.ForeignKey(
        Time,
        verbose_name="Time que Marcou",
        on_delete=models.CASCADE,
        related_name='gol_time_marcou',
        null=False,
    )
    time_sofreu = models.ForeignKey(
        Time,
        verbose_name="Time que Sofreu",
        on_delete=models.CASCADE,
        related_name='gol_time_sofreu',
        null=False,
    )
    assistido = models.ForeignKey(
        Jogador,
        verbose_name="Assistencia",
        on_delete=models.CASCADE,
        related_name='gol_jogador_assistido',
        null=True,
        blank=True
    )
    tempo = models.DateTimeField(
        verbose_name="Tempo em que registrou",
        null=False,
        blank=False
    )
    foi_contra = models.BooleanField(
        verbose_name="Contra?",
    )
    jogo = models.ForeignKey(
        Jogo,
        verbose_name="Jogo",
        on_delete=models.CASCADE,
        related_name='gol_jogo',
        null=False,
        blank=False
    )

    def clean(self):
        if self.time_marcou == self.time_sofreu:
            raise ValidationError("O time que marcou não pode ser o mesmo que o time que sofreu.")

    def delete(self, using=None, keep_parents=False):
        marcou, _ = CompetidoPor.objects.update_or_create(time=self.time_marcou)
        if marcou:
            marcou.gols_marcados -= 1
            marcou.save()
            marcou.set_saldo_gols()
        sofreu, _ = CompetidoPor.objects.update_or_create(time=self.time_sofreu)
        if sofreu:
            sofreu.gols_sofridos -= 1
            sofreu.save()
            sofreu.set_saldo_gols()

        super(Gol, self).delete(using, keep_parents)

    def __str__(self):
        return f'{self.tempo}'

    class Meta:
        verbose_name = u'Gol'
        verbose_name_plural = u'Gols'
        app_label = 'core'


@receiver(post_save, sender=Gol)
def atualizar_estatisticas_com_gol(sender, instance, created, **kwargs):
    if created:
        marcou, _ = CompetidoPor.objects.update_or_create(time=instance.time_marcou,
                                                          torneio=instance.jogo.torneio)
        if marcou:
            marcou.gols_marcados += 1
            marcou.save()
            marcou.set_saldo_gols()
        sofreu, _ = CompetidoPor.objects.update_or_create(time=instance.time_sofreu,
                                                          torneio=instance.jogo.torneio)
        if sofreu:
            sofreu.gols_sofridos += 1
            sofreu.save()
            sofreu.set_saldo_gols()

