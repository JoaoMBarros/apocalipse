# API Simulação de sobrevivência

## Tecnologias
Python, Django, Django Rest, Postgres, Docker.

## Como Rodar Localmente

### Dentro da Pasta da API

1. Crie e ative uma máquina virtual (opcional, mas recomendado para isolar as dependências do projeto).

   ```bash
   python -m venv nome_da_maquina_virtual
   source nome_da_maquina_virtual/bin/activate
   ```

2. Instale as dependências do projeto utilizando o arquivo `requirements.txt`.

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Abra um terminal e navegue até a pasta raiz da API.

4. Execute os seguintes comandos:
   - `python manage.py makemigrations sobreviventes`
   - `python manage.py migrate`
   - `python manage.py runserver`

**Observação:** Caso você não tenha o PostgreSQL instalado, lembre-se de ajustar as configurações do arquivo "settings" para usar outro banco de dados compatível.

Isso iniciará o servidor de desenvolvimento local e permitirá que você acesse a API através do seu navegador ou de ferramentas como o Postman.

## Features
- Criação e atualização de sobreviventes
- Listagem de sobreviventes geral e específico
- Detalhes de inventário
- Troca de itens entre sobreviventes
- Infecção de sobreviventes
- Ações aleatórias de sobreviventes
- Relatório final

# API Endpoints

## Nova Simulação

Este endpoint permite iniciar uma nova simulação, criando um novo jogo com sobreviventes.

### Endpoint

`GET /sobreviventes/novo_jogo/`

Inicia uma nova simulação e retorna um UUIDv4 único que representa o ID do novo jogo.

#### Exemplo de Requisição

```http
GET /sobreviventes/novo_jogo/
```

#### Exemplo de Resposta

```
UUIDv4 único que representa o ID do novo jogo
```

## Todos sobreviventes
Esta classe lida com a busca e criação de informações de sobreviventes no banco de dados.

**Endpoint**

GET `/api/sobreviventes/`

Retorna uma lista de todos os sobreviventes cadastrados no banco de dados.

#### Exemplo de Requisição
```http
GET /api/sobreviventes/
```

#### Exemplo de Resposta
```json
[
    {
        "id": 3,
        "jogo_id": "d6c45f06-45bf-11ee-be56-0242ac120002",
        "nome": "Pedro",
        "idade": 29,
        "sexo": "M",
        "latitude": -7.107016771761896,
        "longitude": 13.469174428535027,
        "avistado_infectado": 0,
        "infectado": false
    }
    // ... outros sobreviventes
]
```

**POST `/api/sobreviventes/`**

Cria um novo sobrevivente no banco de dados juntamente com as informações de seu inventário.

#### Exemplo de Requisição
```json
POST /api/sobreviventes/

{
    "sobrevivente": {
        "nome": "Pedro",
        "idade": 29,
        "sexo": "M",
        "jogo_id": "d6c45f06-45bf-11ee-be56-0242ac120002"
    },
    "inventario": {
        "agua": 10,
        "comida": 10,
        "medicamente": 10,
        "municao": 10
    }
}
```

#### Exemplo de Resposta
```json
{
    "id": 3,
    "jogo_id": "d6c45f06-45bf-11ee-be56-0242ac120002",
    "nome": "Pedro",
    "idade": 29,
    "sexo": "M",
    "latitude": -7.107016771761896,
    "longitude": 13.469174428535027,
    "avistado_infectado": 0,
    "infectado": false
}
```

## Informação Sobrevivente

Este endpoint fornece informações detalhadas sobre um sobrevivente específico com base no ID do sobrevivente.

### Endpoint

**GET `/sobreviventes/id_do_sobrevivente/`**

Retorna informações detalhadas sobre o sobrevivente com o ID especificado.

#### Parâmetros

- `id_do_sobrevivente` (int): O ID único do usuário.

#### Exemplo de Requisição

```http
GET /sobreviventes/3/
```

