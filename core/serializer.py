from rest_framework import serializers

from .models.competido_por import CompetidoPor
from .models.jogador import Jogador
from .models.jogo import Jogo
from .models.time import Time
from .models.torneio import Torneio


class ListarJogadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'


class ListarTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class ListarJogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'


class ListarTorneiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneio
        fields = '__all__'


class ListarEstatisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetidoPor
        fields = '__all__'


class ListarTimesTorneiosSerializer(serializers.ModelSerializer):
    data_hora_inicio = serializers.DateTimeField(
        format='%d/%m/%Y %H:%M',
        input_formats=['%d/%m/%Y %H:%M'],
        required=False
    )
    class Meta:
        model = Jogo
        fields = (
            'data_hora_inicio ',
            'estadio',
            'time_casa',
            'time_visitante',
            'torneio',
            'acabou',
        )