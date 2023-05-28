import java.util.Scanner;

public class Acoes {

    private Scanner sc = new Scanner(System.in);
    private Grafo g = new Grafo("G");

    public void adicionarVertice() {
        // TODO: adicionar uma verificação pra saber se o vértice já existe

        System.out.print("Insira o nome do vértice: ");
        String nomeV = sc.nextLine();
        Vertice v = new Vertice(nomeV);

        g.adicionarVertice(v);
    }

    public void adicionarAresta() {
        // TODO: adicionar uma verificação pra saber se a aresta já existe
        System.out.print("Vértice v1: ");
        String v1 = sc.nextLine();

        System.out.print("Vértice v2: ");
        String v2 = sc.nextLine(); 

        System.out.print("Insira o identificador da aresta: ");
        String aresta = sc.nextLine();

        g.adicionarAresta(new Vertice(v1), new Vertice(v2), aresta);
        g.adicionarVertice(new Vertice(v1));
        g.adicionarVertice(new Vertice(v2));
    }

    public void mostrarGrafo() {
        g.retonarGrafo();
    }

    // TODO: substituir o menu por um reconhecedor de string
    // TODO: o reconhecedor de string deve reconhecer os comandos inseridos no terminal
    public void mostrarMenu() {

        StringBuilder menu = new StringBuilder();

        menu.append("\n\n----- Grafos -----\n");
        menu.append("1) Adicionar vértice\n");
        menu.append("2) Adicionar aresta\n");
        menu.append("3) Mostrar o grafo\n");
        menu.append("0) Sair\n");

        System.out.println(menu.toString());
    }
}
