package src;
public class Aresta {
    Vertice verticeUm;
    Vertice verticeDois;
    String id;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Aresta(Vertice verticeUm, Vertice verticeDois, String id) {
        setVerticeUm(verticeUm);
        setVerticeDois(verticeDois);
        setId(id);
    }

    public Vertice getVerticeUm() {
        return verticeUm;
    }

    public void setVerticeUm(Vertice verticeUm) {
        this.verticeUm = verticeUm;
    }

    public Vertice getVerticeDois() {
        return verticeDois;
    }

    public void setVerticeDois(Vertice verticeDois) {
        this.verticeDois = verticeDois;
    }
}
