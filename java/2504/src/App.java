import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;

public class App {
    public static void main(String[] args) throws Exception {
        // Arthur Von Rohr Monteiro
        // Gera o arquivo disciplinas3 e escreve Paradigmas de ...
        FileWriter fw = new FileWriter("disciplinas3.txt");
        fw.write("Paradigmas de Linguagens de Programação");
        // Adiciona os nomes das outras disciplinas do semestre
        fw.write("\nDesafio de Comunicação");
        fw.write("\nOtimização de Banco de Dados");
        fw.write("\nProjeto, Design e Engenharia de Processos");
        fw.close();

        // Ler uma linha
        FileReader fr = new FileReader("disciplinas3.txt");
        BufferedReader buffer = new BufferedReader(fr);
        System.out.println(buffer.readLine());
        buffer.close();

        // Le todas as linhas
        FileReader fr2 = new FileReader("disciplinas3.txt");
        BufferedReader buffer2 = new BufferedReader(fr2);
        String line = buffer2.readLine();
        while (line != null) {
            System.out.println(line);
            line = buffer2.readLine();
        }
        buffer2.close();

        // Le só a segunda linha
        FileReader fr3 = new FileReader("disciplinas3.txt");
        BufferedReader buffer3 = new BufferedReader(fr3);
        buffer3.readLine();
        System.out.println(buffer3.readLine());
        buffer3.close();

        // Cria o arquivo disciplinas1 e escreve as disciplinas
        FileWriter fileWriter2 = new FileWriter("disciplinas1.txt", true);
        fileWriter2.write("Desafio da Profissão");
        fileWriter2.write("\nPensamento Computacional");
        fileWriter2.write("\nInteligência Artificial e Análise de Dados");
        // Adiciona do 5 até o 20 no arquivo
        for (int i = 5; i < 21; i++) {
            fileWriter2.write("\n" + i);
        }

        fileWriter2.close();

        // Cria um arquivo e escreve 50 numeros pares
        FileWriter fw3 = new FileWriter("numerosPares.txt");
        for (int i = 0; i < 50; i++) {
            fw3.write("\n" + i);
            i++;
        }
        fw3.close();

        // Lê só as linhas impares
        FileReader fr4 = new FileReader("numerosPares.txt");
        BufferedReader br4 = new BufferedReader(fr4);
        String line2 = br4.readLine();
        while (line2 != null) {
            System.out.println(line2);
            br4.readLine();
            line2 = br4.readLine();
        }
        br4.close();

        // Lê a penultima linha
        FileReader fr5 = new FileReader("numerosPares.txt");
        BufferedReader br5 = new BufferedReader(fr5);
        String line4 = br5.readLine();
        String line5 = line4;
        String line3 = line5;
        while (true) {
            line4 = br5.readLine();
            if (line4 == null) {
                break;
            }
            line3 = line5;
            line5 = line4;
        }
        System.out.println(line3);
        br5.close();
    }
}
