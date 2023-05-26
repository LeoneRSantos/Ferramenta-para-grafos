import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Boolean continuar = true;
        int aux = 4;
        Scanner sc = new Scanner(System.in);
        Acoes acoes = new Acoes();

        while (continuar) {
            acoes.mostrarMenu();

            System.out.print("\nEscolha uma opção ");
            aux = sc.nextInt();

            switch (aux) {
                case 1:
                    acoes.adicionarVertice();
                    continue;

                case 2:
                    acoes.adicionarAresta();
                    continue;

                case 3:
                    acoes.mostrarGrafo();
                    break;

                case 0:
                    continuar = false;
                    sc.close();
                    break;

                default:
                    continue;
            }
        }

    }

}
