import java.util.Comparator;

public class ComparadorPorIdade implements Comparator<Aluno> {
    @Override
    public int compare(Aluno a1, Aluno a2){
        return a1.getIdade().compareTo(a2.getIdade());
    }
}
