public class UrlGenerator {
    public UrlGenerator(String url, String pagina, String[] args) {
        StringBuilder sb = new StringBuilder();
        sb.append(url).append(pagina);
        for (String id : args) {
            sb.append(id);
        }
        System.out.println(sb.toString());
    }
}
