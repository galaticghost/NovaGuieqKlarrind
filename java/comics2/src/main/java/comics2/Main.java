package comics2;

import java.sql.ResultSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        try {
            QuadrinhoDao quadrinhoDao = new QuadrinhoDao("jdbc:sqlite:java/comics2/quadrinhos.db");
            QuadrinhoFileDao quadrinhoFileDao = new QuadrinhoFileDao();
            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.println("1 - Inserir valores de teste");
                System.out.println("2 - Inserir quadrinho");
                System.out.println("3 - Listar quadrinhos");
                System.out.println("4 - Listar quadrinhos por título");
                System.out.println("5 - Atualizar quadrinhos");
                System.out.println("6 - Deletar quadrinhos");
                System.out.println("7 - Gravar quadrinhos do CSV");
                System.out.println("8 - Deletar tudo");
                System.out.println("9 -  Sair");

                int choice = scanner.nextInt();
                scanner.nextLine();

                switch (choice) {
                    case 1: {
                        Quadrinho quadrinho1 = new Quadrinho("Hellboy - Caçada Selvagem",
                                "Mike Mignola", "Duncan Fegredo", "Dark Horse");

                        Quadrinho quadrinho2 = new Quadrinho("O Anel do Nibelungo", "P.Craig Rusell", "P.Craig Rusell",
                                "Dark Horse");

                        Quadrinho quadrinho3 = new Quadrinho("Demolidor - A Queda de Murdock",
                                "Frank Miller", "David Mazzucchelli", "Marvel");

                        quadrinhoDao.inserir(quadrinho1);
                        quadrinhoDao.inserir(quadrinho2);
                        quadrinhoDao.inserir(quadrinho3);
                        break;
                    }

                    case 2: {
                        System.out.println("Digite o título: ");
                        String titulo = scanner.nextLine();

                        System.out.println("Digite o autor: ");
                        String autor = scanner.nextLine();

                        System.out.println("Digite o artista: ");
                        String artista = scanner.nextLine();

                        System.out.println("Digite a editora: ");
                        String editora = scanner.nextLine();

                        Quadrinho quadrinho = new Quadrinho(titulo, autor, artista, editora);

                        quadrinhoDao.inserir(quadrinho);

                        break;
                    }

                    case 3: {
                        ResultSet resultSet = quadrinhoDao.consultar();
                        while (resultSet.next()) {
                            Quadrinho quadrinho = new Quadrinho(
                                    resultSet.getString("titulo"),
                                    resultSet.getString("autor"),
                                    resultSet.getString("artista"),
                                    resultSet.getString("editora"),
                                    resultSet.getInt("id"));
                            System.out.println(quadrinho);
                        }
                        break;
                    }

                    case 4: {
                        System.out.println("Digite o titulo: ");
                        String titulo = scanner.nextLine();
                        System.out.println(titulo);
                        ResultSet resultSet = quadrinhoDao.consultarPorTitulo(titulo);
                        while (resultSet.next()) {
                            Quadrinho cliente = new Quadrinho(resultSet.getString("titulo"),
                                    resultSet.getString("autor"),
                                    resultSet.getString("artista"),
                                    resultSet.getString("editora"),
                                    resultSet.getInt("id"));
                            System.out.println(cliente);
                        }
                        break;
                    }

                    case 5: {
                        System.out.println("Digite o id: ");
                        int id = scanner.nextInt();

                        scanner.nextLine();
                        System.out.println("Digite o título: ");
                        String titulo = scanner.nextLine();

                        System.out.println("Digite o autor: ");
                        String autor = scanner.nextLine();

                        System.out.println("Digite o artista: ");
                        String artista = scanner.nextLine();

                        System.out.println("Digite a editora: ");
                        String editora = scanner.nextLine();

                        Quadrinho quadrinho = new Quadrinho(titulo, autor, artista, editora, id);

                        quadrinhoDao.atualizar(quadrinho);
                    }
                    case 6: {
                        System.out.println("Digite o id: ");
                        int id = scanner.nextInt();
                        quadrinhoDao.deletarPorId(id);
                        break;
                    }

                    case 7: {
                        quadrinhoFileDao.gravarQuadrinhos();
                        break;
                    }

                    case 8: {
                        quadrinhoDao.deletarTudo();
                        break;
                    }

                    case 9: {
                        scanner.close();
                        System.exit(0);
                    }
                }
            }
        } catch (Exception e) {
            System.err.println(e.getMessage());
            System.exit(0);
        }
    }
}
