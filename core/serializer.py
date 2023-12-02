from rest_framework import serializers

from .models.cartao import Cartao
from .models.estatistica import Estatistica
from .models.gol import Gol
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


class GolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gol
        fields = '__all__'


class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = '__all__'


class ListarJogosSerializer(serializers.ModelSerializer):
    gols = GolSerializer(many=True, read_only=True)
    cartoes = CartaoSerializer(many=True, read_only=True)

    class Meta:
        model = Jogo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        gols_data = GolSerializer(instance.gol_jogo.all(), many=True).data
        representation['gols'] = gols_data
        cartoes_data = CartaoSerializer(instance.cartao_jogo.all(), many=True).data
        representation['cartoes'] = cartoes_data

        return representation


class ListarEstatisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estatistica
        fields = '__all__'


class ListarTorneiosSerializer(serializers.ModelSerializer):
    estatisticas = ListarEstatisticaSerializer(many=True, read_only=True)
    class Meta:
        model = Torneio
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        estatisticas_data = ListarEstatisticaSerializer(instance.estatistica_torneio.all(), many=True).data
        representation['estatistica'] = estatisticas_data

        return representation


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