class TiposDeGrafos:

    @staticmethod
    def verificarMultigrafo(listaDeGrafos):
        listaDeMultigrafos = []

    for cont in grafos:
        arestas = [tuple(aresta) for aresta in cont['edges']]
        if len(cont['edges']) != len(set(arestas)):
            listaDeMultigrafos.append(cont['id']) 
    if len(listaDeMultigrafos) > 0:
        print('\nMultigrafos encontrados:\n', listaDeMultigrafos, '\n')

    else:
        print('\nNenhum multigrafo encontrado no arquivo')

def verificarPseudoGrafo(grafos):
    listaDePseudoGrafos = []

    for cont in grafos:
        vertices = cont['vertices']
        arestas = cont['edges']

        for aresta in arestas:
            if aresta[0]==aresta[1] and aresta[0] in vertices:
                listaDePseudoGrafos.append(cont['id'])

    if len(listaDePseudoGrafos) > 0:
        print('\nPseudografos encontrados: ', listaDePseudoGrafos)
    
    else:
        print('\nNenhum pseudografo encontrado no arquivo.')

