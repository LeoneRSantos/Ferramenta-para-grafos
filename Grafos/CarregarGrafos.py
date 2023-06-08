import json

from Grafo import Grafo 

class CarregarGrafos:

    with open('graphs.json') as teste:
        grafos = json.load(teste)
        dados = grafos["graphs"]

    continuar = True 

    while continuar:

        comando = str(input('\nGrafos está em execução. Insira um comando\n'))

        if comando == 'grafos carregar arquivo.json':
            
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





    