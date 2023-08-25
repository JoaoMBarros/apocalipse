from django.test import TestCase
from django.urls import reverse
from .models import Sobrevivente, Inventario

# Create your tests here.
class TesteListagemSobreviventes(TestCase):
    def test_listagem_sobreviventes(self):
        response = self.client.get('/sobreviventes/')
        self.assertEqual(response.status_code, 200)

class TesteCadastroSobrevivente(TestCase):
    def test_cadastro_sobrevivente(self):
        response = self.client.post('/sobreviventes/', {
            'nome': 'Teste',
            'idade': 20,
            'sexo': 'M',
            'latitude': 0,
            'longitude': 0,
            'avistado_infectado': 0,
            'infectado': False
        })
        self.assertEqual(response.status_code, 201)
    
    def test_cadastro_sobrevivente_sexo_invalido(self):
        response = self.client.post('/sobreviventes/', {
            'nome': 'Teste',
            'idade': 20,
            'sexo': 'X',
            'latitude': 0,
            'longitude': 0,
            'avistado_infectado': 0,
            'infectado': False
        })
        self.assertEqual(response.status_code, 400)

    def test_cadastro_sobrevivente_json_invalido(self):
        response = self.client.post('/sobreviventes/', {
            'idade': 20,
            'sexo': 'M',
            'latitude': 0,
            'longitude': 0,
            'avistado_infectado': 0,
            'infectado': False
        })
        self.assertEqual(response.status_code, 400)

class TesteBuscaSobrevivente(TestCase):
    # Criacao de um sobrevivente de testes diretamente no objects
    def setUp(self):
        from .models import Sobrevivente
        Sobrevivente.objects.create(
            id=100,
            nome='Teste',
            idade=20,
            sexo='M',
            latitude=0,
            longitude=0,
            avistado_infectado=0,
            infectado=False
        )

    def test_busca_sobrevivente(self):
        response = self.client.get('/sobreviventes/100/')
        self.assertEqual(response.status_code, 200)
    
    def test_busca_sobrevivente_invalido(self):
        response = self.client.get('/sobreviventes/5000/')
        self.assertEqual(response.status_code, 404)
    

class TesteAtualizacaoLocalizacaoSobrevivente(TestCase):

    # Criacao de um sobrevivente de testes diretamente no objects
    def setUp(self):
        from .models import Sobrevivente
        Sobrevivente.objects.create(
            id=100,
            nome='Teste',
            idade=20,
            sexo='M',
            latitude=0,
            longitude=0,
            avistado_infectado=0,
            infectado=False
        )

        response = self.client.get('/sobreviventes/100/')
        self.assertEqual(response.status_code, 200)
    
    # def test_atualizacao_localizacao_sobrevivente(self):
    #     url = reverse('localizacao', args=[1])

    #     response = self.client.patch(url, {
    #         'latitude': 0.0,
    #         'longitude': 0.0
    #     })

    #     print(response.content)
    #     self.assertEqual(response.status_code, 200)
    
    # def test_atualizacao_localizacao_sobrevivente_invalido(self):
    #     response = self.client.patch('/sobreviventes/1/localizacao/', {
    #         'latitude': 'teste',
    #         'longitude': 'teste'
    #     })
    #     self.assertEqual(response.status_code, 400)

class CriacaoDeInventario(TestCase):
    def setUp(self):
        from .models import Sobrevivente
        Sobrevivente.objects.create(
            id=100,
            nome='Teste',
            idade=20,
            sexo='M',
            latitude=0,
            longitude=0,
            avistado_infectado=0,
            infectado=False
        )

        response = self.client.get('/sobreviventes/100/')
        self.assertEqual(response.status_code, 200)
    
    def test_criacao_inventario(self):
        response = self.client.post('/sobreviventes/100/inventario/', {
            'sobrevivente': 100,
            'agua': 1,
            'comida': 1,
            'medicamento': 1,
            'municao': 1,
            'outros_itens': 'teste'
        })

        self.assertEqual(response.status_code, 201)
    
    def test_criacao_inventario_invalido(self):
        response = self.client.post('/sobreviventes/100/inventario/', {
            'agua': 'teste',
            'comida': 'teste',
            'medicamento': 'teste',
            'municao': 'teste',
            'outros_itens': 'teste'
        })
        self.assertEqual(response.status_code, 400)

