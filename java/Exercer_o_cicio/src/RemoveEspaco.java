public class RemoveEspaco {
    public RemoveEspaco(String texto) {
        texto = texto.strip().replaceAll(" +", " ");
        System.out.println(texto);
    }
}
