#!/usr/bin/env python3
import json
from TiposDeGrafos import TiposDeGrafos
from Graus import Graus


class CarregarGrafos:

    continuar = True

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

    def interpretarString(self, stringInserida):
        if stringInserida[0] == 'grafos':
            if len(stringInserida) == 3 and stringInserida[1] == 'carregar':
                self.carregarArquivoJson(stringInserida[2])

            elif stringInserida[1] == 'sair':
                print('\nGrafos desligado\n')
                self.continuar = False

            elif stringInserida[1] == 'mostrar' and stringInserida[2] == 'grafos':
                for cont in self.grafos:
                    print('\nGrafo ', cont["id"],  "\nVértices: ",
                          cont["vertices"], "\nArestas: ", cont["edges"], '\n\n')

            elif stringInserida[1] == 'multigrafos':
                TiposDeGrafos.verificarMultigrafo(self.grafos)

            elif stringInserida[1] == 'pseudografos':
                TiposDeGrafos.verificarPseudoGrafo(self.grafos)

            elif stringInserida[1] == 'desconexos':
                TiposDeGrafos.verificarDesconexo(self.grafos)

            elif stringInserida[1] == 'completos':
                TiposDeGrafos.verificarGrafosCompletos(self.grafos)

            elif stringInserida[1] == 'graus' and len(stringInserida) == 3:
                idDoGrafo = int(stringInserida[2].split('=')[1])
                Graus.encontrarOsGrausDosVertices(self.grafos, idDoGrafo)

            elif stringInserida[1] == 'grau' and len(stringInserida) == 4:
                idDoGrafo = int(stringInserida[2].split('=')[1])
                vertice = stringInserida[3].split('=')[1].strip('"')
                Graus.encontrarOGrauDoVertice(self.grafos, idDoGrafo, vertice)


        else:
            print(
                '\nComando não reconhecido, verifique se o comando foi digitado corretamente.')


def main():

    carregarGrafos = CarregarGrafos()

    while carregarGrafos.continuar:

        comando = str(input('\nGrafos está em execução. Insira um comando\n'))

        comandoAtual = comando.split()

        carregarGrafos.interpretarString(comandoAtual)


if __name__ == '__main__':
    main()
