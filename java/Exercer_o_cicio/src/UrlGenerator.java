public class UrlGenerator {
    public UrlGenerator(String url, String pagina, String[] args) {
        StringBuilder sb = new StringBuilder();
        String urlBase = url + "/" + pagina;
        sb.append(urlBase);
        for (String id : args) {
            sb.append("?id=" + id);
        }
        System.out.println(sb.toString());
    }
}
