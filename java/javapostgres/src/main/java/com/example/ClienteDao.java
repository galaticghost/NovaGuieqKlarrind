package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ClienteDao {
    private Connection conn;

    public ClienteDao() throws SQLException {
        try {
            Class.forName("org.postgresql.Driver");
            String url = "jdbc:postgresql://localhost:5432/postgres";
            String user = "admin"; // Ver se o usuario existe e afins
            String password = "postgres"; // Senha tbm
            conn = DriverManager.getConnection(url, user, password);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void criarTabelaCliente() throws SQLException {
        try {
            String sql = "CREATE TABLE IF NOT EXISTS cliente (" +
                    "id INTEGER GENERATED ALWAYS AS IDENTITY," +
                    "nome VARCHAR(100) NOT NULL," +
                    "salario REAL NOT NULL," +
                    "idade INTEGER NOT NULL);";
            this.conn.createStatement().executeUpdate(sql);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void inserirCliente(Cliente cliente) throws SQLException {
        try {
            String sql = "INSERT INTO cliente(nome,salario,idade)" +
                    "values (?,?,?)";
            PreparedStatement stmt = this.conn.prepareStatement(sql);
            stmt.setString(1, cliente.getNome());
            stmt.setDouble(2, cliente.getSalario());
            stmt.setInt(3, cliente.getIdade());
            stmt.executeUpdate();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public ResultSet consultarTodosClientes() throws SQLException {
        try {
            String sql = "SELECT id,nome,salario,idade FROM cliente";
            Statement stmt = this.conn.createStatement();
            ResultSet resultSet = stmt.executeQuery(sql);
            return resultSet;
        } catch (Exception e) {
            System.out.println(e.getMessage());
            throw e;
        }
    }

    public ResultSet consultarClienteNome(String nome) throws SQLException {
        try {
            String sql = "SELECT id,nome,salario,idade FROM cliente WHERE nome = ?";
            PreparedStatement stmt = this.conn.prepareStatement(sql);
            stmt.setString(1, nome);
            ResultSet resultSet = stmt.executeQuery();
            return resultSet;
        } catch (Exception e) {
            System.out.println(e.getMessage());
            throw e;
        }
    }

    public void deletarClientePorId(int id) throws SQLException {
        try {
            String sql = "DELETE FROM cliente WHERE id = ?";
            PreparedStatement stmt = this.conn.prepareStatement(sql);
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void deletarTodosClientes() throws SQLException {
        try {
            String sql = "TRUNCATE TABLE cliente";
            this.conn.createStatement().executeUpdate(sql);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void deletarTabelaCliente() throws SQLException {
        try {
            String sql = "DROP TABLE cliente";
            this.conn.createStatement().executeUpdate(sql);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
