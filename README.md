# Ferramenta para grafos
- Este repositório contém uma ferramenta com interface em linha de comando na qual é possível aplicar conceitos estudados em Teoria dos Grafos a partir de um arquivo json.
- Esta ferramenta também é um trabalho prático da matéria de Teoria dos Grafos.
- No trabalho, foi solicitado que os alunos buscassem criar os comandos e suas funcionalidades, e também indicassem quais comandos conseguiram implementar e os que não conseguiram.
- Legenda:
  - [x] Feito

## Comandos para a execução da ferramenta
- [x] **grafos carrregar arquivo.json**: carrega o arquivo json;
- [x] **grafos mostrar grafos**: mostra todos os grafos do arquivo;
- [x] **grafos multigrafos**: mostra os multigrafos do arquivo;
- [x] **grafos pseudografos**: mostra os pseudografos do arquivo;
- [x] **grafos desconexos**: mostra os grafos desconexos do arquivo;
- [x] **grafos completos**: mostra os grafos completos do arquivo;
- [x] **grafos graus id=1**: indica quais os graus dos vértices do grafo com id=1;
- [x] **grafos grau id=1 vertice="A"**: informa os graus do vértice "A" no grafo com id=1;
- [x] **grafos alcancaveis id=1 partida="A"**: indica quais vértices do grafo de id=1 são alcançáveis a partir do vértice A;
- [x] **grafos inalcancaveis id=1 partida="A"**: indica quais vértices do grafo de id=1 são inalcançáveis a partir do vértice "A";
- [x] **grafos bfs id=1 partida="A" chegada="B"**: informa o caminho partindo do vértice = A até chegar no vértice=B usando o algoritmo BFS no grafo de id=1;
- [x] **grafos dfs id=1 partida="A" chegada="B"**: mostra o caminho a partir do vértice = A até chegar no vértice=B usando o algoritmo BFS no grafo de id=1;
- [x] **grafos sair**: finaliza a execução da ferramenta.