class TesteTrocaItens(TestCase):
    def setUp(self):
        from .models import Sobrevivente
        Sobrevivente.objects.create(
            id=100,
            nome='Teste',
            idade=20,
            sexo='M',
            latitude=0,
            longitude=0,
            avistado_infectado=0,
            infectado=False
        )

        Sobrevivente.objects.create(
            id=200,
            nome='Teste',
            idade=20,
            sexo='M',
            latitude=0,
            longitude=0,
            avistado_infectado=0,
            infectado=False
        )

        response = self.client.get('/sobreviventes/100/')
        self.assertEqual(response.status_code, 200)

        # Criação do inventário de cada
        response = self.client.post('/sobreviventes/100/inventario/', {
            'sobrevivente': 100,
            'agua': 1,
            'comida': 1,
            'medicamento': 1,
            'municao': 1,
            'outros_itens': 'teste'
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['agua'], 1)
        inventario = Inventario.objects.get(sobrevivente=100)
        self.assertEqual(inventario.agua, 1)

        response = self.client.post('/sobreviventes/200/inventario/', {
            'sobrevivente': 200,
            'agua': 1,
            'comida': 1,
            'medicamento': 1,
            'municao': 1,
            'outros_itens': 'teste'
        })

        self.assertEqual(response.status_code, 201)
    
    # def test_troca_itens(self):
    #     payload = {
    #         "troca": [
    #             {
    #                 "sobrevivente": 100,
    #                 "itens": {
    #                     "agua": 1
    #                 }
    #             },
    #             {
    #                 "sobrevivente": 200,
    #                 "itens": {
    #                     "comida": 1,
    #                     "municao": 1
    #                 }
    #             }
    #         ]
    #     }

    #     response = self.client.post('/sobreviventes/troca/', data=payload)

    #     print(response.content)
    #     self.assertEqual(response.status_code, 200)

    #     # Verifica se os itens foram trocados
    #     response = self.client.get('/sobreviventes/100/inventario/')
    #     self.assertEqual(response.status_code, 100)
    #     self.assertEqual(response.data['agua'], 0)
    #     self.assertEqual(response.data['comida'], 2)
    #     self.assertEqual(response.data['medicamento'], 1)
    #     self.assertEqual(response.data['municao'], 2)

    #     response = self.client.get('/sobreviventes/200/inventario/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data['agua'], 2)
    #     self.assertEqual(response.data['comida'], 0)
    #     self.assertEqual(response.data['medicamento'], 1)
    #     self.assertEqual(response.data['municao'], 0)

class AvistaSobreviventeInfectado(TestCase):
    def setUp(self):
        Sobrevivente.objects.create(
            id=100,
            nome='Teste',
            idade=20,
            sexo='M',
            latitude=0,
            longitude=0,
            avistado_infectado=0,
            infectado=False
        )

        Inventario.objects.create(
            sobrevivente_id=100,
            agua=1,
            comida=1,
            medicamento=1,
            municao=1,
            outros_itens='teste'
        )

        response = self.client.get('/sobreviventes/100/')
        self.assertEqual(response.status_code, 200)
    
    def test_avista_sobrevivente_infectado(self):
        response = self.client.post('/sobreviventes/infectado/', {
            'sobrevivente': 100
        })
        self.assertEqual(response.status_code, 200)
        sobrevivente = Sobrevivente.objects.get(id=100)
        self.assertEqual(sobrevivente.avistado_infectado, 1)

    def test_avista_sobrevivente_infectado_3_vezes(self):
        response = self.client.post('/sobreviventes/infectado/', {
            'sobrevivente': 100
        })
        self.assertEqual(response.status_code, 200)
        sobrevivente = Sobrevivente.objects.get(id=100)
        self.assertEqual(sobrevivente.avistado_infectado, 1)
        self.assertEqual(sobrevivente.infectado, False)

        response = self.client.post('/sobreviventes/infectado/', {
            'sobrevivente': 100
        })
        self.assertEqual(response.status_code, 200)
        sobrevivente = Sobrevivente.objects.get(id=100)
        self.assertEqual(sobrevivente.avistado_infectado, 2)
        self.assertEqual(sobrevivente.infectado, False)

        response = self.client.post('/sobreviventes/infectado/', {
            'sobrevivente': 100
        })
        self.assertEqual(response.status_code, 200)
        sobrevivente = Sobrevivente.objects.get(id=100)
        self.assertEqual(sobrevivente.avistado_infectado, 3)
        self.assertEqual(sobrevivente.infectado, True)
    
    def test_avista_sobrevivente_invalido_infectado(self):
        response = self.client.post('/sobreviventes/infectado/', {
            'sobrevivente': 500
        })

        self.assertEqual(response.status_code, 404)