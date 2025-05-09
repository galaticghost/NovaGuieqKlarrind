package comics2;

public class Quadrinho {
    private int id;
    private String titulo;
    private String autor;
    private String artista;
    private String editora;

    public Quadrinho (String titulo,String autor,String artista, String editora){
        this.titulo = titulo;
        this.autor = autor;
        this.artista = artista;
        this.editora = editora;
    }

    public Quadrinho (String titulo,String autor,String artista, String editora,int id){
        this(titulo, autor, artista, editora);
        this.id = id;
    }

    @Override
    public String toString(){
        if (id == 0) {
            return String.format("Titulo: %s, Autor: %s, Artista: %s, Editora: %s",
            this.titulo,this.autor,this.artista,this.editora);
        } else {
            return String.format("Id: %d, Titulo: %s, Autor: %s, Artista: %s, Editora: %s",
            this.id,this.titulo,this.autor,this.artista,this.editora);
        }
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public String getArtista() {
        return artista;
    }

    public void setArtista(String artista) {
        this.artista = artista;
    }

    public String getEditora() {
        return editora;
    }

    public void setEditora(String editora) {
        this.editora = editora;
    }
}

