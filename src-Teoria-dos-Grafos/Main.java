package src;
// TODO: estudar manipulação de arquivo json com Java 

import java.io.FileReader;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class Main {
    public static void main(String[] args) {
        // Converte o arquivo lido
        JSONParser jsonParser = new JSONParser();

        try(FileReader leitor = new FileReader("src/graphs.json")) {
            Object objetoVertice = jsonParser.parse(leitor);

            JSONArray verticesLista = (JSONArray) objetoVertice;

            verticesLista.forEach(vertice -> exibirParserGrafo((JSONObject) vertice));
        } catch (Exception e) {
           System.out.println(e.toString());
        }
    }

    private static void exibirParserGrafo(JSONObject pGrafo) {
        System.out.println("---------------");
        JSONArray verticesArray = (JSONArray) pGrafo.get("vertices");
        for (Object vertice : verticesArray) {
            System.out.print("\nVértices: " + vertice);
        }
        System.out.print("\n---------------");
    }

}
