import java.util.Scanner;

public class Acoes {

    private Scanner sc = new Scanner(System.in);
    private Grafo g = new Grafo("G");

    public void adicionarVertice() {

        System.out.print("Insira o nome do vértice: ");
        String nomeV = sc.nextLine();
        Vertice v = new Vertice(nomeV);

        g.adicionarVertice(v);
    }

    public void adicionarAresta() {
        System.out.print("Vértice v1: ");
        String v1 = sc.nextLine();

        System.out.print("Vértice v2: ");
        String v2 = sc.nextLine(); 

        System.out.print("Insira o identificador da aresta: ");
        String aresta = sc.nextLine();

        g.adicionarAresta(new Vertice(v1), new Vertice(v2), aresta);
    }

    public void mostrarGrafo() {
        g.retonarGrafo();
    }

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
