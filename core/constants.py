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


class EnumCartao(Enum):
    AMARELO = 0
    VERMELHO = 1


class EnumEntidade(Enum):
    JOGADOR = 0
    TIME = 1
