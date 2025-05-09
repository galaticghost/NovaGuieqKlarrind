package com.example;

import java.sql.ResultSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try {
            ClienteDao clienteDao = new ClienteDao();
            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.println("1 - Criar tabela cliente");
                System.out.println("2 - Inserir cliente");
                System.out.println("3 - Listar clientes");
                System.out.println("4 - Listar cliente por nome");
                System.out.println("5 - Deletar cliente por id");
                System.out.println("6 - Deletar todos os clientes");
                System.out.println("7 - Deletar tabela cliente");
                System.out.println("8 - Inserir 2 clientes de teste");
                System.out.println("9 - Sair");
                int choice = scanner.nextInt();
                scanner.nextLine();

                switch (choice) {
                    case 1: {
                        clienteDao.criarTabelaCliente();
                        break;
                    }

                    case 2: {
                        System.out.println("Digite o nome: ");
                        String nome = scanner.nextLine();

                        System.out.println("Digite a idade: ");
                        int idade = scanner.nextInt();

                        System.out.println("Digite o salário: ");
                        Double salario = scanner.nextDouble();

                        Cliente cliente = new Cliente(nome, idade, salario);
                        clienteDao.inserirCliente(cliente);
                        break;
                    }

                    case 3: {
                        ResultSet resultSet = clienteDao.consultarTodosClientes();
                        while (resultSet.next()) {
                            Cliente cliente = new Cliente(resultSet.getString("nome"),
                                    resultSet.getInt("idade"),
                                    resultSet.getDouble("salario"),
                                    resultSet.getInt("id"));
                            System.out.println(cliente);
                        }
                        break;
                    }

                    case 4: {
                        System.out.println("Digite o nome: ");
                        String nome = scanner.nextLine();
                        ResultSet resultSet = clienteDao.consultarClienteNome(nome);
                        resultSet.next();
                        Cliente cliente = new Cliente(resultSet.getString("nome"),
                                resultSet.getInt("idade"),
                                resultSet.getDouble("salario"),
                                resultSet.getInt("id"));
                        System.out.println(cliente);
                        break;
                    }

                    case 5: {
                        System.out.println("Digite o id: ");
                        int id = scanner.nextInt();
                        clienteDao.deletarClientePorId(id);
                        break;
                    }
                    case 6:
                        clienteDao.deletarTodosClientes();
                        System.out.println("Deletado");
                        break;
                    case 7: {
                        clienteDao.deletarTabelaCliente();
                        System.out.println("Tabela deletada");
                        break;
                    }
                    case 8: {
                        Cliente cliente1 = new Cliente("Carlos Eduardo", 19, 0.0);
                        Cliente cliente2 = new Cliente("Theo 'Bola' Cunha", 18, 1500.0);

                        clienteDao.inserirCliente(cliente1);
                        clienteDao.inserirCliente(cliente2);

                        break;
                    }
                    case 9:
                        scanner.close();
                        System.exit(0);
                        break;
                }
            }
        } catch (Exception e) {
            System.err.println(e.getMessage());
            System.exit(0);
        }

    }
}