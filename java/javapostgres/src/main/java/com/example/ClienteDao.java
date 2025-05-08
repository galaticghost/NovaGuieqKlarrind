package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class ClienteDao {
    private Connection conn;

    public ClienteDao() throws SQLException {
        try {
            Class.forName("org.postgresql.Driver");
            String url = "jdbc:postgresql://localhost:5432/postgres";
            String user = "admin";
            String password = "postgres";
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
            conn.createStatement().executeUpdate(sql);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void inserirCliente(String nome, Double salario, int idade) throws SQLException {
        try {
            String sql = "INSERT INTO cliente(nome,salario,idade)" +
                    "values (?,?,?)";
            PreparedStatement stmt = this.conn.prepareStatement(sql);
            stmt.setString(1, nome);
            stmt.setDouble(2, salario);
            stmt.setInt(3, idade);
            stmt.executeUpdate();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
