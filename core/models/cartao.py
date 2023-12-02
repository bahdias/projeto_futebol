from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..constants import EnumCartao
from django.core.exceptions import ValidationError

from .estatistica import Estatistica
from .jogador import Jogador
from .jogo import Jogo
from ..choices import CARTAO
from .time import Time


def validate_custom_time_format(value):
    # Verifique se o valor atende a um dos formatos desejados (XX:XX ou XXX:XX)
    if not (len(value) == 5 and value[:2].isdigit() and value[2] == ':' and value[3:].isdigit()) and \
            not (len(value) == 6 and value[:3].isdigit() and value[3] == ':' and value[4:].isdigit()):
        raise ValidationError("O formato do tempo deve ser XX:XX ou XXX:XX.")


class Cartao(models.Model):
    time = models.ForeignKey(
        Time,
        verbose_name="Time",
        on_delete=models.CASCADE,
        related_name='time_cartao',
        null=False,
        blank=False,
        default=None
    )
    jogador = models.ForeignKey(
        Jogador,
        verbose_name="Jogador",
        on_delete=models.CASCADE,
        related_name='jogador_cartao',
        null=True,
        blank=True,
        default=None
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
    tipo = models.SmallIntegerField(
        verbose_name="Tipo de Cartão",
        choices=CARTAO,
        null=False,
        blank=False
    )
    jogo = models.ForeignKey(
        Jogo,
        verbose_name="Jogo",
        on_delete=models.CASCADE,
        related_name='cartao_jogo',
        null=False,
        blank=False
    )

    def clean(self):
        if self.time and self.jogador:
            if self.jogador.time.nome != self.time.nome:
                self.jogador = None
                raise ValidationError("O Jogador selecionado não é integrante do time selecionado.")

    def delete(self, using=None, keep_parents=False):
        estatistica, _ = Estatistica.objects.update_or_create(time=self.time)
        if estatistica:
            if self.tipo is EnumCartao.AMARELO.value:
                estatistica.cartao_amarelo -= Cartao.objects.filter(jogo=self.jogo,
                                                                    time=self.time,
                                                                    tipo=self.tipo).count()
            elif self.tipo is EnumCartao.VERMELHO.value:
                estatistica.cartao_vermelho -= Cartao.objects.filter(jogo=self.jogo,
                                                                     time=self.time,
                                                                     tipo=self.tipo).count()
            estatistica.save()

        super(Cartao, self).delete(using, keep_parents)

    def __str__(self):
        return f'{self.time} em {self.jogo}'

    class Meta:
        verbose_name = u'Cartão'
        verbose_name_plural = u'Cartões'
        app_label = 'core'


@receiver(post_save, sender=Cartao)
def atualizar_estatisticas_com_gol(sender, instance, created, **kwargs):
    try:
        if created:
            estatistica, _ = Estatistica.objects.update_or_create(time=instance.time, torneio=instance.jogo.torneio)
            if estatistica:
                estatistica.cartao_vermelho += sender.objects.filter(jogo=instance.jogo,
                                                                     time=instance.time,
                                                                     tipo=EnumCartao.VERMELHO.value).count()
                estatistica.cartao_amarelo += sender.objects.filter(jogo=instance.jogo,
                                                                    time=instance.time,
                                                                    tipo=EnumCartao.AMARELO.value).count()
                estatistica.save()
    except Exception as e:
        print(e)
