package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ClienteDao {
    private Connection conn;

    public ClienteDao() throws SQLException{
        try {
            Class.forName("org.postgresql.Driver");
            String url = "jdbc:postgresql://localhost:5432/postgres";
            String user = "admin";
            String password = "postgres";
            conn = DriverManager.getConnection(url,user,password);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void criarTabelaCliente() throws SQLException{
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
}
