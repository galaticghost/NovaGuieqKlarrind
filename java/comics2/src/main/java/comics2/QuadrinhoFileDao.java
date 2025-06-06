package comics2;

import java.util.List;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class QuadrinhoFileDao {
    private String arquivo = "quadrinhos.csv";

    public QuadrinhoFileDao() {

    }

    public QuadrinhoFileDao(String arquivo) {
        this.arquivo = arquivo;
    }

    private List<Quadrinho> carregarQuadrinhos() {
        int totalLinha = 0;
        int totalImportado = 0;
        List<Quadrinho> quadrinhos = new ArrayList<>();
        List<Integer> linhasErradas = new ArrayList<>();
        List<String> linhasErradasContent = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(this.arquivo))) {
            br.readLine();
            String linha;
            while ((linha = br.readLine()) != null) {
                totalLinha++;
                String[] campos = linha.split(",");
                if (campos.length == 4) {
                    String titulo = campos[0];
                    String autor = campos[1];
                    String artista = campos[2];
                    String editora = campos[3];
                    quadrinhos.add(new Quadrinho(titulo, autor, artista, editora));
                    totalImportado++;
                } else if (campos.length == 5) {
                    int id = Integer.parseInt(campos[0]);
                    String titulo = campos[1];
                    String autor = campos[2];
                    String artista = campos[3];
                    String editora = campos[4];
                    quadrinhos.add(new Quadrinho(titulo, autor, artista, editora, id));
                    totalImportado++;
                } else {
                    linhasErradas.add(totalLinha + 1);
                    linhasErradasContent.add(linha);
                }
            }
        } catch (Exception e) {
            System.err.println("Erro ao carregar os dados: " + e.getMessage());
        }
        System.out.println("Total de linhas: " + totalLinha);
        System.out.println("Quadrinhos importados: " + totalImportado);
        System.out.println("Linhas erradas: " + linhasErradas);
        System.out.println("Conteúdo errado: " + linhasErradasContent);
        return quadrinhos;
    }

    public void gravarQuadrinhos() {
        try {
            List<Quadrinho> quadrinhos = carregarQuadrinhos();
            QuadrinhoDao dao = new QuadrinhoDao("jdbc:sqlite:java/comics2/quadrinhos.db");

            for (Quadrinho q : quadrinhos) {
                dao.inserir(q);
            }
        } catch (Exception e) {
            System.err.println("Erro ao carregar os dados: " + e.getMessage());
        }
    }
}
