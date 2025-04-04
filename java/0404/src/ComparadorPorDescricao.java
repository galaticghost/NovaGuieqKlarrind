import java.util.Comparator;

public class ComparadorPorDescricao implements Comparator<Produto> {
    @Override
    public int compare(Produto p1, Produto p2){
        return p1.getDescricao().compareTo(p2.getDescricao());
    }
}
