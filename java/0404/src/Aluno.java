
public class Aluno implements Comparable<Aluno>{
    private String nome;
    private Integer idade;
    private Double notaFinal;

    public Aluno(String nome, Integer idade, Double notaFinal){
        this.nome = nome;
        this.idade = idade;
        this.notaFinal = notaFinal;
    }

    @Override
    public int compareTo(Aluno aluno){
        int r = 0;
        r = Double.compare(this.notaFinal,aluno.notaFinal);
        return r;
    }

    @Override
    public String toString(){
        return String.format("\nNome: %s, idade: %d, nota final: %.2f",this.nome,this.idade,this.notaFinal);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Integer getIdade() {
        return idade;
    }

    public void setIdade(Integer idade) {
        this.idade = idade;
    }

    public Double getNotaFinal() {
        return notaFinal;
    }

    public void setNotaFinal(Double notaFinal) {
        this.notaFinal = notaFinal;
    }

    
}