#### Exemplo de Resposta

```json
{
    "id": 3,
    "jogo_id": "d6c45f06-45bf-11ee-be56-0242ac120002",
    "nome": "Pedro",
    "idade": 29,
    "sexo": "M",
    "latitude": -7.107016771761896,
    "longitude": 13.469174428535027,
    "avistado_infectado": 0,
    "infectado": false
}
```

**PUT `/sobreviventes/id_do_sobrevivente/`**

Atualiza informações do sobrevivente, como nome, idade e sexo, com base no ID do sobrevivente.

#### Parâmetros

- `id_do_sobrevivente` (int): O ID único do sobrevivente a ser atualizado.

#### Exemplo de Requisição

```http
PUT /sobreviventes/3/

{
    "nome": "Novo Nome",
    "idade": 30,
    "sexo": "F"
}
```

#### Exemplo de Resposta

```json
{
    "id": 3,
    "jogo_id": "d6c45f06-45bf-11ee-be56-0242ac120002",
    "nome": "Novo Nome",
    "idade": 30,
    "sexo": "F",
    "latitude": -7.107016771761896,
    "longitude": 13.469174428535027,
    "avistado_infectado": 0,
    "infectado": false
}
```

## Sobreviventes Simulação
Este endpoint retorna informações sobre os sobreviventes de uma simulação específica com base no ID do jogo.

**Endpoint**

GET `/sobreviventes/id_jogo/`

Retorna uma lista de todos os sobreviventes da simulação com o ID do jogo especificado.

#### Parâmetros
- `id_jogo` (UUIDv4): O ID único da simulação (UUID versão 4).

#### Exemplo de Requisição
```http
GET /sobreviventes/d6c45f06-45bf-11ee-be56-0242ac120002/
```

#### Exemplo de Resposta
```json
[
    {
        "id": 3,
        "jogo_id": "d6c45f06-45bf-11ee-be56-0242ac120002",
        "nome": "Pedro",
        "idade": 29,
        "sexo": "M",
        "latitude": -7.107016771761896,
        "longitude": 13.469174428535027,
        "avistado_infectado": 0,
        "infectado": false
    }
    // ... outros sobreviventes
]
```

## Detalhes Inventário

Este endpoint retorna os detalhes do inventário de um sobrevivente específico com base no ID do sobrevivente.

### Endpoint

`GET /sobreviventes/id_do_sobrevivente/inventario/`

Retorna os detalhes do inventário do sobrevivente com o ID especificado.

#### Parâmetros

- `id_do_sobrevivente` (int): O ID único do sobrevivente.

#### Exemplo de Requisição

```http
GET /sobreviventes/3/inventario/
```

#### Exemplo de Resposta

```json
{
    "id": 3,
    "agua": 10,
    "comida": 10,
    "medicamento": 0,
    "municao": 10,
    "outros_itens": "",
    "sobrevivente": 3
}
```

## Nova Ação

Este endpoint permite registrar novas ações realizadas por sobreviventes em uma simulação específica, com base no ID do jogo.

### Endpoint

**GET `/sobreviventes/id_jogo/nova_acao/`**

Registra uma nova ação realizada por um sobrevivente na simulação com o ID do jogo especificado.

#### Parâmetros

- `id_jogo` (UUIDv4): O ID único da simulação (UUID versão 4).

#### Exemplo de Requisição

```http
GET /sobreviventes/d6c45f06-45bf-11ee-be56-0242ac120002/nova_acao/
```

#### Exemplos de Resposta

##### Ação "fugiu"

```json
{
    "acao": "fugiu",
    "sobrevivente": 3
}
```

##### Ação "troca"

```json
{
    "acao": "troca",
    "sobrevivente": 3,
    "outro_sobrevivente": 4
}
```

##### Ação "visto_infectado"

```json
{
    "acao": "visto_infectado",
    "sobrevivente": 4,
    "outro_sobrevivente": 3
}
```

