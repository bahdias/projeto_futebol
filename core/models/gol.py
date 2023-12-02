from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.exceptions import ValidationError

from .estatistica import Estatistica
from .jogador import Jogador
from .jogo import Jogo
from .time import Time


def validate_custom_time_format(value):
    # Verifique se o valor atende a um dos formatos desejados (XX:XX ou XXX:XX)
    if not (len(value) == 5 and value[:2].isdigit() and value[2] == ':' and value[3:].isdigit()) and \
            not (len(value) == 6 and value[:3].isdigit() and value[3] == ':' and value[4:].isdigit()):
        raise ValidationError("O formato do tempo deve ser XX:XX ou XXX:XX.")


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
    tempo = models.CharField(
        verbose_name="Tempo em que registrou",
        max_length=6,
        validators=[validate_custom_time_format]
    )
    tempo_acrescimo = models.CharField(
        verbose_name="Tempo de acrescimo",
        max_length=6,
        validators=[validate_custom_time_format]
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
        marcou, _ = Estatistica.objects.update_or_create(time=self.time_marcou)
        if marcou:
            marcou.gols_marcados -= 1
            marcou.save()
            marcou.set_saldo_gols()
        sofreu, _ = Estatistica.objects.update_or_create(time=self.time_sofreu)
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
        marcou, _ = Estatistica.objects.update_or_create(time=instance.time_marcou,
                                                         torneio=instance.jogo.torneio)
        if marcou:
            marcou.gols_marcados += 1
            marcou.save()
            marcou.set_saldo_gols()
        sofreu, _ = Estatistica.objects.update_or_create(time=instance.time_sofreu,
                                                         torneio=instance.jogo.torneio)
        if sofreu:
            sofreu.gols_sofridos += 1
            sofreu.save()
            sofreu.set_saldo_gols()
