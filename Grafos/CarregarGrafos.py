import json

from Grafo import Grafo 

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
                    print('\nGrafo ', cont["id"],  "\nVértices: ", cont["vertices"], "\nArestas: ", cont["edges"], '\n\n')

        else:
                print('\nComando não reconhecido, verifique se o comando foi digitado corretamente.')



def main():

    carregarGrafos = CarregarGrafos()

    while carregarGrafos.continuar:

        comando = str(input('\nGrafos está em execução. Insira um comando\n'))

        comandoAtual = comando.split()

        carregarGrafos.interpretarString(comandoAtual)

    
if __name__ == '__main__':
    main()
            


    
