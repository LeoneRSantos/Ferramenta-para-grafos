class Graus:
    @staticmethod
    def encontrarOsGrausDosVertices(grafos, idDoGrafo):
        for grafo in grafos:
            if grafo['id'] == idDoGrafo:
                vertices = grafo['vertices']
                arestas = grafo['edges']
                graus = {vertex: 0 for vertex in vertices}
                for edge in arestas:
                    graus[edge[0]] += 1
                    graus[edge[1]] += 1
                print("\nGraus dos vértices do grafo ", idDoGrafo, ":")
                for vertex, grau in graus.items():
                    print("\nVértice: ", vertex, "\nGrau: ", grau)
                return
        print("\nGrafo não encontrado: ", idDoGrafo)

    @staticmethod
    def encontrarOGrauDoVertice(grafos, idDoGrafo, vertice):
        for grafo in grafos:
            if grafo['id'] == idDoGrafo:
                arestas = grafo['edges']
                grau = 0
                for aresta in arestas:
                    if aresta[0] == vertice:
                        grau += 1
                    if aresta[1] == vertice:
                        grau += 1
                print("\nGrau do vértice ", vertice, " no grafo ", idDoGrafo, ": ", grau)
                return
        print("\nO grafo ", idDoGrafo, " não foi encontrado.")