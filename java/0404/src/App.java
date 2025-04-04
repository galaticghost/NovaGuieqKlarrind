import java.util.ArrayList;
import java.util.Collections;

public class App {
    public static void main(String[] args) throws Exception {
        /*
        ArrayList<Produto> ps;
        Produto p1 = new Produto(5000.40, "TV");
        Produto p2 = new Produto(3000.00, "Bluray");
        Produto p3 = new Produto(2000.12, "Carro fiat Honda");

        ps = new ArrayList<>();
        ps.add(p1);
        ps.add(p3);
        ps.add(p2);

        System.out.println(ps);
        Collections.sort(ps);
        System.out.println(ps);

        ComparadorPorDescricao cpd;
        cpd = new ComparadorPorDescricao();
        ps.sort(cpd);
        System.out.println(ps);*/
    
        ArrayList<Aluno> alunos = new ArrayList<>(); // TODO GERADOR COM FOR e ARRAYS
        Aluno a1 = new Aluno("CARLOS EDUARDO", 50, 2.00);
        Aluno a2 = new Aluno("Joao Lauro", 20, 8.00);
        Aluno a3 = new Aluno("Junior Moraes de Freitas", 24, 11.50);
        Aluno a4 = new Aluno("Theo 'Bola' Cunha", 18, 6.50);
        Aluno a5 = new Aluno("JEduardo", 20, 6.00);
        Aluno a6 = new Aluno("Henrique", 20, 7.50);
        Aluno a7 = new Aluno("Leonardo 'Dominik' Machado", 20, 8.50);
        Aluno a8 = new Aluno("Predo Preus", 19, 3.00);
        Aluno a9 = new Aluno("PH", 20, 0.09);
        Aluno a10 = new Aluno("Xi Jiping", 52, 9.50);

        alunos.add(a3);
        alunos.add(a1);
        alunos.add(a2);
        alunos.add(a10);
        alunos.add(a9);
        alunos.add(a7);
        alunos.add(a5);
        alunos.add(a4);
        alunos.add(a8);
        alunos.add(a6);

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
