from .constants import EnumPosicao, EnumDesempenho, EnumPreferenciaPe, EnumClassificacao

POSICAO_JOGADOR = (
    (EnumPosicao.GOLEIRO.value, u'Goleiro'),
    (EnumPosicao.ZAGUEIRO.value, u'Zagueiro'),
    (EnumPosicao.LATERAL.value, u'Lateral'),
    (EnumPosicao.VOLANTE.value, u'Volante'),
    (EnumPosicao.MEIA.value, u'Meia'),
    (EnumPosicao.ATACANTE.value, u'Atacante'),
)

PREFERENCIA_PE = (
    (EnumPreferenciaPe.ESQUERDO.value, u'Esquerdo'),
    (EnumPreferenciaPe.DIREITO.value, u'Direito'),
)

DESEMPENHO = (
    (EnumDesempenho.EXCELENTE.value, u'Excelente'),
    (EnumDesempenho.BOM.value, u'Bom'),
    (EnumDesempenho.MEDIO.value, u'Médio'),
    (EnumDesempenho.EM_DESENVOLVIMENTO.value, u'Em desenvolvimento'),
    (EnumDesempenho.PESSIMO.value, u'Péssimo'),
)

CLASSIFICACAO = (
    (EnumClassificacao.CONMEBOL_LIBERTADORES.value, u'Conmebol Libertadores'),
    (EnumClassificacao.CONMEBOL_LIBERTADORES_QUALIFIERS.value, u'Conmebol Libertadores Qualifiers'),
    (EnumClassificacao.CONMEBOL_SUDAMERICANA.value, u'Conmebol Sudamericana'),
    (EnumClassificacao.REBAIXAMENTO.value, u'Rebaixamento'),
)
