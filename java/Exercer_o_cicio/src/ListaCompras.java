public class ListaCompras {
    public ListaCompras(String[] lista) {
        StringBuilder sb = new StringBuilder();
        sb.append("Lista de compras: ");
        int i = 0;
        for (String item : lista) {
            i++;
            if (i == 1) {
                sb.append(item);
            } else {
                sb.append(", " + item);
            }
        }
        System.out.println(sb.toString());
    }
}