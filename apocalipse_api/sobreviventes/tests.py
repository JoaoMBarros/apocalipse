import uuid
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Sobrevivente, Inventario

class TestarListagemSobreviventes(APITestCase):
    def testar_listagem_sobreviventes(self):
        request = self.client.get('/sobreviventes/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

class TestarCriacaoIdJogo(APITestCase):
    def testar_criacao_id_jogo(self):
        request = self.client.get('/sobreviventes/novo_jogo/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

class TestarCriacaoSobreviventeInventario(APITestCase):
    def testar_criacao_sobrevivente_inventario(self):
        payload = {
            "sobrevivente": {
                "sobrevivente": 100,
                "nome": "Teste",
                "idade": 20,
                "sexo": "M",
                "jogo_id": 123
            },
            "inventario": {
                "agua": 10,
                "comida": 10,
                "medicamento": 10,
                "municao": 10,
            }
        }

        request = self.client.post('/sobreviventes/', payload, format="json")
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

class TestarCriacaoSobreviventeInvalido(APITestCase):
    def testar_criacao_sobrevivente_sem_nome(self):
        payload = {
            "sobrevivente": {
                "sobrevivente": 100,
                "idade": 20,
                "sexo": "M",
                "jogo_id": 123
            },
            "inventario": {
                "agua": 10,
                "comida": 10,
                "medicamento": 10,
                "municao": 10,
                "outros_itens": "Teste"
            }
        }
        request = self.client.post('/sobreviventes/', payload, format="json")
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
    
    def testar_criacao_sobrevivente_sem_idade(self):
        payload = {
            "sobrevivente": {
                "sobrevivente": 100,
                "nome": "Teste",
                "sexo": "M",
                "jogo_id": 123
            },
            "inventario": {
                "agua": 10,
                "comida": 10,
                "medicamento": 10,
                "municao": 10,
                "outros_itens": "Teste"
            }
        }
        request = self.client.post('/sobreviventes/', payload, format="json")
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

class TestarListagemSobreviventesIdJogo(APITestCase):
    def testar_listagem_sobreviventes_id_jogo(self):
        teste_uuid = uuid.uuid4()

        payload = {
            "sobrevivente": {
                "sobrevivente": 100,
                "nome": "Teste",
                "idade": 20,
                "sexo": "M",
                "jogo_id": teste_uuid
            },
            "inventario": {
                "agua": 10,
                "comida": 10,
                "medicamento": 10,
                "municao": 10,
                "outros_itens": "Teste"
            }
        }
        request = self.client.post('/sobreviventes/', payload, format="json")
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        payload = {
            "sobrevivente": {
                "sobrevivente": 100,
                "nome": "Teste",
                "idade": 20,
                "sexo": "M",
                "jogo_id": teste_uuid
            },
            "inventario": {
                "agua": 10,
                "comida": 10,
                "medicamento": 10,
                "municao": 10,
                "outros_itens": "Teste"
            }
        }
        request = self.client.post('/sobreviventes/', payload, format="json")
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        
        request = self.client.get(f'/sobreviventes/{teste_uuid}/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), 2)

class TestarListagemSobreviventesIdJogoInvalido(APITestCase):
    def testar_listagem_sobreviventes_id_jogo_invalido(self):
        teste_uuid = uuid.uuid4()

        request = self.client.get(f'/sobreviventes/{teste_uuid}/')
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

class TestarListagemSobreviventesIdSobrevivente(APITestCase):
    def testar_listagem_sobreviventes_id_sobrevivente(self):
        Sobrevivente.objects.create(
            id=100,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )
        request = self.client.get('/sobreviventes/100/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

class TestarListagemSobreviventesIdSobreviventeInvalido(APITestCase):
    def testar_listagem_sobreviventes_id_sobrevivente_invalido(self):
        request = self.client.get('/sobreviventes/100/')
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

class TestarListagemSobreviventesInventario(APITestCase):
    def testar_listagem_sobreviventes_inventario(self):
        Sobrevivente.objects.create(
            id=100,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )

        Inventario.objects.create(
            sobrevivente_id=100,
            agua=10,
            comida=10,
            medicamento=10,
            municao=10,
            outros_itens="Teste"
        )

        request = self.client.get('/sobreviventes/100/inventario/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

class TestarListagemSobreviventesInventarioInvalido(APITestCase):
    def testar_listagem_sobreviventes_inventario_invalido(self):
        request = self.client.get('/sobreviventes/100/inventario/')
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

class TestarAtualizacaoSobreviventeLocalizacao(APITestCase):
    def testar_atualizacao_sobrevivente_localizacao(self):
        Sobrevivente.objects.create(
            id=100,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )
        request = self.client.patch('/sobreviventes/localizacao/', {"sobrevivente": 100, "latitude": 10, "longitude": 10}, format="json")
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        sobrevivente = Sobrevivente.objects.get(id=100)
        self.assertEqual(sobrevivente.latitude, 10)
        self.assertEqual(sobrevivente.longitude, 10)

class TestarAtualizacaoSobreviventeInvalidoLocalizacao(APITestCase):
    def testar_atualizacao_sobrevivente_localizacao_invalido(self):
        request = self.client.patch('/sobreviventes/localizacao/', {"sobrevivente": 100, "latitude": 10, "longitude": 10}, format="json")
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

class TestarAtualizacaoSobreviventeLocalizacaoInvalida(APITestCase):
    def testar_atualizacao_sobrevivente_localizacao_invalida(self):
        Sobrevivente.objects.create(
            id=100,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )
        request = self.client.patch('/sobreviventes/localizacao/', {"sobrevivente": 100, "latitude": "Teste", "longitude": 10}, format="json")
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

class TestarSobreviventeVistoInfectado(APITestCase):
    def testar_sobrevivente_visto_infectado(self):
        Sobrevivente.objects.create(
            id=100,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )
        request = self.client.patch('/sobreviventes/infectado/', {"sobrevivente": 100}, format="json")
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        sobrevivente = Sobrevivente.objects.get(id=100)
        self.assertEqual(sobrevivente.avistado_infectado, 1)

class TestarSobreviventeInvalidoVistoInfectado(APITestCase):
    def testar_sobrevivente_visto_infectado_invalido(self):
        request = self.client.patch('/sobreviventes/infectado/', {"sobrevivente": 100}, format="json")
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

class TestarSobreviventeInfectado(APITestCase):
    def testar_sobrevivente_infectado(self):
        Sobrevivente.objects.create(
            id=100,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123,
            avistado_infectado=2
        )

        request = self.client.patch('/sobreviventes/infectado/', {"sobrevivente": 100}, format="json")
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        sobrevivente = Sobrevivente.objects.get(id=100)
        self.assertEqual(sobrevivente.infectado, True)

class TestarSobreviventeInfectadoInvalido(APITestCase):
    def testar_sobrevivente_visto_infectado_invalido(self):
        request = self.client.patch('/sobreviventes/infectado/', {"sobrevivente": 100}, format="json")
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

class TestarTrocaItens(APITestCase):
    def testar_troca_itens(self):
        Sobrevivente.objects.create(
            id=100,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )

        Sobrevivente.objects.create(
            id=101,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )

        Inventario.objects.create(
            sobrevivente_id=100,
            agua=10,
            comida=10,
            medicamento=10,
            municao=10,
            outros_itens="Teste"
        )

        Inventario.objects.create(
            sobrevivente_id=101,
            agua=10,
            comida=10,
            medicamento=10,
            municao=10,
            outros_itens="Teste"
        )

        payload = {
            "troca": [
                {
                    "sobrevivente": 100,
                    "itens": {
                        "agua": 1,
                        "comida": 0,
                        "medicamento": 0,
                        "municao": 0
                    },
                },
                {
                    "sobrevivente": 101,
                    "itens": {
                        "agua": 0,
                        "comida": 1,
                        "medicamento": 0,
                        "municao": 1
                    },
                }
            ]
        }
        request = self.client.post('/sobreviventes/troca/', payload, format="json")
        self.assertEqual(request.status_code, status.HTTP_200_OK)

class TestarTrocaItensInvalida(APITestCase):
    def test_trocar_itens_pontos_invalidos(self):
        Sobrevivente.objects.create(
            id=100,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )

        Sobrevivente.objects.create(
            id=101,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )

        Inventario.objects.create(
            sobrevivente_id=100,
            agua=10,
            comida=10,
            medicamento=10,
            municao=10,
            outros_itens="Teste"
        )

        Inventario.objects.create(
            sobrevivente_id=101,
            agua=10,
            comida=10,
            medicamento=10,
            municao=10,
            outros_itens="Teste"
        )

        payload = {
            "troca": [
                {
                    "sobrevivente": 100,
                    "itens": {
                        "agua": 1,
                        "comida": 0,
                        "medicamento": 0,
                        "municao": 0
                    },
                },
                {
                    "sobrevivente": 101,
                    "itens": {
                        "agua": 0,
                        "comida": 1,
                        "medicamento": 1,
                        "municao": 1
                    },
                }
            ]
        }

        request = self.client.post('/sobreviventes/troca/', payload, format="json")
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_trocar_itens_sem_estoque(self):
        Sobrevivente.objects.create(
            id=100,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )

        Sobrevivente.objects.create(
            id=101,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )

        Inventario.objects.create(
            sobrevivente_id=100,
            agua=0,
            comida=0,
            medicamento=0,
            municao=0,
            outros_itens="Teste"
        )

        Inventario.objects.create(
            sobrevivente_id=101,
            agua=0,
            comida=0,
            medicamento=0,
            municao=0,
            outros_itens="Teste"
        )

        payload = {
            "troca": [
                {
                    "sobrevivente": 100,
                    "itens": {
                        "agua": 1,
                        "comida": 0,
                        "medicamento": 0,
                        "municao": 0
                    },
                },
                {
                    "sobrevivente": 101,
                    "itens": {
                        "agua": 0,
                        "comida": 1,
                        "medicamento": 0,
                        "municao": 1
                    },
                }
            ]
        }

        request = self.client.post('/sobreviventes/troca/', payload, format="json")
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_trocar_itens_sobrevivente_infectado(self):
        Sobrevivente.objects.create(
            id=100,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123,
            infectado = True
        )

        Sobrevivente.objects.create(
            id=101,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=123
        )

        Inventario.objects.create(
            sobrevivente_id=100,
            agua=10,
            comida=10,
            medicamento=10,
            municao=10,
            outros_itens="Teste"
        )

        Inventario.objects.create(
            sobrevivente_id=101,
            agua=10,
            comida=10,
            medicamento=10,
            municao=10,
            outros_itens="Teste"
        )

        payload = {
            "troca": [
                {
                    "sobrevivente": 100,
                    "itens": {
                        "agua": 1,
                        "comida": 0,
                        "medicamento": 0,
                        "municao": 0
                    },
                },
                {
                    "sobrevivente": 101,
                    "itens": {
                        "agua": 0,
                        "comida": 1,
                        "medicamento": 0,
                        "municao": 1
                    },
                }
            ]
        }

        request = self.client.post('/sobreviventes/troca/', payload, format="json")
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

class TestaRelatorio(APITestCase):
    def testa_relatorio(self):
        uuid_teste = uuid.uuid4()

        Sobrevivente.objects.create(
            id=100,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=uuid_teste,
            infectado = True
        )

        Sobrevivente.objects.create(
            id=101,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=uuid_teste
        )

        Sobrevivente.objects.create(
            id=102,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=uuid_teste
        )

        Sobrevivente.objects.create(
            id=103,
            nome="Teste",
            idade=20,
            sexo="M",
            jogo_id=uuid_teste
        )

        Inventario.objects.create(
            sobrevivente_id=100,
            agua=10,
            comida=10,
            medicamento=10,
            municao=10,
            outros_itens="Teste"
        )

        Inventario.objects.create(
            sobrevivente_id=101,
            agua=10,
            comida=10,
            medicamento=10,
            municao=10,
            outros_itens="Teste"
        )

        Inventario.objects.create(
            sobrevivente_id=102,
            agua=10,
            comida=10,
            medicamento=10,
            municao=10,
            outros_itens="Teste"
        )

        Inventario.objects.create(
            sobrevivente_id=103,
            agua=10,
            comida=10,
            medicamento=10,
            municao=10,
            outros_itens="Teste"
        )

        request = self.client.get(f'/sobreviventes/{uuid_teste}/relatorio/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        self.assertEqual(request.data["porcentagem_sobreviventes_infectados"], 25)
        self.assertEqual(request.data["porcentagem_sobreviventes_nao_infectados"], 75)
        self.assertEqual(request.data["pontos_perdidos"], 100)
        

        self.assertEqual(request.data['quantidade_media_itens_nao_infectados']['agua'], 10)
        self.assertEqual(request.data['quantidade_media_itens_nao_infectados']['comida'], 10)
        self.assertEqual(request.data['quantidade_media_itens_nao_infectados']['medicamento'], 10)
        self.assertEqual(request.data['quantidade_media_itens_nao_infectados']['municao'], 10)

        self.assertEqual(request.data['quantidade_itens_perdidos']['agua'], 10)
        self.assertEqual(request.data['quantidade_itens_perdidos']['comida'], 10)
        self.assertEqual(request.data['quantidade_itens_perdidos']['medicamento'], 10)
        self.assertEqual(request.data['quantidade_itens_perdidos']['municao'], 10)
    
    def testa_relatorio_invalido(self):
        uuid_teste = uuid.uuid4()

        request = self.client.get(f'/sobreviventes/{uuid_teste}/relatorio/')
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)