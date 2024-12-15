DELETE FROM venda;
ALTER TABLE venda ADD COLUMN data DATE NOT NULL;


-- Chatgpt
INSERT INTO venda (pk_cliente, pk_produto, quantidade, valor_total, data) VALUES
(1, 3, 2, 120.00, '2024-10-28'),
(1, 7, 1, 45.00, '2024-10-29'),
(1, 11, 3, 180.00, '2024-10-30'),
(2, 4, 5, 250.00, '2024-10-27'),
(2, 6, 2, 120.00, '2024-10-26'),
(2, 9, 4, 160.00, '2024-10-25'),
(3, 1, 3, 150.00, '2024-10-24'),
(3, 5, 2, 100.00, '2024-10-23'),
(3, 10, 1, 50.00, '2024-10-22'),
(4, 8, 6, 360.00, '2024-10-21'),
(4, 12, 1, 60.00, '2024-10-20'),
(4, 14, 3, 210.00, '2024-10-19'),
(5, 2, 4, 180.00, '2024-10-18'),
(5, 13, 2, 140.00, '2024-10-17'),
(5, 15, 5, 250.00, '2024-10-16');

-- Eu
UPDATE produto SET preco = ((preco * 0.10) + preco) WHERE pk_produto < 6;
INSERT INTO venda(pk_cliente,pk_produto,quantidade,valor_total,data) VALUES (1,1,2,110,'2024-11-07');
INSERT INTO venda(pk_cliente,pk_produto,quantidade,valor_total,data) VALUES (1,1,3,165,'2024-11-07');