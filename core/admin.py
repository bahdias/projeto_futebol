from django.contrib import admin

from .models.carreira import Carreira
from .models.estatisticas_jogador import EstatisticasJogador
from .models.estatisticas_jogo import EstatisticasJogo
from .models.jogador import Jogador
from .models.jogo import Jogo
from .models.time import Time


class CarreiraAdmin(admin.TabularInline):
    model = Carreira
    extra = 0
    fieldsets = (
        (
            "CARREIRA PROFISSIONAL",
            {
                "fields": (
                    (
                        "equipe",
                        "jogos",
                        "gols",
                    ),
                ),
            },
        ),
    )


class EstatisticasJogadorAdmin(admin.TabularInline):
    model = EstatisticasJogador
    extra = 0
    fieldsets = (
        (
            "EQUIPE",
            {
                "fields": (
                    (
                        "equipe",
                    ),
                ),
            },
        ),
        (
            "ESTATISTICAS",
            {
                "fields": (
                    (
                        "jogos_disputados",
                        "partidas_titular",
                    ),
                    (
                        "assistencia",
                        "impedimentos",
                        "escanteios",
                    ),
                )
            },
        ),
        (
            "TEMPOS",
            {
                "fields": (
                    (
                        "minutos_jogados",
                        "minutos_jogados_gol",
                    ),
                )
            },
        ),
        (
            "GOLS",
            {
                "fields": (
                    (
                        "gols",
                        "gols_cabeca",
                        "gols_penalti",
                    ),
                    (
                        "chutes_gol",
                        "chutes_fora",
                    ),
                )
            },
        ),
        (
            "CARTÕES",
            {
                "fields": (
                    (
                        "cartao_vermelho",
                        "cartao_amarelo",
                    ),
                ),
            },
        ),
    )


class EstatisticasJogoAdmin(admin.TabularInline):
    model = EstatisticasJogo
    extra = 0
    fieldsets = (
        (
            "ESTATISTICAS",
            {
                "fields": (
                    (
                        "posse_de_bola",
                        "finalizacoes",
                        "finalizacoes_gol",
                        "cobranca_lateral",
                    ),
                    (
                        "escanteios",
                        "faltas",
                        "impedimentos",
                        "defesas",
                    ),
                )
            },
        ),
    )


class JogadorAdmin(admin.ModelAdmin):
    model = Jogador
    search_fields = ('nome', 'posicao', 'idade',)
    list_display = ('nome', 'nacionalidade', 'posicao')
    inlines = [
        CarreiraAdmin,
        EstatisticasJogadorAdmin,
    ]

    fieldsets = (
        (
            "PERFIL",
            {
                "fields": (
                    (
                        "nome",
                        "idade",
                        "nacionalidade",
                    ),
                    (
                        "peso",
                        "altura",
                    ),
                    (
                        "posicao",
                        "preferencia_pe",
                    ),
                ),
            },
        ),
        (
            "DESEMPENHO",
            {
                "fields": (
                    "avaliacao_desempenho",
                ),
            },
        ),
    )

    # def time_nome(self, obj):
    #     if obj in Time.objects.filter(goleiros=obj):
    #         return obj.time.nome
    #     elif obj in Time.objects.filter(defensores=obj):
    #         return obj.time.nome
    #     elif obj in Time.objects.filter(meio_campistas=obj):
    #         return obj.time.nome
    #     elif obj in Time.objects.filter(atacantes=obj):
    #         return obj.time.nome
    #     return ''
    #
    # time_nome.short_description = 'Nome do Time'


class JogoAdmin(admin.ModelAdmin):
    model = Jogo
    search_fields = ('local', 'equipe_casa__nome')
    list_display = ('equipe_casa_nome', 'equipe_visitante_nome', 'local', 'data_partida')
    inlines = [
        EstatisticasJogoAdmin,
    ]

    fieldsets = (
        (
            "PROGRAMAÇÃO DO JOGO",
            {
                "fields": (
                    (
                        "data_partida",
                    ),
                    (
                        "equipe_casa",
                        "placar_casa",
                    ),
                    (
                        "equipe_visitante",
                        "placar_visitante",
                    ),
                    (
                        "local",
                    ),
                ),
            },
        ),
        (
            "DADOS DO JOGO",
            {
                "fields": (
                    (
                        "arbitro",
                        "tempo_jogo",
                    ),
                ),
            },
        ),
    )

    def equipe_casa_nome(self, obj):
        return obj.equipe_casa.nome if obj.equipe_casa else ''

    equipe_casa_nome.short_description = 'Nome da Equipe da Casa'

    def equipe_visitante_nome(self, obj):
        return obj.equipe_visitante.nome if obj.equipe_visitante else ''

    equipe_visitante_nome.short_description = 'Nome da Equipe Visitante'


class TimeAdmin(admin.ModelAdmin):
    model = Time
    search_fields = ('nome', 'sigla', 'estadio', 'cidade')
    list_display = ('nome', 'sigla', 'cidade', 'pontos')

    fieldsets = (
        (
            "DADOS DA EQUIPE",
            {
                "fields": (
                    (
                        "nome",
                        "sigla",
                        "cidade",
                    ),
                    (
                        "fundacao",
                        "estadio",
                    ),
                ),
            },
        ),
        (
            "ESCUDO",
            {
                "fields": (
                    (
                        "escudo_url",
                        "escudo",
                    ),
                    (
                        "cores",
                        "anexado_em"
                    ),
                ),
            },
        ),
        (
            "CLASSIFICAÇÃO",
            {
                "fields": (
                    (
                        "classificacao",
                        "pontos"
                    ),
                ),
            },
        ),
    )
    filter_horizontal = ('jogadores',)


admin.site.register(Jogador, JogadorAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Jogo, JogoAdmin)
