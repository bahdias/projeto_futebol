from django.contrib import admin
from .models.cartao import Cartao
from .models.competido_por import CompetidoPor
from .models.gol import Gol
from .models.jogador import Jogador
from .models.jogo import Jogo
from .models.time import Time
from .models.torneio import Torneio
from import_export.admin import ImportExportModelAdmin


class JogadorAdmin(ImportExportModelAdmin):
    model = Jogador
    search_fields = ('nome', 'posicao', 'idade',)
    list_display = ('nome', 'pais', 'posicao', 'time_nome')
    readonly_fields = (
        'idade',
    )

    fieldsets = (
        (
            "PERFIL",
            {
                "fields": (
                    (
                        "nome",
                        "pais",
                    ),
                    (
                        "dt_nascimento",
                        "idade",
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

    def time_nome(self, obj):
        return obj.time.nome if obj.time else ''

    time_nome.short_description = 'Nome do Time'


class CartaoInline(admin.TabularInline):
    model = Cartao
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if self.model:
            jogo_id = request.resolver_match.kwargs.get('object_id')

            # Verificar se o jogo_id existe
            if jogo_id is not None:
                try:
                    jogo = Jogo.objects.get(pk=jogo_id)
                except Jogo.DoesNotExist:
                    jogo = None

                if jogo:
                    if db_field.name == "jogador":
                        kwargs["queryset"] = jogo.time_casa.time_jogador.all() | jogo.time_visitante.time_jogador.all()
                    elif db_field.name == "time":
                        kwargs["queryset"] = Time.objects.filter(pk__in=[jogo.time_casa.id, jogo.time_visitante.id])

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class GolInline(admin.TabularInline):
    model = Gol
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if self.model:
            jogo_id = request.resolver_match.kwargs.get('object_id')

            # Verificar se o jogo_id existe
            if jogo_id is not None:
                try:
                    jogo = Jogo.objects.get(pk=jogo_id)
                except Jogo.DoesNotExist:
                    jogo = None

                if jogo:
                    if db_field.name == "jogador":
                        kwargs["queryset"] = jogo.time_casa.time_jogador.all() | jogo.time_visitante.time_jogador.all()
                    elif db_field.name in ("time_marcou", "time_sofreu"):
                        if db_field.name == "time_marcou":
                            kwargs["queryset"] = Time.objects.filter(pk__in=[jogo.time_casa.id, jogo.time_visitante.id])
                        elif db_field.name == "time_sofreu":
                            kwargs["queryset"] = Time.objects.filter(pk__in=[jogo.time_casa.id, jogo.time_visitante.id])
                    elif db_field.name == "assistido":
                        kwargs["queryset"] = jogo.time_casa.time_jogador.all() | jogo.time_visitante.time_jogador.all()

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class JogoAdmin(ImportExportModelAdmin):
    model = Jogo
    search_fields = ('local', 'time_casa_nome')
    list_display = ('time_casa_nome', 'time_visitante_nome', 'data_hora_inicio')
    inlines = [
        GolInline,
        CartaoInline
    ]

    fieldsets = (
        (
            "PROGRAMAÇÃO DO JOGO",
            {
                "fields": (
                    (
                        "data_hora_inicio",
                    ),
                    (
                        "torneio",
                        "estadio",
                    ),
                    (
                        "time_casa",
                        "time_visitante",
                    ),
                    (
                        "acabou",
                    ),
                ),
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj and obj.acabou:
            return (
                'data_inicio',
                'torneio',
                'estadio',
                'time_casa',
                'time_visitante',
                'acabou'
            )
        return readonly_fields

    def time_casa_nome(self, obj):
        return obj.time_casa.nome if obj.time_casa else ''

    time_casa_nome.short_description = 'Nome da Equipe da Casa'

    def time_visitante_nome(self, obj):
        return obj.time_visitante.nome if obj.time_visitante else ''

    time_visitante_nome.short_description = 'Nome da Equipe Visitante'


class TimeAdmin(ImportExportModelAdmin):
    model = Time
    search_fields = ('nome', 'abreviacao', 'pais')
    list_display = ('nome', 'abreviacao', 'pais',)

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
                        "pais",
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
                    ),
                    (
                        "cor_primaria",
                        "cor_secundaria"
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


class TorneioAdmin(ImportExportModelAdmin):
    model = Torneio
    search_fields = ('nome', 'data')
    list_display = ('nome', 'data')

    fieldsets = (
        (
            "DADOS DO TORNEIO",
            {
                "fields": (
                    (
                        "nome",
                        "data",
                    ),
                ),
            },
        ),
    )


class CompetidoPorAdmin(admin.ModelAdmin):
    model = CompetidoPor
    search_fields = ('time', 'torneio')
    list_display = ('time', 'torneio', 'vitorias', 'derrotas', 'empates', 'pontuacao')
    readonly_fields = (
        'saldo_gols',
        'time',
        'torneio',
        'vitorias',
        'derrotas',
        'empates',
        'gols_marcados',
        'gols_sofridos',
        'saldo_gols',
        'saldo_gols',
        'cartao_amarelo',
        'cartao_vermelho',
        'pontuacao',
    )

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
                        "cartao_amarelo",
                        "cartao_vermelho",
                        "pontuacao",
                    ),
                ),
            },
        ),
    )


admin.site.register(Jogador, JogadorAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Jogo, JogoAdmin)
admin.site.register(CompetidoPor, CompetidoPorAdmin)
admin.site.register(Torneio, TorneioAdmin)
