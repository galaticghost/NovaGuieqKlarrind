package com.example;

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
                System.out.println("4 - Listar cliente por id");
                System.out.println("5 - Deletar cliente por id");
                System.out.println("6 - Deletar todos os clientes");
                System.out.println("7 - Deletar tabela cliente");
                System.out.println("8 - Sair");
                int choice = scanner.nextInt();
                scanner.nextLine();

                switch (choice) {
                    case 1:
                        clienteDao.criarTabelaCliente();
                        break;
                    case 2:
                        break;
                    case 3:
                        break;
                    case 4:
                        break;
                    case 5:
                        break;
                    case 6:
                        break;
                    case 7:
                        break;
                    case 8:
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