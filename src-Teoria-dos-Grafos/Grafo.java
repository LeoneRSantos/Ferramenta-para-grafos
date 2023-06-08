package src;
import java.util.ArrayList;

public class Grafo {
    private String nome;
    private ArrayList<Vertice> vertices = new ArrayList<>();
    private ArrayList<Aresta> arestas = new ArrayList<>();

    public Grafo(String nome) {
        setNome(nome);
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void adicionarVertice(Vertice novoVertice) {

        vertices.add(novoVertice);
    }

    public void adicionarAresta(Vertice verticeUm, Vertice verticeDois, String id) {

        Aresta novaAresta = new Aresta(verticeUm, verticeDois, id);

        arestas.add(novaAresta);
    }

    // TODO: alterar o nome de 'retornar' para 'mostrar' ou 'exibir'
    public void retonarGrafo() {
        System.out.print("\n\nNo grafo " + getNome() + ": \n");

        // Vértices que pertencem ao grafo
        System.out.print("\nV = {");
        for (Vertice v : vertices) {
            System.out.print(v.getId() + ",");
        }

        // Arestas que pertencem ao grafo
        System.out.print("}\nA = {");
        for (Aresta a2 : arestas) {
            System.out.print(a2.getId() + ",");
        }
        System.out.print("}\n\n");

        // Incidências
        for (Aresta a : arestas) {
            System.out.print("A aresta " + a.getId() + " incide nos vértices " + a.verticeUm.getId() + " e "
                    + a.verticeDois.getId() + ".\n");
        }

    }
}
