public class PetRepeate {
    public PetRepeate(int numero) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numero; i++) {
            sb.append("java");
        }
        System.out.println(sb.toString());
    }
}
