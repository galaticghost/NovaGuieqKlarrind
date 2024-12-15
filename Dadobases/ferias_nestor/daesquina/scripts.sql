INSERT INTO cliente(nome_cliente, telefone, vegetariano) VALUES 
('Ana Silva', '1234-5678', TRUE),
('João Souza', '2345-6789', FALSE),
('Maria Oliveira', '3456-7890', TRUE),
('Pedro Santos', '4567-8901', FALSE),
('Lucas Lima', '5678-9012', TRUE),
('Julia Costa', '6789-0123', FALSE),
('Mariana Ferreira', '7890-1234', TRUE),
('Thiago Almeida', '8901-2345', FALSE),
('Fernanda Rocha', '9012-3456', TRUE),
('Rafael Mendes', '0123-4567', FALSE),
('Tatiane Pires', '1234-5678', TRUE),
('Carlos Santos', '2345-6789', FALSE),
('Gabriela Martins', '3456-7890', TRUE),
('Eduardo Pereira', '4567-8901', FALSE),
('Isabela Almeida', '5678-9012', TRUE);

INSERT INTO produto(nome_produto, quantidade, vencimento) VALUES 
('Arroz', 50, '2024-11-01'),
('Feijão', 30, '2025-03-15'),
('Macarrão', 100, '2024-10-30'),
('Açúcar', 20, '2025-01-10'),
('Sal', 15, '2024-12-20'),
('Óleo de Soja', 40, '2025-05-05'),
('Milho', 25, '2024-11-15'),
('Lentejas', 10, '2025-02-25'),
('Café', 60, '2024-08-22'),
('Chá', 45, '2025-04-12'),
('Biscoito', 80, '2024-09-10'),
('Molho de Tomate', 35, '2025-06-30'),
('Queijo', 20, '2024-12-01'),
('Salsicha', 12, '2025-03-30'),
('Iogurte', 25, '2024-07-18');

INSERT INTO fornecedor(nome_fornecedor, cpf_cnpj) VALUES 
('Fornecedor A', '123.456.789-09'),
('Fornecedor B', '12.345.678/0001-90'),
('Fornecedor C', '987.654.321-00'),
('Fornecedor D', '98.765.432/0001-01'),
('Fornecedor E', '123.123.123-12'),
('Fornecedor F', '45.678.901/0001-23'),
('Fornecedor G', '321.321.321-34'),
('Fornecedor H', '23.456.789/0001-45'),
('Fornecedor I', '654.987.321-56'),
('Fornecedor J', '11.111.111/0001-11'),
('Fornecedor K', '222.333.444-77'),
('Fornecedor L', '33.444.555/0001-22'),
('Fornecedor M', '555.666.777-88'),
('Fornecedor N', '44.555.666/0001-33'),
('Fornecedor O', '777.888.999-99');

INSERT INTO lanche(nome_lanche, preco) VALUES 
('Hambúrguer', 15.00),
('Sanduíche Natural', 12.50),
('Wrap de Frango', 18.00),
('Hot Dog', 10.00),
('Taco', 14.00),
('Salada de Frutas', 8.50),
('Panini', 13.00),
('Pastel', 7.00),
('Croissant', 5.50),
('Biscoito de Polvilho', 4.00),
('Pão de Queijo', 6.00),
('Sushi', 20.00),
('Coxinha', 9.00),
('Bolo de Cenoura', 5.00),
('Pão com Linguiça', 11.00);

INSERT INTO produto_lanche(pk_produto, pk_lanche) VALUES 
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 4),
(3, 5),
(4, 6),
(5, 2),
(6, 3),
(7, 1),
(7, 4),
(8, 5),
(9, 6),
(10, 2),
(11, 3);

INSERT INTO produto_fornecedor(pk_produto, pk_fornecedor) VALUES 
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 4),
(4, 1),
(4, 5),
(5, 2),
(6, 3),
(7, 4),
(8, 1),
(9, 5),
(10, 2),
(11, 3);

INSERT INTO passo(pk_lanche, numero_passo, passo) VALUES 
(1, 1, 'Preparar todos os ingredientes.'),
(1, 2, 'Cozinhar a carne até ficar bem passada.'),
(1, 3, 'Montar o hambúrguer com alface e tomate.'),
(2, 1, 'Picar os vegetais para o sanduíche.'),
(2, 2, 'Espalhar a maionese no pão.'),
(2, 3, 'Adicionar os vegetais e fechar o sanduíche.'),
(3, 1, 'Cozinhar o frango e desfiar.'),
(3, 2, 'Misturar o frango com molho.'),
(3, 3, 'Envolver o frango em uma tortilha.'),
(4, 1, 'Cozinhar a salsicha.'),
(4, 2, 'Colocar a salsicha no pão.'),
(4, 3, 'Adicionar ketchup e mostarda.'),
(5, 1, 'Preparar a massa do taco.'),
(5, 2, 'Rechear com carne e legumes.'),
(5, 3, 'Dobrar o taco e servir.'),
(6, 1, 'Lavar as frutas.'),
(6, 2, 'Cortar as frutas em pedaços.'),
(6, 3, 'Servir em uma tigela.');

SELECT * FROM cliente;
SELECT * FROM passo;
SELECT * FROM lanche;
SELECT * FROM produto_lanche;
SELECT * FROM produto;
SELECT * FROM fornecedor;
SELECT * FROM produto_fornecedor;