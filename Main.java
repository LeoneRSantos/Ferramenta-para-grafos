public class Main {
    public static void main(String[] args) {
        Grafo g = new Grafo("G");
        Grafo g2 = new Grafo("G2");

        // Vértices de G
        Vertice a = new Vertice("A");
        Vertice b = new Vertice("B");
        Vertice c = new Vertice("C");
        Vertice d = new Vertice("D");
        
        g.adicionarVertice(a);
        g.adicionarVertice(b);
        g.adicionarVertice(c);
        g.adicionarVertice(d);

        // Vértices de G2
        Vertice e = new Vertice("E");
        Vertice f = new Vertice("F");
        Vertice gg = new Vertice("G");
        Vertice h = new Vertice("H");

        
        g2.adicionarVertice(e);
        g2.adicionarVertice(f);
        g2.adicionarVertice(gg);
        g2.adicionarVertice(h);

        // Arestas de G
        g.adicionarAresta(a, b, "ab");
        g.adicionarAresta(c, d, "cd");

        // Arestas de G2
        g2.adicionarAresta(e, f, "ef");
        g2.adicionarAresta(gg, h, "gh");

        g.retonarGrafo();
        g2.retonarGrafo();

    }
}
