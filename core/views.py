from django.db.models import Q, Sum, Count
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from .constants import EnumCartao
from .models.cartao import Cartao
from .models.competido_por import CompetidoPor
from .models.gol import Gol
from .models.jogador import Jogador
from .models.jogo import Jogo
from .models.time import Time
from .models.torneio import Torneio
from .serializer import ListarJogadoresSerializer, ListarTimesSerializer, ListarTimesTorneiosSerializer, \
    ListarJogosSerializer, ListarTorneiosSerializer, ListarEstatisticaSerializer
from django.http import HttpResponseRedirect


def index(request):
    return HttpResponseRedirect('/admin')


"""APIs para os Jogadores"""


class ListarJogadores(ListAPIView):
    """
    API da listagem dos dados de todos os Jogadores
    """

    def get(self, request):
        # Verifica a origem do request
        try:
            jogadores = Jogador.objects.filter().all()
            serializer = ListarJogadoresSerializer(
                jogadores, many=True, context={'request': request}
            )
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception:
            return Response(
                {'Erro': 'Não foi possível listar todos os Jogadores.'},
                status=HTTP_400_BAD_REQUEST,
            )


class ListarJogadorId(ListAPIView):
    """
    API da listagem dos dados do Jogadores que corresponde ao id
    """

    def get(self, request, id):
        # Verifica a origem do request
        try:
            nome_like_prefix = "name_like="
            id_time_prefix = "teamId="
            if id.startswith(nome_like_prefix):
                nome = id[len(nome_like_prefix):].strip('"')
                jogador = Jogador.objects.filter(nome=nome).first()
            elif id.startswith(id_time_prefix):
                id_time = id[len(id_time_prefix):].strip('"')
                time = Time.objects.filter(pk=id_time).first()
                jogador = Jogador.objects.filter(time=time).first()
            else:
                jogador = get_object_or_404(Jogador, pk=id)
            serializer = ListarJogadoresSerializer(
                jogador, context={'request': request}
            )
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response(
                {'Erro': f'Não foi possível listar o jogador.'},
                status=HTTP_400_BAD_REQUEST,
            )


"""APIs para os Times"""


class ListarTimes(ListAPIView):
    """
    API da listagem dos dados de todos os Times
    """

    def get(self, request):
        # Verifica a origem do request
        try:
            times = Time.objects.filter().all()
            serializer = ListarTimesSerializer(
                times, many=True, context={'request': request}
            )
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception:
            return Response(
                {'Erro': 'Não foi possível listar todos os Times.'},
                status=HTTP_400_BAD_REQUEST,
            )


class ListarTimeId(ListAPIView):
    """
    API da listagem dos dados do Times que corresponde ao id
    """

    def get(self, request, id):
        # Verifica a origem do request
        try:
            nome_like_prefix = "name_like="
            id_torneio_prefix = "tournamentId="
            if id.startswith(nome_like_prefix):
                nome = id[len(nome_like_prefix):].strip('"')
                time = Time.objects.filter(nome=nome).first()
                serializer = ListarTimesSerializer(
                    time, context={'request': request}
                )
            elif id.startswith(id_torneio_prefix):
                id_torneio = id[len(id_torneio_prefix):].strip('"')
                torneio = Torneio.objects.filter(pk=id_torneio).first()
                times_ids = CompetidoPor.objects.filter(torneio=torneio).values_list('time_id', flat=True)
                times_objects = Time.objects.filter(pk__in=times_ids)
                serializer = ListarTimesSerializer(
                    times_objects, many=True, context={'request': request}
                )
            else:
                time = get_object_or_404(Time, pk=id)
                serializer = ListarTimesSerializer(
                    time, context={'request': request}
                )
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            return Response(
                {'Erro': f'Não foi possível listar o time com o id {id}.'},
                status=HTTP_400_BAD_REQUEST,
            )


"""APIs para os Jogos"""


class ListarJogos(ListAPIView):
    """
    API da listagem dos dados de todos os Jogos
    """

    def get(self, request):
        # Verifica a origem do request
        try:
            jogos = Jogo.objects.filter().all()
            serializer = ListarJogosSerializer(
                jogos, many=True, context={'request': request}
            )
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception:
            return Response(
                {'Erro': 'Não foi possível listar todos os Jogos.'},
                status=HTTP_400_BAD_REQUEST,
            )


class ListarJogosId(ListAPIView):
    """
    API da listagem dos dados do Jogos que corresponde ao id
    """

    def get(self, request, id):
        # Verifica a origem do request
        try:
            tournamentId_prefix = "tournamentId="
            teamId_prefix = "teamId="
            if id.startswith(tournamentId_prefix):
                torneio_id = id[len(tournamentId_prefix):].strip('"')
                torneio = Torneio.objects.filter(pk=torneio_id).first()
                jogos_objects = Jogo.objects.filter(torneio=torneio)
                serializer = ListarJogosSerializer(
                    jogos_objects, many=True, context={'request': request}
                )
            elif id.startswith(teamId_prefix):
                time_id = id[len(teamId_prefix):].strip('"')
                time = Time.objects.filter(pk=time_id).first()
                jogos_objects = Jogo.objects.filter(Q(time_casa=time) | Q(time_visitante=time))
                serializer = ListarJogosSerializer(
                    jogos_objects, many=True, context={'request': request}
                )
            else:
                jogo = get_object_or_404(Jogo, pk=id)
                serializer = ListarJogosSerializer(
                    jogo, context={'request': request}
                )
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception:
            return Response(
                {'Erro': f'Não foi possível listar o jogo com o id {id}.'},
                status=HTTP_400_BAD_REQUEST,
            )


