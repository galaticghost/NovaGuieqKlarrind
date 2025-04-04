public class Produto implements Comparable<Produto> {
    private Double preco;
    private String descricao;

    public Produto(Double preco,String descricao){
        this.preco = preco;
        this.descricao = descricao;
    }

    @Override
    public int compareTo(Produto produto){
        int r = 0;
        r = Double.compare(this.preco,produto.preco);
        return r;
    }

    @Override
    public String toString(){
        return this.preco.toString() + " " + this.descricao;
    }

    public Double getPreco() {
        return preco;
    }

    public void setPreco(Double preco) {
        this.preco = preco;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }    
}
