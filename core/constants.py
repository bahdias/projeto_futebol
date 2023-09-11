from enum import Enum


class EnumPosicao(Enum):
    GOLEIRO = 0
    ZAGUEIRO = 1
    LATERAL = 2
    VOLANTE = 3
    MEIA = 4
    ATACANTE = 5


class EnumPreferenciaPe(Enum):
    ESQUERDO = 0
    DIREITO = 1


class EnumDesempenho(Enum):
    EXCELENTE = 0
    BOM = 1
    MEDIO = 2
    EM_DESENVOLVIMENTO = 3
    PESSIMO = 4


class EnumClassificacao(Enum):
    CONMEBOL_LIBERTADORES = 0
    CONMEBOL_LIBERTADORES_QUALIFIERS = 1
    CONMEBOL_SUDAMERICANA = 2
    REBAIXAMENTO = 3
