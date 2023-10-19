from .constants import EnumPosicao, EnumPreferenciaPe, EnumCartao

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

CARTAO = (
    (EnumCartao.AMARELO.value, u'Amarelo'),
    (EnumCartao.VERMELHO.value, u'Vermelho'),
)
