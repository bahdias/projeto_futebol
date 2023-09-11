from django.db import models

from ..models.jogador import Jogador


class EstatisticasJogador(models.Model):
    equipe = models.CharField(
        verbose_name="Equipe",
        max_length=200
    )
    jogador = models.ForeignKey(
        Jogador,
        on_delete=models.CASCADE,
        related_name='estatisticas_jogador'
    )
    jogos_disputados = models.IntegerField(
        verbose_name="Jogos Disputados",
    )
    partidas_titular = models.IntegerField(
        verbose_name="Partidas como Titular",
    )
    minutos_jogados = models.IntegerField(
        verbose_name="Minutos Jogados",
    )
    gols = models.IntegerField(
        verbose_name="Quantidade de Gols",
        null=True,
        blank=True
    )
    minutos_jogados_gol = models.IntegerField(
        verbose_name="Minutos Jogados por gol",
    )
    assistencia = models.IntegerField(
        verbose_name="Assistências",
        null=True,
        blank=True
    )
    gols_cabeca = models.IntegerField(
        verbose_name="Gols de Cabeça",
    )
    gols_penalti = models.IntegerField(
        verbose_name="Gols de Pênalti",
    )
    chutes_gol = models.IntegerField(
        verbose_name="Chutes ao Gol",
    )
    chutes_fora = models.IntegerField(
        verbose_name="Chutes Fora",
    )
    impedimentos = models.IntegerField(
        verbose_name="Chutes Fora",
    )
    escanteios = models.IntegerField(
        verbose_name="Escanteios",
    )
    cartao_vermelho = models.IntegerField(
        verbose_name="Quantidade de Cartões Vermelhos",
    )
    cartao_amarelo = models.IntegerField(
        verbose_name="Quantidade de Cartões Amarelos",
    )

    def __str__(self):
        return self.equipe.verbose_name

    class Meta:
        verbose_name = u'Estatistica do Jogador'
        verbose_name_plural = u'Estatisticas do Jogador'
        app_label = 'core'
