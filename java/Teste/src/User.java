public class User {
    private String nome;
    private String sobrenome;
    private int idade;
    private float peso;

    public User(int idade){
        this.idade = idade;
    }

    public User(String n){
        this.nome = n;
    }

    public User(String n, String sobrenome, int idade, float peso){
        this.nome = n;
        this.sobrenome = sobrenome;
        this.idade = idade;
        this.peso = peso;
    }

    @Override
    public String toString(){
        String resultado;
        resultado = this.nome + "  bola";
        return resultado;
    }

    public void print(){
        System.out.println("Nome: " + this.getNome());
        System.out.println("Sobrenome: " + this.getSobrenome());
        System.out.println("Idade: " + this.getIdade());
        System.out.println("Peso: " + this.getPeso());
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void setPeso(float peso) {
        this.peso = peso;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public int getIdade() {
        return idade;
    }

    public float getPeso() {
        return peso;
    }
}