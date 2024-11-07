SELECT p.categoria, SUM(pp.valor_total) AS 'Valor total' FROM produto p
INNER JOIN pedido_produto pp ON pp.pk_produto = p.pk_produto
GROUP BY categoria
HAVING SUM(pp.valor_total)
ORDER BY SUM(pp.valor_total) DESC LIMIT 3; -- 4

SELECT COUNT(tipo), tipo FROM pedido
GROUP BY tipo
ORDER BY COUNT(tipo) DESC
LIMIT 1; -- 6

SELECT c.endereco AS Endereço, c.endereco_2 AS 'Endereço 2', t.telefone AS Telefone,
(SELECT telefone FROM telefone WHERE pk_cliente = c.pk_cliente LIMIT 1 OFFSET 1) AS 'Telefone 2' FROM cliente c
INNER JOIN telefone t ON c.pk_cliente = t.pk_cliente
GROUP BY c.pk_cliente; -- 7

-- 8