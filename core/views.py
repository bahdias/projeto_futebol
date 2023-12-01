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
            time_id_prefix = "teamId="
            if id.startswith(nome_like_prefix):
                nome = id[len(nome_like_prefix):].strip('"')
                jogador = Jogador.objects.filter(nome=nome).first()
            elif id.startswith(time_id_prefix):
                time_id = id[len(time_id_prefix):].strip('"')
                time = Time.objects.filter(pk=time_id).first()
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
            torneio_id_prefix = "tournamentId="
            if torneio_id_prefix in id and nome_like_prefix in id:
                start_nome = id.find(nome_like_prefix)
                end_nome = id.find("&", start_nome)
                nome = id[start_nome + len(nome_like_prefix):end_nome].strip('"')
                partes = id.split("=")
                torneio_id = partes[2].strip('"')
                torneio = Torneio.objects.filter(pk=torneio_id).first()
                time = Time.objects.filter(nome=nome)
                times_ids = CompetidoPor.objects.filter(torneio=torneio).values_list('time_id', flat=True)
                times_objects = Time.objects.filter(pk__in=times_ids)
                times_torneio_serializer = ListarTimesSerializer(
                    times_objects, many=True, context={'request': request}
                )
                time_id_serializer = ListarTimesSerializer(
                    time, many=True, context={'request': request}
                )
                serializer = []
                serializer.extend(times_torneio_serializer.data)
                serializer.extend(time_id_serializer.data)
                return Response(serializer, status=HTTP_200_OK)
            elif id.startswith(nome_like_prefix):
                nome = id[len(nome_like_prefix):].strip('"')
                time = Time.objects.filter(nome=nome).first()
                serializer = ListarTimesSerializer(
                    time, context={'request': request}
                )
            elif id.startswith(torneio_id_prefix):
                torneio_id = id[len(torneio_id_prefix):].strip('"')
                torneio = Torneio.objects.filter(pk=torneio_id).first()
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
            tournament_id_prefix = "tournamentId="
            team_id_prefix = "teamId="
            if tournament_id_prefix in id and team_id_prefix in id:
                start_id = id.find(tournament_id_prefix)
                end_nome = id.find("&", start_id)
                torneio_id = id[start_id + len(tournament_id_prefix):end_nome].strip('"')
                partes = id.split("=")
                time_id = partes[2].strip('"')
                time = Time.objects.filter(pk=time_id).first()
                jogos_objects_time = Jogo.objects.filter(Q(time_casa=time) | Q(time_visitante=time))
                torneio = Torneio.objects.filter(pk=torneio_id).first()
                jogos_objects_torneio = Jogo.objects.filter(torneio=torneio)
                jogos_torneio_serializer = ListarJogosSerializer(
                    jogos_objects_torneio, many=True, context={'request': request}
                )
                jogos_time_serializer = ListarJogosSerializer(
                    jogos_objects_time, many=True, context={'request': request}
                )
                serializer = []
                serializer.extend(jogos_torneio_serializer.data)
                serializer.extend(jogos_time_serializer.data)
                return Response(serializer, status=HTTP_200_OK)
            elif id.startswith(tournament_id_prefix):
                torneio_id = id[len(tournament_id_prefix):].strip('"')
                torneio = Torneio.objects.filter(pk=torneio_id).first()
                jogos_objects = Jogo.objects.filter(torneio=torneio)
                serializer = ListarJogosSerializer(
                    jogos_objects, many=True, context={'request': request}
                )
            elif id.startswith(team_id_prefix):
                time_id = id[len(team_id_prefix):].strip('"')
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
            team_id_prefix = "teamId="
            if id.startswith(team_id_prefix):
                time_id = id[len(team_id_prefix):].strip('"')
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
                {'Erro': f'Não foi possível listar os jogos do time {id}.'},
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

                serializer_data = []
                for jogador_info in jogadores.values():
                    jogador = jogador_info['jogador']
                    jogador_serializer = ListarJogadoresSerializer(jogador, context={'request': request})
                    jogador_data = jogador_serializer.data
                    quantidade_gols = jogador_info['quantidade']

                    serializer_data.append({
                        'gols': quantidade_gols,
                        'jogador': jogador_data
                    })

                serializer_data = sorted(serializer_data, key=lambda x: x['quantidade_gols'], reverse=True)[:limit]

                return Response(serializer_data, status=HTTP_200_OK)
            if category == 'cards':
                cartoes = Cartao.objects.filter(jogo__in=jogos)
                jogadores = {}
                for cartao in cartoes:
                    jogador = cartao.jogador
                    if jogador in jogadores:
                        jogadores[jogador]['quantidade'] += 1
                    else:
                        jogadores[jogador] = {'jogador': jogador, 'quantidade': 1}

                serializer_data = []
                for jogador_info in jogadores.values():
                    jogador = jogador_info['jogador']
                    jogador_serializer = ListarJogadoresSerializer(jogador, context={'request': request})
                    jogador_data = jogador_serializer.data
                    quantidade_cartao = jogador_info['quantidade']

                    serializer_data.append({
                        'quantidade_cartao': quantidade_cartao,
                        'jogador': jogador_data,
                    })

                serializer_data = sorted(serializer_data, key=lambda x: x['quantidade_cartao'], reverse=True)[:limit]

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
            cartao_amarelo = Cartao.objects.filter(jogo__in=jogos, jogador=jogador,
                                                   tipo=EnumCartao.AMARELO.value).count()
            cartao_vermelho = Cartao.objects.filter(jogo__in=jogos, jogador=jogador,
                                                    tipo=EnumCartao.VERMELHO.value).count()

            # Obter dados do jogador usando o serializer
            jogador_data = ListarJogadoresSerializer(jogador, context={'request': request}).data

            # Adicionar dados do jogador ao dicionário serializer_data
            serializer_data = [
                {
                    'gols': gols,
                    'cartao_amarelo': cartao_amarelo,
                    'cartao_vermelho': cartao_vermelho,
                    'assistencia': assistencia,
                    'jogador': jogador_data
                }
            ]
            serializer_data.extend(jogador_data.data)
            return Response(serializer_data, status=HTTP_200_OK)
        except Exception as e:
            return Response(
                {'Erro': f'Não foi possível obter a estatistica: {str(e)}'},
                status=HTTP_400_BAD_REQUEST,
            )
