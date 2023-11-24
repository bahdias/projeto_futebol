from django.contrib import admin
from django.urls import path

from . import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index'),

    path('players/', core_views.ListarJogadores.as_view(), name='listar-jogadores',),
    path('players/<str:id>/', core_views.ListarJogadorId.as_view(), name='listar-jogador-id',),

    path('teams/', core_views.ListarTimes.as_view(), name='listar-times',),
    path('teams/<str:id>/', core_views.ListarTimeId.as_view(), name='listar-time-id',),

    path('games/', core_views.ListarJogos.as_view(), name='listar-jogos',),
    path('games/<str:id>/', core_views.ListarJogosId.as_view(), name='listar-jogos-id',),

    path('tournaments/', core_views.ListarTorneios.as_view(), name='listar-torneios',),
    path('tournaments/<str:id>/', core_views.ListarTorneiosId.as_view(), name='listar-torneios-id',),

    path('rankings/<int:tournament_id>/<str:category>/<int:limit>', core_views.Ranking.as_view(), name='ranking-jogadores'),
    path('statistics/<int:tournament_id>/<int:id>', core_views.Estatisticas.as_view(), name='estatisticas-jogadores'),

]
