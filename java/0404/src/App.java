import java.util.ArrayList;
import java.util.Collections;

public class App {
    public static void main(String[] args) throws Exception {
        /*
         * ArrayList<Produto> ps;
         * Produto p1 = new Produto(5000.40, "TV");
         * Produto p2 = new Produto(3000.00, "Bluray");
         * Produto p3 = new Produto(2000.12, "Carro fiat Honda");
         * 
         * ps = new ArrayList<>();
         * ps.add(p1);
         * ps.add(p3);
         * ps.add(p2);
         * 
         * System.out.println(ps);
         * Collections.sort(ps);
         * System.out.println(ps);
         * 
         * ComparadorPorDescricao cpd;
         * cpd = new ComparadorPorDescricao();
         * ps.sort(cpd);
         * System.out.println(ps);
         */

        ArrayList<Aluno> alunos = new ArrayList<>(); // TODO GERADOR COM FOR e ARRAYS

        String[] nomes = { "CARLOS EDUARDO", "Joao Lauro", "Junior Moraes de Freitas",
                "Leonardo 'Dominik' Machado", "JEduardo", "Henrique", "Predo Preus", "PH", "Xi Jiping",
                "Fulano da silva" };

        int[] idades = { 50, 20, 24, 18, 20, 20, 20, 20, 52, 18 };

        double[] notas = { 2.00, 8.00, 11.50, 8.50, 6.50, 8.50, 3.00, 0.09, 9.50, 7.50 };

        for (int i = 0; i < notas.length; i++) {
            Aluno aluno = new Aluno(nomes[i], idades[i], notas[i]);
            alunos.add(aluno);
        }

        System.out.println(alunos);
        Collections.sort(alunos);
        System.out.println(alunos);

        ComparadorPorNome cpn = new ComparadorPorNome();
        alunos.sort(cpn);
        System.out.println(alunos);

        ComparadorPorIdade cpi = new ComparadorPorIdade();
        alunos.sort(cpi);
        System.out.println(alunos);
    }
}