## Troca de Itens

Este endpoint permite realizar trocas de itens entre sobreviventes.

### Endpoint

`POST /sobreviventes/troca/`

Realiza uma troca de itens entre os sobreviventes especificados.

#### Exemplo de Requisição

```http
POST /sobreviventes/troca/

{
    "troca": [
        {
            "sobrevivente": 3,
            "itens": {
                "agua": 1,
                "comida": 10,
                "medicamento": 0,
                "municao": 0
            }
        },
        {
            "sobrevivente": 2,
            "itens": {
                "agua": 1,
                "comida": 0,
                "medicamento": 0,
                "municao": 0
            }
        }
    ]
}
```

#### Exemplo de Resposta

```json
"Troca realizada com sucesso"
```

## Atualiza Localização

Este endpoint permite atualizar a localização de um sobrevivente específico.

### Endpoint

**PATCH `/sobreviventes/localizacao/`**

Atualiza a localização do sobrevivente com base no ID do sobrevivente.

#### Parâmetros

- `sobrevivente` (int): O ID único do sobrevivente.
- `latitude` (float): A nova latitude a ser atribuída.
- `longitude` (float): A nova longitude a ser atribuída.

#### Exemplo de Requisição

```http
PATCH /sobreviventes/localizacao/

{
    "sobrevivente": 3,
    "latitude": 0.0,
    "longitude": 0.0
}
```

#### Exemplo de Resposta

```json
{
    "latitude": 0.0,
    "longitude": 0.0
}
```

## Avistado Infectado

Este endpoint permite marcar um sobrevivente como avistado infectado.

### Endpoint

**PATCH `/sobreviventes/infectado/`**

Marca um sobrevivente como avistado infectado com base no ID do sobrevivente.

#### Exemplo de Requisição

```http
PATCH /sobreviventes/infectado/

{
    "sobrevivente": 3
}
```

#### Exemplo de Resposta

```json
{
    "message": "Sobrevivente marcado como avistado infectado"
}
```

## Relatório Final

Este endpoint gera um relatório final sobre uma simulação específica com base no ID do jogo.

### Endpoint

**GET `/sobreviventes/id_jogo/relatorio/`**

Gera um relatório final sobre a simulação com o ID do jogo especificado.

#### Parâmetros

- `id_jogo` (UUIDv4): O ID único da simulação (UUID versão 4).

#### Exemplo de Requisição

```http
GET /sobreviventes/d6c45f06-45bf-11ee-be56-0242ac120002/relatorio/
```

#### Exemplo de Resposta

```json
{
    "porcentagem_sobreviventes_infectados": 0,
    "porcentagem_sobreviventes_nao_infectados": 100,
    "quantidade_media_itens_nao_infectados": {
        "agua": 10.0,
        "comida": 10.0,
        "medicamento": 0.0,
        "municao": 10.0
    },
    "pontos_perdidos": 0,
    "quantidade_itens_perdidos": {
        "agua": 0,
        "comida": 0,
        "medicamento": 0,
        "municao": 0
    }
}
```

## Finaliza Simulação

Este endpoint permite finalizar uma simulação específica com base no ID do jogo.

### Endpoint

**DELETE `/sobreviventes/id_jogo/deletar/`**

Finaliza a simulação com o ID do jogo especificado.

#### Parâmetros

- `id_jogo` (UUIDv4): O ID único da simulação (UUID versão 4).

#### Exemplo de Requisição

```http
DELETE /sobreviventes/d6c45f06-45bf-11ee-be56-0242ac120002/deletar/
```

#### Exemplo de Resposta (código 204)

```json

```

Este endpoint permite finalizar a simulação associada ao ID do jogo especificado. Após a conclusão bem-sucedida, a resposta não contém um corpo de mensagem, apenas o código de status 204 para indicar que a solicitação foi processada com sucesso, mas não há conteúdo para retornar.