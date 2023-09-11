from .constants import EnumPosicao, EnumDesempenho, EnumPreferenciaPe, EnumClassificacao

POSICAO_JOGADOR = (
    (EnumPosicao.GOLEIRO, u'Goleiro'),
    (EnumPosicao.ZAGUEIRO, u'Zagueiro'),
    (EnumPosicao.LATERAL, u'Lateral'),
    (EnumPosicao.VOLANTE, u'Volante'),
    (EnumPosicao.MEIA, u'Meia'),
    (EnumPosicao.ATACANTE, u'Atacante'),
)

PREFERENCIA_PE = (
    (EnumPreferenciaPe.ESQUERDO, u'Esquerdo'),
    (EnumPreferenciaPe.DIREITO, u'Direito'),
)

DESEMPENHO = (
    (EnumDesempenho.EXCELENTE, u'Excelente'),
    (EnumDesempenho.BOM, u'Bom'),
    (EnumDesempenho.MEDIO, u'Médio'),
    (EnumDesempenho.EM_DESENVOLVIMENTO, u'Em desenvolvimento'),
    (EnumDesempenho.PESSIMO, u'Péssimo'),
)

CLASSIFICACAO = (
    (EnumClassificacao.CONMEBOL_LIBERTADORES, u'Conmebol Libertadores'),
    (EnumClassificacao.CONMEBOL_LIBERTADORES_QUALIFIERS, u'Conmebol Libertadores Qualifiers'),
    (EnumClassificacao.CONMEBOL_SUDAMERICANA, u'Conmebol Sudamericana'),
    (EnumClassificacao.REBAIXAMENTO, u'Rebaixamento'),
)
