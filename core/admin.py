from django.contrib import admin
from .models.cartao import Cartao
from .models.competido_por import CompetidoPor
from .models.gol_jogador import GolJogador
from .models.gol_time import GolTime
from .models.jogador import Jogador
from .models.jogo import Jogo
from .models.time import Time
from .models.torneio import Torneio


class JogadorAdmin(admin.ModelAdmin):
    model = Jogador
    search_fields = ('nome', 'posicao', 'idade',)
    list_display = ('nome', 'nacionalidade', 'posicao')

    fieldsets = (
        (
            "PERFIL",
            {
                "fields": (
                    (
                        "nome",
                        "nacionalidade",
                    ),
                    (
                        "idade",
                        "dt_nascimento"
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
            "INFORMAÇÕES DO TIME",
            {
                "fields": (
                    "time",
                    "numero_camisa",
                ),
            },
        ),
    )


class JogoAdmin(admin.ModelAdmin):
    model = Jogo
    search_fields = ('local', 'time_casa__nome')
    list_display = ('time_casa_nome', 'time_visitante_nome', 'data_partida')

    fieldsets = (
        (
            "PROGRAMAÇÃO DO JOGO",
            {
                "fields": (
                    (
                        "data_partida",
                    ),
                    (
                        "torneio",
                        "estadio",
                    ),
                    (
                        "time_casa",
                        "time_visitante",
                    ),
                ),
            },
        ),
    )

    def time_casa_nome(self, obj):
        return obj.time_casa.nome if obj.time_casa else ''

    time_casa_nome.short_description = 'Nome da Equipe da Casa'

    def time_visitante_nome(self, obj):
        return obj.time_visitante.nome if obj.time_visitante else ''

    time_visitante_nome.short_description = 'Nome da Equipe Visitante'


class TimeAdmin(admin.ModelAdmin):
    model = Time
    search_fields = ('nome', 'abreviacao', 'cidade')
    list_display = ('nome', 'abreviacao', 'cidade')

    fieldsets = (
        (
            "DADOS DA EQUIPE",
            {
                "fields": (
                    (
                        "nome",
                        "abreviacao",
                    ),
                    (
                        "cidade",
                        "fundacao",
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
                        "anexado_em"
                    ),
                    (
                        "primeira_cor",
                        "segunda_cor"
                    ),
                ),
            },
        ),
        (
            "TÉCNICO",
            {
                "fields": (
                    (
                        "tecnico",
                    ),
                ),
            },
        ),
    )


class TorneioAdmin(admin.ModelAdmin):
    model = Torneio
    search_fields = ('nome', 'ano')
    list_display = ('nome', 'ano')

    fieldsets = (
        (
            "DADOS DO TORNEIO",
            {
                "fields": (
                    (
                        "nome",
                        "ano",
                    ),
                ),
            },
        ),
    )


class GolTimeAdmin(admin.ModelAdmin):
    model = GolTime
    search_fields = ('time', 'tempo')
    list_display = ('time', 'tempo', 'contra', 'marcado', 'sofrido')

    fieldsets = (
        (
            "DADOS DO GOL",
            {
                "fields": (
                    (
                        "time",
                        "tempo",
                    ),
                ),
            },
        ),
        (
            "INFORMAÇÕES",
            {
                "fields": (
                    (
                        "contra",
                        "marcado",
                        "sofrido",
                    ),
                ),
            },
        ),
    )


class GolJogadorAdmin(admin.ModelAdmin):
    model = GolJogador
    search_fields = ('jogador', 'tempo')
    list_display = ('jogador', 'tempo', 'contra', 'marcado', 'assistido')

    fieldsets = (
        (
            "DADOS DO GOL",
            {
                "fields": (
                    (
                        "jogador",
                        "tempo",
                    ),
                ),
            },
        ),
        (
            "INFORMAÇÕES",
            {
                "fields": (
                    (
                        "contra",
                        "marcado",
                        "assistido",
                    ),
                ),
            },
        ),
    )


class CompetidoPorAdmin(admin.ModelAdmin):
    model = CompetidoPor
    search_fields = ('time', 'torneio')
    list_display = ('time', 'torneio', 'vitorias', 'derrotas', 'empates', 'pontuacao')

    fieldsets = (
        (
            "DADOS DO TORNEIO",
            {
                "fields": (
                    (
                        "time",
                        "torneio",
                    ),
                    (
                        "vitorias",
                        "derrotas",
                        "empates",
                    ),
                    (
                        "gols_marcados",
                        "gols_sofridos",
                        "saldo_gols",
                    ),
                    (
                        "cartao",
                        "pontuacao",
                    ),
                ),
            },
        ),
    )


class CartaoAdmin(admin.ModelAdmin):
    model = Cartao
    search_fields = ('jogo',)
    list_display = ('jogo', 'tempo', 'tipo')

    fieldsets = (
        (
            "DADOS DO CARTÃO",
            {
                "fields": (
                    (
                        "jogo",
                    ),
                    (
                        "tempo",
                        "tipo",
                    ),
                    (
                        "time",
                        "jogador",
                    ),
                ),
            },
        ),
    )


admin.site.register(Jogador, JogadorAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Jogo, JogoAdmin)
admin.site.register(GolTime, GolTimeAdmin)
admin.site.register(GolJogador, GolJogadorAdmin)
admin.site.register(Cartao, CartaoAdmin)
# admin.site.register(CartaoJogador, CartaoJogadorAdmin)
admin.site.register(CompetidoPor, CompetidoPorAdmin)
admin.site.register(Torneio, TorneioAdmin)
