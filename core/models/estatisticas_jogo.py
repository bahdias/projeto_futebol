from django.db import models

from ..models.jogo import Jogo


class EstatisticasJogo(models.Model):
    equipe = models.CharField(
        verbose_name="Equipe",
        max_length=200
    )
    jogo = models.ForeignKey(
        Jogo,
        verbose_name="Jogo",
        on_delete=models.CASCADE,
        related_name='jogo'
    )
    posse_de_bola = models.IntegerField(
        verbose_name="Posses de Bola",
        help_text="Em Porcentagem"
    )
    finalizacoes = models.IntegerField(
        verbose_name="Finalizações",
    )
    finalizacoes_gol = models.IntegerField(
        verbose_name="Finalizações no Gol",
    )
    escanteios = models.IntegerField(
        verbose_name="Escanteios",
    )
    faltas = models.IntegerField(
        verbose_name="Faltas",
    )
    impedimentos = models.IntegerField(
        verbose_name="Chutes Fora",
    )
    cobranca_lateral = models.IntegerField(
        verbose_name="Cobrança Lateral",
    )
    defesas = models.IntegerField(
        verbose_name="Defesas",
    )

    class Meta:
        verbose_name = u'Estatistica do Jogo'
        verbose_name_plural = u'Estatisticas do Jogo'
        app_label = 'core'
