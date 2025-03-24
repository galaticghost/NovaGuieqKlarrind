public class FraseGenerator {
    public FraseGenerator() {
        StringBuilder string = new StringBuilder();

        for (int i = 1; i <= 20; i++) {
            string.append("Número " + i + " ");
        }
        System.out.println(string);
    }
}
