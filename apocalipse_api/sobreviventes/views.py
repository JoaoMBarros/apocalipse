from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sobrevivente, Inventario
from rest_framework import status, serializers
import random
import uuid

from .serializers import (
    SobreviventeSerializer, InventarioSerializer, 
    SobreviventeLocalizacaoSerializer, TrocaSerializer,
    InfectadoSerializer
    )

class NovaAcao(APIView):
    '''Randomiza ações'''

    def randomiza_acoes(self, sobreviventes):
        acoes = ['fugiu', 'visto_infectado', 'troca']
        for sobrevivente in sobreviventes:
            acao = random.choice(acoes)
            if acao == 'fugiu':
                # Retorna json com o sobrevivente que fugiu e a nova localização
                evento = {
                    'fugiu': {
                        'sobrevivente': {
                            'sobrevivente': sobrevivente.id,
                            'nome': sobrevivente.nome,
                        },
                        'latitude': random.uniform(-15, 15),
                        'longitude': random.uniform(-15, 15)
                    }
                }
                return evento
            
            elif acao == 'visto_infectado':
                outro_sobrevivente = random.choice(sobrevivente)
                while outro_sobrevivente.id == sobrevivente.id:
                    outro_sobrevivente = random.choice(sobrevivente)

                # Retorna json com o sobrevivente que foi visto infectado
                evento = {
                    'visto_infectado': {
                        'sobrevivente': {
                            'sobrevivente': sobrevivente.id,
                            'nome': sobrevivente.nome,
                        },
                        'outro_sobrevivente': {
                            'sobrevivente': outro_sobrevivente.id,
                            'nome': outro_sobrevivente.nome,
                        }
                    }
                }
                return evento

            elif acao == 'troca':
                outro_sobrevivente = random.choice(sobrevivente)
                while outro_sobrevivente.id == sobrevivente.id:
                    outro_sobrevivente = random.choice(sobrevivente)

                # Retorna json com os sobreviventes que querem trocar itens
                evento = {
                    'troca':{
                        'sobrevivente': {
                            'sobrevivente': sobrevivente.id,
                            'nome': sobrevivente.nome,
                        },
                        'outro_sobrevivente': {
                            'sobrevivente': outro_sobrevivente.id,
                            'nome': outro_sobrevivente.nome,
                        },
                    }
                }

                return evento
            
    def get(self, request, id_jogo):
        sobreviventes = Sobrevivente.objects.filter(jogo_id=id_jogo)
        if sobreviventes:
            return Response(self.randomiza_acoes(sobreviventes), status=status.HTTP_200_OK)
        else:
            return Response('Nenhum sobrevivente', status=status.HTTP_404_NOT_FOUND)

class CriaIdJogoView(APIView):
    '''Cria um novo id de jogo'''
    def get(self, request):
        id_jogo = str(uuid.uuid4())
        return Response(id_jogo, status=status.HTTP_200_OK)

