
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        
        User user;
        user = new User("Xina","Men",4,14.4f);
        
        System.out.println(user.toString());
        System.err.println(user.getNome());
        
        Scanner scanner;
        scanner = new Scanner(System.in);
        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();
        System.out.print("Digite seu sobrenome: ");
        String sobrenome = scanner.nextLine();
        System.out.print("Digite sua idade: ");
        int idade = scanner.nextInt();
        System.out.print("Digite seu peso: ");
        float peso = scanner.nextFloat();

        
        User user3 = new User(nome,sobrenome,idade,peso);
        user3.print();
        scanner.close();
    }
}