abstract public class Veiculo {
    private String modelo;
    private String cor;
    private String ano;

    public Veiculo(String modelo, String cor, String ano) {
        this.modelo = modelo;
        this.cor = cor;
        this.ano = ano;
        System.out.println("Modelo: " + this.modelo);
    }

    public void buzinar() {
        System.out.println("[Não sou criativo para fazer um barulho de buzina]");
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getAno() {
        return ano;
    }

    public void setAno(String ano) {
        this.ano = ano;
    }
}