class TodosSobreviventesView(APIView):
    '''Busca e cria no banco de dados as informações de todos os sobreviventes'''

    def get(self, request):
        sobreviventes = Sobrevivente.objects.all()
        serializer = SobreviventeSerializer(sobreviventes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SobreviventeSerializer(data=request.data['sobrevivente'])

        if serializer.is_valid():
            sobrevivente = serializer.save()
            sobrevivente_id = sobrevivente.id

            inventario_data = request.data.get('inventario')
            inventario_data['sobrevivente'] = sobrevivente_id
            inventario_serializer = InventarioSerializer(data=inventario_data)

            if inventario_serializer.is_valid():
                inventario_serializer.save(sobrevivente=sobrevivente)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                sobrevivente.delete()
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SobreviventeIdJogoView(APIView):
    '''Busca no banco de dados as informações de todos os sobreviventes de um jogo'''
    def get(self, request, id_jogo):
        sobreviventes = Sobrevivente.objects.filter(jogo_id=id_jogo)
        serializer = SobreviventeSerializer(sobreviventes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SobreviventeView(APIView):
    '''Busca e atualiza no banco de dados as informações de um sobrevivente'''

    def get(self, request, id_sobrevivente):
        try:
            sobrevivente = Sobrevivente.objects.get(id=id_sobrevivente)
            serializer = SobreviventeSerializer(sobrevivente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id_sobrevivente):
        sobrevivente = Sobrevivente.objects.get(id=id_sobrevivente)
        serializer = SobreviventeSerializer(sobrevivente, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SobreviventeLocalizacao(APIView):
    '''Busca e atualiza no banco de dados as informações de localização de um sobrevivente'''
        
    def patch(self, request):
        try:
            id_sobrevivente = request.data['sobrevivente']
            sobrevivente = Sobrevivente.objects.get(id=id_sobrevivente)
            serializer = SobreviventeLocalizacaoSerializer(sobrevivente, data=request.data, partial=True)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SobreviventeInfectado(APIView):
    '''Busca e atualiza no banco de dados as informações de quantas vezes um sobrevivente foi avistado infectado'''

    def patch(self, request):
        infectado_serializer = InfectadoSerializer(data=request.data)

        if infectado_serializer.is_valid():
            try:
                sobrevivente = Sobrevivente.objects.get(id=infectado_serializer.data['sobrevivente'])
                sobrevivente.avistado_infectado += 1

                if sobrevivente.avistado_infectado >= 3:
                    inventario = Inventario.objects.get(sobrevivente_id=infectado_serializer.data['sobrevivente'])
                    inventario.inventario_disponivel = False
                    sobrevivente.infectado = True
            
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
            sobrevivente.save()
            return Response(status=status.HTTP_200_OK)

class SobreviventeInventario(APIView):
    '''Busca e cria no banco de dados as informações de inventário de um sobrevivente'''

    def get(self, request, id_sobrevivente):
        try:
            inventario = Inventario.objects.get(sobrevivente=id_sobrevivente)
            serializer = InventarioSerializer(inventario)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
class TrocaItens(APIView):
    '''Troca itens entre sobreviventes'''

    itens_comerciais_pontos = {
        'agua': 4,
        'comida': 3,
        'medicamento': 2,
        'municao': 1
    }

    def valida_troca(self, serializer_data):
        '''Valida se a troca é possível'''

        # Verifica se o sobrevivente quer fazer uma troca com ele mesmo
        if serializer_data[0]['sobrevivente'] == serializer_data[1]['sobrevivente']:
            raise serializers.ValidationError("Sobrevivente não pode fazer troca com ele mesmo!")
        
        itens_sobrevivente_1 = serializer_data[0]['itens']
        itens_sobrevivente_2 = serializer_data[1]['itens']

        try:
            inventario_1 = Inventario.objects.get(sobrevivente_id=serializer_data[0]['sobrevivente'])
            inventario_2 = Inventario.objects.get(sobrevivente_id=serializer_data[1]['sobrevivente'])
        except:
            raise serializers.ValidationError("Sobrevivente não encontrado!")
        
        # Verificar se algum sobrevivente está infectado
        sobrevivente_infectado = None
        if inventario_1.sobrevivente.infectado:
            sobrevivente_infectado = inventario_1.sobrevivente.nome
        elif inventario_2.sobrevivente.infectado:
            sobrevivente_infectado = inventario_2.sobrevivente.nome
        
        if sobrevivente_infectado:
            raise serializers.ValidationError(f"Sobrevivente {sobrevivente_infectado} está infectado(a) e não pode realizar trocas. Fuja!")
        

        # Verificar se os sobreviventes têm itens suficientes para a troca
        for item, quantidade in itens_sobrevivente_1.items():
            if getattr(inventario_1, item) < quantidade:
                raise serializers.ValidationError(f"Sobrevivente {inventario_1.sobrevivente.nome} não possui quantidade suficiente de {item}!")

        for item, quantidade in itens_sobrevivente_2.items():
            if getattr(inventario_2, item) < quantidade:
                raise serializers.ValidationError(f"Sobrevivente {inventario_2.sobrevivente.nome} não possui quantidade suficiente de {item}!")


        # Verificar se a pontuação dos inventários é igual
        pontos_sobrevivente_1 = 0
        pontos_sobrevivente_2 = 0

        for item in self.itens_comerciais_pontos:
            if itens_sobrevivente_1[item]:
                pontos_sobrevivente_1 += self.itens_comerciais_pontos[item] * itens_sobrevivente_1[item]

            if itens_sobrevivente_2[item]:
                pontos_sobrevivente_2 += self.itens_comerciais_pontos[item] * itens_sobrevivente_2[item]

        if pontos_sobrevivente_1 != pontos_sobrevivente_2:
            if pontos_sobrevivente_2 > pontos_sobrevivente_1:
                sobrevivente_pontuacao_itens_inferior = inventario_1.sobrevivente.nome
            else:
                sobrevivente_pontuacao_itens_inferior = inventario_2.sobrevivente.nome
            
            raise serializers.ValidationError(f"A pontuação de troca de {sobrevivente_pontuacao_itens_inferior} é inferior!")
            
        return inventario_1, inventario_2
        

    def post(self, request):
        '''Realiza a troca de itens entre sobreviventes'''
        serializer = TrocaSerializer(data=request.data['troca'], many=True)
        
        if (serializer.is_valid()):
            inventario_1, inventario_2 = self.valida_troca(serializer.data)

            if inventario_1:
                itens_sobrevivente_1 = serializer.data[0]['itens']
                itens_sobrevivente_2 = serializer.data[1]['itens']

                for item in self.itens_comerciais_pontos:
                    if itens_sobrevivente_1[item]:
                        setattr(inventario_1, item, getattr(inventario_1, item) - itens_sobrevivente_1[item])
                        setattr(inventario_2, item, getattr(inventario_2, item) + itens_sobrevivente_1[item])

                    if itens_sobrevivente_2[item]:
                        setattr(inventario_2, item, getattr(inventario_2, item) - itens_sobrevivente_2[item])
                        setattr(inventario_1, item, getattr(inventario_1, item) + itens_sobrevivente_2[item])
                
                inventario_1.save()
                inventario_2.save()

                return Response("Troca realizada com sucesso", status=status.HTTP_200_OK)


        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)