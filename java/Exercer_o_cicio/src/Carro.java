public class Carro extends Veiculo {
    public int portas;

    public Carro(String modelo, String cor, String ano, int portas) {
        super(modelo, cor, ano);
        this.portas = portas;
        System.out.println("Portas: " + portas);
    }

    @Override
    public void buzinar() {
        System.out.println("[tutututututtu]");
    }

    public void andar(int velocidade) {
        System.out.println("Velocidade: " + velocidade + "km/h");
    }

    public void andar(int velocidade, int nitro) {
        System.out.println("Velocidade: " + (velocidade + nitro) + "km/h");
    }
}
