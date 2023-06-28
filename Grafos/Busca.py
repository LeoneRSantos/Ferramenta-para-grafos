class Busca:

    @staticmethod
    def bfs(grafos, idDoGrafo, verticeInicial, verticeFinal):
        for grafo in grafos:
            if grafo['id'] == idDoGrafo:
                vertices = grafo['vertices']
                arestas = grafo['edges']
                fila = [[verticeInicial]]
                visitado = set()
                while fila:
                    path = fila.pop(0)
                    verticeAtual = path[-1]
                    if verticeAtual == verticeFinal:
                        print("\nNo grafo ", idDoGrafo, "BFS a partir do vértice ", verticeInicial, "até ",
                                verticeFinal,": ", path)
                        return
                    if verticeAtual in visitado:
                        continue
                    visitado.add(verticeAtual)
                    for aresta in arestas:
                        if aresta[0] == verticeAtual and aresta[1] not in visitado:
                            new_path = list(path)
                            new_path.append(aresta[1])
                            fila.append(new_path)
                        elif aresta[1] == verticeAtual and aresta[0] not in visitado:
                            new_path = list(path)
                            new_path.append(aresta[0])
                            fila.append(new_path)
                print("\nNenhum vértice encontrado através de BFS partindo de ", verticeInicial,
                        "até", verticeFinal)
                return
        print("\nNenhum vértice encontrado através de BFS partindo de ", verticeInicial,
                        "até", verticeFinal)
    
    @staticmethod
    def dfs(grafos, idDoGrafo, verticeInicial, verticeFinal):
        for grafo in grafos:
            if grafo['id'] == idDoGrafo:
                vertices = grafo['vertices']
                arestas = grafo['edges']
                pilha = [[verticeInicial]]
                visitado = set()
                while pilha:
                    path = pilha.pop()
                    verticeAtual = path[-1]
                    if verticeAtual == verticeFinal:
                        print("DFS path from", verticeInicial, "to", verticeFinal, "in graph", idDoGrafo, "is:", path)
                        return
                    if verticeAtual in visitado:
                        continue
                    visitado.add(verticeAtual)
                    for aresta in arestas:
                        if aresta[0] == verticeAtual and aresta[1] not in visitado:
                            new_path = list(path)
                            new_path.append(aresta[1])
                            pilha.append(new_path)
                        elif aresta[1] == verticeAtual and aresta[0] not in visitado:
                            new_path = list(path)
                            new_path.append(aresta[0])
                            pilha.append(new_path)
                print("No DFS path found from", verticeInicial, "to", verticeFinal, "in graph", idDoGrafo)
                return
        print("Graph not found:", idDoGrafo)