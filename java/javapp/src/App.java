import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class App {
    static App app = new App();
    public static void main(String[] args) throws Exception {
    
        System.out.println("Bem vindo");
        Scanner teclado = new Scanner(System.in);
        do{
            System.out.println("Escolha uma opção");
            System.out.println("1: Escrever no arquivo");
            System.out.println("2: Anexar no arquivo");
            System.out.println("3: Ler primeira");
            System.out.println("4: Ler todas linhas");
            System.out.println("5: Sair");
            int op = teclado.nextInt();
            teclado.nextLine();
            switch (op) {
                case 1:
                    app.escreve(false,"bola");
                    break;
                case 2:
                    app.escreve(true, "");
                    break;
                case 3:
                    app.lePrimeira();
                    break;
                case 4:
                    app.leTodas();
                    break;
                case 5:
                    System.exit(0);
                default:
                    throw new AssertionError();
            }
        } while (true);
    }
            
    public void escreve(Boolean tipo, String content){
        try {
            FileWriter filew = new FileWriter("arquivo.txt",tipo);
            filew.write(content);
            filew.close(); 
        } catch (IOException e) {
            System.out.println("Erro "+ e.getMessage());
        }
    }

    public void lePrimeira(){
        try {
            FileReader filer = new FileReader("arquivo.txt");
            BufferedReader buffer = new BufferedReader(filer);
            String line = buffer.readLine();
            System.out.println(line);
            buffer.close();
        } catch (IOException e) {
            System.out.println("Erro " + e.getMessage());
        }
    }

    public void leTodas(){
        try {
            FileReader filer = new FileReader("arquivo.txt");
            BufferedReader buffer = new BufferedReader(filer);
            String line = buffer.readLine();
            while (line != null) { 
                System.out.println(line);   
                line = buffer.readLine();
            }
            buffer.close();
        } catch (IOException e) {
            System.out.println("Erro " + e.getMessage());
        }
    }
}