"""APIs para os Torneios"""


class ListarTorneios(ListAPIView):
    """
    API da listagem dos dados de todos os Torneios
    """

    def get(self, request):
        # Verifica a origem do request
        try:
            torneios = Torneio.objects.filter().all()
            serializer = ListarTorneiosSerializer(
                torneios, many=True, context={'request': request}
            )
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception:
            return Response(
                {'Erro': 'Não foi possível listar todos os Torneios.'},
                status=HTTP_400_BAD_REQUEST,
            )


class ListarTorneiosId(ListAPIView):
    """
    API da listagem dos dados do Torneios que corresponde ao id
    """

    def get(self, request, id):
        # Verifica a origem do request
        try:
            teamId_prefix = "teamId="
            if id.startswith(teamId_prefix):
                time_id = id[len(teamId_prefix):].strip('"')
                time = Time.objects.filter(pk=time_id).first()
                torneios_ids = CompetidoPor.objects.filter(time=time).values_list('torneio_id', flat=True)
                torneios_objects = Torneio.objects.filter(pk__in=torneios_ids)
                serializer = ListarTorneiosSerializer(
                    torneios_objects, many=True, context={'request': request}
                )
            else:
                torneio = get_object_or_404(Torneio, pk=id)
                serializer = ListarTorneiosSerializer(
                    torneio, context={'request': request}
                )
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception:
            return Response(
                {'Erro': f'Não foi possível listar o torneio com o id {id}.'},
                status=HTTP_400_BAD_REQUEST,
            )


class ListarTimesTorneiosId(ListAPIView):
    """
    API da listagem dos dados do Time que corresponde ao nome e ao id do torneio
    """

    def get(self, request, id):
        # Verifica a origem do request
        try:
            time = Time.objects.filter(pk=id).first()
            jogo = Jogo.objects.filter(Q(time_casa=time) | Q(time_visitante=time))
            serializer = ListarTimesTorneiosSerializer(
                jogo, context={'request': request}
            )
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(
                {'Erro': f'Não foi possível listar os jogos do time {nome}.'},
                status=HTTP_400_BAD_REQUEST,
            )

class Ranking(ListAPIView):
    """
    API de ranking de jogadores
    """

    def get(self, request, tournament_id, category, limit):
        try:
            torneio = get_object_or_404(Torneio, pk=tournament_id)
            jogos = Jogo.objects.filter(torneio=torneio)

            if category == 'goals':
                gols = Gol.objects.filter(jogo__in=jogos)
                jogadores = {}
                for gol in gols:
                    jogador = gol.jogador
                    if jogador in jogadores:
                        jogadores[jogador]['quantidade'] += 1
                    else:
                        jogadores[jogador] = {'jogador': jogador, 'quantidade': 1}

                ranking = sorted(jogadores.values(), key=lambda x: x['quantidade'], reverse=True)[:limit]
                serializer_data = [
                    {'nome': jogador['jogador'].nome, 'apelido': jogador['jogador'].apelido, 'quantidade_gols': jogador['quantidade']}
                    for jogador in ranking
                ]

                return Response(serializer_data, status=HTTP_200_OK)
            if category == 'cards':
                gols = Cartao.objects.filter(jogo__in=jogos)
                jogadores = {}
                for gol in gols:
                    jogador = gol.jogador
                    if jogador in jogadores:
                        jogadores[jogador]['quantidade'] += 1
                    else:
                        jogadores[jogador] = {'jogador': jogador, 'quantidade': 1}

                ranking = sorted(jogadores.values(), key=lambda x: x['quantidade'], reverse=True)[:limit]
                serializer_data = [
                    {'nome': jogador['jogador'].nome, 'apelido': jogador['jogador'].apelido, 'quantidade_cartao': jogador['quantidade']}
                    for jogador in ranking
                ]

                return Response(serializer_data, status=HTTP_200_OK)
            else:
                return Response(
                    {'Erro': 'A categoria deve ser "goals".'},
                    status=HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {'Erro': f'Não foi possível obter o ranking: {str(e)}'},
                status=HTTP_400_BAD_REQUEST,
            )

class Estatisticas(ListAPIView):
    """
    API de estatisticas do jogadores
    """

    def get(self, request, tournament_id, id):
        try:
            torneio = get_object_or_404(Torneio, pk=tournament_id)
            jogador = get_object_or_404(Jogador, pk=id)
            jogos = Jogo.objects.filter(torneio=torneio)

            gols = Gol.objects.filter(jogo__in=jogos, jogador=jogador).count()
            assistencia = Gol.objects.filter(jogo__in=jogos, assistido=jogador).count()
            cartao_amarelo = Cartao.objects.filter(jogo__in=jogos, jogador=jogador, tipo=EnumCartao.AMARELO.value).count()
            cartao_vermelho = Cartao.objects.filter(jogo__in=jogos, jogador=jogador, tipo=EnumCartao.VERMELHO.value).count()

            serializer_data = [
                {
                    'nome': jogador.nome, 'gols': gols, 'assistencia': assistencia,
                    'cartao_amarelo': cartao_amarelo, 'cartao_vermelho': cartao_vermelho
                }
            ]
            return Response(serializer_data, status=HTTP_200_OK)
        except Exception as e:
            return Response(
                {'Erro': f'Não foi possível obter a estatistica: {str(e)}'},
                status=HTTP_400_BAD_REQUEST,
            )
