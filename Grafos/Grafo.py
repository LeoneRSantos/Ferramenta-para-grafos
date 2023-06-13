from Aresta import Aresta
from Vertice import Vertice


class Grafo:
    def __init__(self):
        self.listaDeAdjacencia = []
        self.listaDeVertices = []
        self.listaDeArestas = []

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
    
    # Adicionar vértices e arestas

    def adicionarVertices(self, vertices):
        self.listaDeVertices = [Vertice(id) for id in vertices]
        self.criarListaDeAdjacencia()

    # Definir a lista de adjacência
    def criarListaDeAdjacencia(self):
        for i in self.listaDeVertices:
            self.listaDeAdjacencia[i.nome] = []
    
    def adicionarArestas(self, arestas):
        self.__verificarAdjacencia()
        self.listaDeArestas = [
            Aresta(aresta[0], aresta[1]) for aresta in enumerate(arestas)
        ]

    

    def __verificarAdjacencia(self):
        for aresta in self.__arestas:
            self.listaDeAdjacencia[aresta.pontoA].append(
                self.verificarVertice(aresta.pontoB)
            )
            self.listaDeAdjacencia[aresta.pontoB].append(
                self.verificarVertice(aresta.pontoA)
            )
    
    def verificarVertice(self, nome_vertice):
        for vertice in self.__lista_de_Vertices:
            if vertice.nome == nome_vertice:
                return vertice
        else:
            return None
        
