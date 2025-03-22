public class Concatena {
    public Concatena() {
        long startTime = System.nanoTime();

        String result = "";

        for(int i = 0; i < 100; i++) {
            result += "a";
        }   

        long endTime = System.nanoTime();
        long duration = endTime - startTime;

        System.out.println("Concatenação Básica: Tempo de execução: " + duration + " nanosegundos");
        System.out.println(result);
    }

    public void rodar(int quantidade) {
        long startTime = System.nanoTime();

        String result = "";

        for(int i = 0; i < quantidade; i++) {
            result += "a";
        }   
        long endTime = System.nanoTime();
        long duration = endTime - startTime;

        System.out.println("Concatenação Básica: Tempo de execução: " + duration + " nanosegundos");
    }
            
}
