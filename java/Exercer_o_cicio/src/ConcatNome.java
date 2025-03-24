public class ConcatNome {
    private String nome;
    private String sobrenome;
    private String sufixo;

    public ConcatNome(String nome, String sobrenome, String sufixo) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.sufixo = sufixo;

        System.out.println("Nome completo: " + this.nome + " " + this.sobrenome + " " + this.sufixo);
    }

    public ConcatNome(String nome, String sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;

        System.out.println("Nome completo: " + this.nome + " " + this.sobrenome);
    }
}
