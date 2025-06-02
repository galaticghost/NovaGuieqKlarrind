import java.util.Scanner;

public class StringGnirts {
    public StringGnirts() {
        Scanner x = new Scanner(System.in);
        System.out.println("Digite algo: ");
        String string = x.nextLine();

        StringBuilder sb = new StringBuilder();

        sb.append(string);

        System.out.println(sb.reverse().toString());
        x.close();
    }
}
