DELETE FROM telefone;

-- chatgpt
INSERT INTO telefone(pk_cliente, telefone) VALUES
(1, '1234-5678'),
(1, '9876-5432'),
(2, '2345-6789'),
(2, '8765-4321'),
(3, '3456-7890'),
(3, '7654-3210'),
(4, '4567-8901'),
(4, '6543-2109'),
(5, '5678-9012'),
(5, '5432-1098');


--eu
ALTER TABLE produto ADD COLUMN categoria VARCHAR(100);
-- eu e gpt
INSERT INTO produto(sku, nome, descricao, preco, quantidade, categoria) VALUES
('SKU016', 'Produto sdg', 'Descrição dfdso Produto A', 25.99, 100, 'Eletrônicos'),
('SKU017', 'Produto dsg', 'Descrição dodsf Produto B', 15.50, 150, 'Roupas'),
('SKU018', 'Produto dsgchfsdds', 'Desfdsfdfdscrição do Produto C', 39.90, 80, 'Alimentos'),
('SKU019', 'Produto FDSDG', 'Descrição do Pdfroduto D', 99.99, 50, 'Móveis'),
('SKU020', 'Produto GDSDGSV', 'Descdffdsrição do Produto E', 12.75, 200, 'Roupas'),
('SKU021', 'Produto DTEWY', 'Descfdfdrição dsfdfsdo Produto F', 199.99, 30, 'Eletrônicos'),
('SKU022', 'Produto YWSYW', 'Descriçãosdf do Produto G', 8.99, 500, 'Alimentos'),
('SKU023', 'Produto dshshhshsf', 'Descriçãdfsfdso fdsdo Produto H', 29.99, 60, 'Móveis'),
('SKU024', 'Produto sagh', 'Descrição do Profsdfduto I', 49.99, 40, 'Eletrônicos'),
('SKU025', 'Produto Jdsh', 'Descrição do Prodfduto J', 10.00, 300, 'Uma pedra'),
('SKU026', 'Produto eqtetK', 'Descrição dodsffsd Produto K', 5.99, 450, 'Alimentos'),
('SKU027', 'Produto ewtgsfL', 'Descrição do Produto L', 75.00, 20, 'Móveis'),
('SKU028', 'Produto dsgM', 'Descrição dodsf Produto M', 150.00, 25, 'Uma Pedra'),
('SKU029', 'Produto sdN', 'Descrição doffds ProfddsfN', 20.50, 180, 'Roupas'),
('SKU030', 'Produto Od', 'Descriçãfdssfdo do Produto O', 60.00, 70, 'Móveis');

UPDATE produto SET categoria = 'Uma pedra' WHERE pk_produto < 16;

DELETE FROM pedido_produto;
DELETE FROM pedido;
-- Eu e gpt
INSERT INTO pedido(pk_cliente, pk_funcionario, pk_inspetor, verificado, data, status) VALUES
(1, 1, 1, TRUE, '2024-11-01', 'PEDIDO FEITO'),
(1, 1, 1, TRUE, '2024-11-02', 'PEDIDO FEITO'),
(2, 2, 2, TRUE, '2024-11-03', 'EM SEPARAÇÃO'),
(2, 2, 2, TRUE, '2024-11-04', 'PEDIDO FEITO'),
(3, 3, 3, TRUE, '2024-11-05', 'PEDIDO FEITO'),
(3, 3, 3, TRUE, '2024-11-06', 'CANCELADO');