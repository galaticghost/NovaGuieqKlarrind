public class Username {
    public Username(String email){
        String username = email.split("@")[0];
        System.err.println(username);
    }
}
