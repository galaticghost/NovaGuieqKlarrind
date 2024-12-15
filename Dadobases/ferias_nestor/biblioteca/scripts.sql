INSERT INTO autor(nome_autor) VALUES 
('J.K. Rowling'),
('George R.R. Martin'),
('Agatha Christie'),
('Stephen King'),
('J.R.R. Tolkien'),
('Mark Twain'),
('Ernest Hemingway'),
('Jane Austen'),
('F. Scott Fitzgerald'),
('Gabriel García Márquez'),
('Isaac Asimov'),
('Virginia Woolf'),
('Haruki Murakami'),
('Maya Angelou'),
('Ray Bradbury');

INSERT INTO livro(isbn, nome_livro, genero, status) VALUES 
('978-3-16-148410-0', 'Harry Potter e a Pedra Filosofal', 'Fantasia', TRUE),
('978-0-7432-7356-5', 'A Guerra dos Tronos', 'Fantasia', TRUE),
('978-0-452-28423-4', 'O Sol é Para Todos', 'Ficção', FALSE),
('978-0-06-112008-4', 'Matar a Saudade', 'Ficção', TRUE),
('978-0-06-235059-6', '1984', 'Distopia', TRUE),
('978-1-86197-876-9', 'Orgulho e Preconceito', 'Romance', FALSE),
('978-0-553-21311-7', 'Cem Anos de Solidão', 'Ficção', TRUE),
('978-0-06-195929-0', 'O Hobbit', 'Fantasia', TRUE),
('978-0-06-229049-5', 'O Lobo da Estepe', 'Ficção', FALSE),
('978-0-452-28425-8', 'O Morro dos Ventos Uivantes', 'Romance', TRUE),
('978-0-7432-7357-2', 'O Senhor dos Anéis', 'Fantasia', TRUE),
('978-0-553-21310-0', 'Fahrenheit 451', 'Distopia', FALSE),
('978-0-14-303943-3', 'A Menina que Roubava Livros', 'Ficção', TRUE),
('978-0-06-093846-1', 'O Grande Gatsby', 'Ficção', TRUE),
('978-0-452-28424-1', 'As Aventuras de Tom Sawyer', 'Infantil', TRUE);

INSERT INTO autor_livro(pk_autor, pk_livro) VALUES 
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 6),
(4, 7),
(4, 8),
(5, 9),
(5, 10),
(6, 11),
(6, 12),
(7, 13),
(7, 14),
(8, 15);

INSERT INTO usuario(nome_usuario, data_nascimento) VALUES 
('Ana Clara', '1990-05-12'),
('João Pedro', '1988-08-25'),
('Maria Fernanda', '1992-03-15'),
('Carlos Eduardo', '1995-11-30'),
('Juliana Alves', '1993-07-19'),
('Lucas Oliveira', '1991-01-04'),
('Tatiane Santos', '1987-06-22'),
('Rafael Gomes', '1994-09-10'),
('Fernanda Lima', '1990-12-05'),
('Pedro Henrique', '1989-02-14'),
('Isabela Ferreira', '1996-04-30'),
('Eduardo Costa', '1985-10-18'),
('Gabriela Martins', '1992-07-25'),
('Thiago Almeida', '1993-08-09'),
('Mariana Rocha', '1991-05-21');

INSERT INTO emprestimo(pk_usuario, pk_livro, data_emprestimo, data_vencimento) VALUES 
(1, 1, '2024-01-10', '2024-01-24'),
(2, 2, '2024-01-12', '2024-01-26'),
(3, 3, '2024-01-15', '2024-01-29'),
(4, 4, '2024-01-17', '2024-01-31'),
(5, 5, '2024-01-20', '2024-02-03'),
(6, 6, '2024-01-22', '2024-02-05'),
(7, 7, '2024-01-25', '2024-02-08'),
(8, 8, '2024-01-27', '2024-02-10'),
(9, 9, '2024-01-30', '2024-02-12'),
(10, 10, '2024-02-01', '2024-02-15'),
(11, 11, '2024-02-03', '2024-02-18'),
(12, 12, '2024-02-05', '2024-02-20'),
(13, 13, '2024-02-07', '2024-02-22'),
(14, 14, '2024-02-10', '2024-02-25'),
(15, 15, '2024-02-12', '2024-02-27');

INSERT INTO interesse(interesse) VALUES 
('Ficção'),
('Fantasia'),
('Romance'),
('Mistério'),
('Thriller'),
('Ciência Ficção'),
('Não-ficção'),
('Biografia'),
('Autoajuda'),
('História'),
('Poesia'),
('Drama'),
('Infantil'),
('Literatura Clássica'),
('Graphic Novel');

INSERT INTO usuario_interesse(pk_usuario, pk_interesse) VALUES 
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 6),
(4, 1),
(4, 7),
(5, 2),
(5, 8),
(6, 3),
(6, 9),
(7, 4),
(7, 10),
(8, 5);

SELECT * FROM autor;
SELECT * FROM livro;
SELECT * FROM autor_livro;
SELECT * FROM usuario;
SELECT * FROM emprestimo;
SELECT * FROM interesse;
SELECT * FROM usuario_interesse;