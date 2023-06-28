class Passeio:

    @staticmethod
    def encontrarVerticesAlcancaveis(grafos, idDoGrafo, verticeInicial):
        for grafo in grafos:
            if grafo['id'] == idDoGrafo:
                vertices = grafo['vertices']
                arestas = grafo['edges']
                verticeAlcancavel = [verticeInicial.strip('"')]
                fila = [verticeInicial]
                while fila:
                    verticeAtual = fila.pop(0)
                    for arestas in arestas:
                        if arestas[0] == verticeAtual and arestas[1] not in verticeAlcancavel:
                            verticeAlcancavel.append(arestas[1])
                            fila.append(arestas[1])
                        elif arestas[1] == verticeAtual and arestas[0] not in verticeAlcancavel:
                            verticeAlcancavel.append(arestas[0])
                            fila.append(arestas[0])
                print("\nNo grafo ", idDoGrafo, ":\nVértices alcançáveis a partir de ", verticeInicial, ": ", verticeAlcancavel)
                return
        print("\nNenhum vértice alcançável a partir de ", verticeInicial, " no grafo " ,idDoGrafo)

    @staticmethod
    def encontrarVerticesInalcancaveis(grafos, idDoGrafo, verticeInicial):
        for grafo in grafos:
            if grafo['id'] == idDoGrafo:
                vertices = grafo['vertices']
                arestas = grafo['edges']
                verticesAlcancaveis = [verticeInicial]
                queue = [verticeInicial]
                while queue:
                    current_vertex = queue.pop(0)
                    for aresta in arestas:
                        if aresta[0] == current_vertex and aresta[1] not in verticesAlcancaveis:
                            verticesAlcancaveis.append(aresta[1])
                            queue.append(aresta[1])
                        elif aresta[1] == current_vertex and aresta[0] not in verticesAlcancaveis:
                            verticesAlcancaveis.append(aresta[0])
                            queue.append(aresta[0])
                verticesInalcancaveis = [vertex for vertex in vertices if vertex not in verticesAlcancaveis]
                print("\nNo grafo ", idDoGrafo, ":\nVértices inalcançáveis a partir do vértice ", verticeInicial, ": ",verticesInalcancaveis)
                return
        print("\nNenhum vértice inalcançável a partir de ", verticeInicial, " no grafo ", idDoGrafo)