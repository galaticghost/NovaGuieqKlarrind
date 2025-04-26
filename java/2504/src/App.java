import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;

public class App {
    public static void main(String[] args) throws Exception {
        FileWriter fw = new FileWriter("disciplinas3.txt",true);
        fw.write("Paradigmas de Linguagens de Programação");
        fw.write("\nDesafio de Comunicação");
        fw.write("\nOtimização de Banco de Dados");
        fw.write("\nProjeto, Design e Engenharia de Processos");
        
        FileReader fr = new FileReader("disciplinas3.txt");
        BufferedReader buffer = new BufferedReader(fr);
        System.out.println(buffer.readLine());
        buffer.close();
        fw.close();
    
        FileWriter fileWriter2 = new FileWriter("disciplinas1.txt",true);
        fileWriter2.write("Desafio da Profissão");
        fileWriter2.write("\nPensamento Computacional");
        fileWriter2.write("\nInteligência Artificial e Análise de Dados");
        for (int i = 5; i < 21; i++){
            fileWriter2.write("\n" + i);
        }

        FileReader fr2 = new FileReader("disciplinas1.txt");
        BufferedReader buffer2 = new BufferedReader(fr2);
        for(int i = 0; i < 3; i++){
            System.out.println(buffer2.readLine());
        }
        buffer2.close();

        fileWriter2.close();
    
    }
}
