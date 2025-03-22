public class App {
    public static void main(String[] args) throws Exception {
        Append append = new Append();
        Concatena conc = new Concatena();

        rodar(append, conc, 500);
    }
    public static void rodar(Append append, Concatena conc, int qtd){
        System.out.println("---- Rodando com " + qtd + " ----");
        conc.rodar(qtd);
        append.rodar(qtd);
    }
}
