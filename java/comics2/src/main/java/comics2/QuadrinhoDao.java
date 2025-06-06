package comics2;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class QuadrinhoDao {
    private Connection conn;

    public QuadrinhoDao(String url) {
        try {
            this.conn = DriverManager.getConnection(url);
            this.criarTabela();
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }

    public void criarTabela() throws SQLException {
        try {
            String sql = "CREATE TABLE IF NOT EXISTS quadrinhos (" +
                    "id INTEGER PRIMARY KEY," +
                    "titulo TEXT NOT NULL," +
                    "autor TEXT NOT NULL," +
                    "artista TEXT NOT NULL," +
                    "editora TEXT NOT NULL);";
            this.conn.createStatement().executeUpdate(sql);
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }

    public void inserir(Quadrinho quadrinho) throws SQLException {
        try {
            String sql = "INSERT INTO quadrinhos(titulo,autor,artista,editora) " +
                    "VALUES (?,?,?,?);";
            PreparedStatement stmt = this.conn.prepareStatement(sql);
            stmt.setString(1, quadrinho.getTitulo());
            stmt.setString(2, quadrinho.getAutor());
            stmt.setString(3, quadrinho.getArtista());
            stmt.setString(4, quadrinho.getEditora());
            stmt.executeUpdate();
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }

    public ResultSet consultar() throws SQLException {
        try {
            String sql = "SELECT * FROM quadrinhos;";
            ResultSet resultSet = this.conn.createStatement().executeQuery(sql);
            return resultSet;
        } catch (Exception e) {
            System.err.println(e.getMessage());
            throw e;
        }
    }

    public ResultSet consultarPorTitulo(String titulo) throws SQLException {
        try {
            String sql = "SELECT * FROM quadrinhos WHERE titulo = ? OR titulo LIKE ?;";
            PreparedStatement stmt = this.conn.prepareStatement(sql);
            stmt.setString(1, titulo);
            stmt.setString(2, "%" + titulo + "%");
            ResultSet resultSet = stmt.executeQuery();
            return resultSet;
        } catch (Exception e) {
            System.err.println(e.getMessage());
            throw e;
        }
    }

    public void atualizar(Quadrinho quadrinho) throws SQLException {
        try {
            String sql = "UPDATE quadrinhos SET titulo = ?," +
                    "autor = ?, artista = ?, editora = ? WHERE id = ?";
            PreparedStatement stmt = this.conn.prepareStatement(sql);
            stmt.setString(1, quadrinho.getTitulo());
            stmt.setString(2, quadrinho.getAutor());
            stmt.setString(3, quadrinho.getArtista());
            stmt.setString(4, quadrinho.getEditora());
            stmt.setInt(5, quadrinho.getId());
            stmt.executeUpdate();
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }

    public void deletarPorId(int id) throws SQLException {
        try {
            String sql = "DELETE FROM quadrinhos WHERE id = ?";
            PreparedStatement stmt = this.conn.prepareStatement(sql);
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void deletarTudo() throws SQLException {
        try {
            String sql = "DELETE FROM quadrinhos";
            this.conn.createStatement().executeUpdate(sql);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
