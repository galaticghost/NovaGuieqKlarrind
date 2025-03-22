public class Append {

    public Append() {
        long startTime = System.nanoTime();

        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < 100; i++) {
            sb.append("a");
        }   

        long endTime = System.nanoTime();
        long duration = endTime - startTime;

        System.out.println("StringBuilder: Tempo de execução: " + duration + " nanosegundos");
        System.out.println(sb);
    }
    
    public void rodar(int quantidade) {
        long startTime = System.nanoTime();

        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < quantidade; i++) {
            sb.append("a");
        }   

        long endTime = System.nanoTime();
        long duration = endTime - startTime;

        System.out.println("StringBuilder: Tempo de execução: " + duration + " nanosegundos");

    }
}
