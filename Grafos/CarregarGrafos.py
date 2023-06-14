import json

from Grafo import Grafo 

class CarregarGrafos:

    with open('graphs.json') as teste:
        grafos = json.load(teste)
        dados = grafos["graphs"]

    continuar = True 
    g1 = Grafo()

    def __init__(self):
        self.grafos = []

    def carregarArquivoJson(self, arquivoJson):
        try:
            with open(arquivoJson, 'r') as file:
                dados = json.load(file)
                self.grafos = dados['graphs']
                print("\nGrafos carregados a partir do arquivo ", arquivoJson)
        except FileNotFoundError:
            print("\nArquivo não econtrado. Verifique se o nome inserido está correto.\n")

        if comando == 'grafos carregar arquivo.json':
            for cont in dados:
                idAtual = cont["id"]
                for cont2 in idAtual:
                    g1.adicionarVertices(idAtual['vertices'])
            print('\nO arquivo foi carregado.')

        elif comando == 'grafos mostrar grafos':
            for g in dados:
                print('\nGrafo ', g["id"],  "\nVértices: ", g["vertices"], "\nArestas: ", g["edges"], '\n\n')

            # Pegar o id do grafo
            # for i in dados:
            #     if(i["id"] == 1):
            #         vertices = i["vertices"]
            #         arestas = i["edges"]

            #         print("Vertices: ", vertices, " arestas: ", arestas)

            #     numero = int(input('\nInsira um número ')) 
        elif comando == 'grafos sair' or comando == 'sair':
            print('Grafos desligado')
            continuar = False
        else:
            print('\nComando não reconhecido, verifique se o comando foi digitado corretamente.')





    
