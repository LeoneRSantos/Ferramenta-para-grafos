class Grafo:
    def __init__(self, nome, listaDeVertices, listaDeArestas):
        self.setNome = nome
        self.setVertices = listaDeVertices
        self.setArestas = listaDeArestas

    # Getter e setter
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setArestas(self, arestas):
        self.arestas = arestas

    def getArestas(self):
        return self.arestas
    
    def setVertices(self, vertices):
        self.vertices = vertices

    def getVertices(self):
        return self.vertices


    def __verificarAdjacencia(self):
        for aresta in self.__arestas:
            self.__lista_de_Adjacentes[aresta.pontoA].append(
                self.__select_vertice(aresta.pontoB)
            )
            self.__lista_de_Adjacentes[aresta.pontoB].append(
                self.__select_vertice(aresta.pontoA)
            )
        
