class TiposDeGrafos:

    @staticmethod
    def verificarMultigrafo(listaDeGrafos):
        listaDeMultigrafos = []

        for cont in listaDeGrafos:
            arestas = [tuple(aresta) for aresta in cont['edges']]
            if len(cont['edges']) != len(set(arestas)):
                listaDeMultigrafos.append(cont['id']) 
        if len(listaDeMultigrafos) > 0:
            print('\nMultigrafos encontrados:\n', listaDeMultigrafos, '\n')

        else:
            print('\nNenhum multigrafo encontrado no arquivo')

    @staticmethod
    def verificarPseudoGrafo(listaDeGrafos):
        listaDePseudoGrafos = []

        for cont in listaDeGrafos:
            vertices = cont['vertices']
            arestas = cont['edges']

            for aresta in arestas:
                if aresta[0]==aresta[1] and aresta[0] in vertices:
                    listaDePseudoGrafos.append(cont['id'])

        if len(listaDePseudoGrafos) > 0:
            print('\nPseudografos encontrados: ', listaDePseudoGrafos)
        
        else:
            print('\nNenhum pseudografo encontrado no arquivo.')

    @staticmethod
    def verificarConexao(vertices, arestas):
        if not vertices:
            return False
        verticesAlcancaveis = set()
        queue = [vertices[0]] 
        while queue:
            verticeAtual = queue.pop(0)
            verticesAlcancaveis.add(verticeAtual)
            for aresta in arestas:
                if aresta[0] == verticeAtual and aresta[1] not in verticesAlcancaveis:
                    verticesAlcancaveis.add(aresta[1])
                    queue.append(aresta[1])
                elif aresta[1] == verticeAtual and aresta[0] not in verticesAlcancaveis:
                    verticesAlcancaveis.add(aresta[0])
                    queue.append(aresta[0])
        return len(verticesAlcancaveis) == len(vertices) 
