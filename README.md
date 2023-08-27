# API de um minigame de sobrevivência

# Tecnologias
Python, Django, Django Rest, Postgres, HTML, CSS, Javascript, Vue 3.

## Features
- Criação e atualização de sobreviventes
- Listagem de sobreviventes geral e específico
- Detalhes de inventário
- Troca de itens entre sobreviventes
- Infecção de sobreviventes
- Ações aleatórias de sobreviventes
- Relatório final

## API Endpoints
#### GET
- [#](#Buscar-sobreviventes) /sobreviventes/ 
- /sobreviventes/id_do_sobrevivente/
- /sobreviventes/id_jogo/
- /sobreviventes/id_jogo/nova_acao/
- /sobreviventes/novo_jogo/
- /sobreviventes/id_do_sobrevivente/inventario/
- /sobreviventes/id_do_jogo/relatorio/

#### POST
- /sobreviventes/
- /troca/

#### PUT
- /sobreviventes/id_do_sobrevivente/

#### PATCH
- /sobreviventes/localizacao/
- /sobreviventes/infectado/

#### DELETE
- sobreviventes/id_jogo/deletar/

## Buscar sobreviventes