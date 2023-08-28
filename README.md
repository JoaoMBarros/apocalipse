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
- ([GET](#buscar-sobreviventes) | [POST](#adicionar-sobrevivente)) /sobreviventes/ 
- ([GET](#informacao-sobrevivente)) /sobreviventes/id_do_sobrevivente/
- ([GET](#sobrevives-simulacao)) /sobreviventes/id_jogo/
- ([GET](#nova-acao)) /sobreviventes/id_jogo/nova_acao/
- ([GET](#nova-simulacao)) /sobreviventes/novo_jogo/
- ([GET](#detalhes-inventario)) /sobreviventes/id_do_sobrevivente/inventario/
- ([GET](#relatorio-final)) /sobreviventes/id_do_jogo/relatorio/
- ([POST](#troca-de-itens)) /sobreviventes/troca/
- ([PUT](#atualiza-usuario)) /sobreviventes/id_do_sobrevivente/
- ([PATCH](#atualiza-localizacao)) /sobreviventes/localizacao/
- ([PATCH](#avistado-infectado)) /sobreviventes/infectado/
- ([DELETE](#finaliza-simulacao)) /sobreviventes/id_jogo/deletar/