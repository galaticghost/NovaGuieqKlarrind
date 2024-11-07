SELECT COUNT(pk_cliente),SUM(quantidade),SUM(valor_total) FROM venda GROUP BY pk_cliente; -- 1

SELECT nome, quantidade FROM produto GROUP BY nome HAVING quantidade < 6; -- 2, só retorna banana pois é o unico com menos de 5 no estoque

SELECT p.nome,p.quantidade,COUNT(DISTINCT v.pk_cliente) FROM produto p INNER JOIN venda v ON p.pk_produto = v.pk_produto GROUP BY v.pk_produto ORDER BY COUNT(v.pk_produto) DESC LIMIT 4 -- 3

SELECT AVG(valor_total) FROM venda GROUP BY pk_cliente; -- 4
SELECT AVG(valor_total) FROM venda; -- 4.5

SELECT strftime('%w',data), SUM(quantidade) FROM venda
GROUP BY strftime('%w',data); -- 5, ele retorna os dias da semana como 0 a 6 sendo 0 domingo e assim por diante

SELECT SUM(v.quantidade), f.nome FROM fornecedor f
INNER JOIN produto p ON p.pk_fornecedor = f.pk_fornecedor
INNER JOIN venda v ON v.pk_produto = p.pk_produto
GROUP BY f.pk_fornecedor -- 6

SELECT p.nome AS Produto,f.nome AS Fornecedor, c.nome AS Cliente, v.data AS 'Data de venda', SUM(v.quantidade) AS Quantidade FROM venda v 
INNER JOIN produto p ON v.pk_produto = p.pk_produto
INNER JOIN fornecedor f ON p.pk_fornecedor = f.pk_fornecedor
INNER JOIN cliente c ON v.pk_cliente = c.pk_cliente WHERE v.pk_produto = 1; -- 7

SELECT v.quantidade,p.nome,v.data,v.valor_total FROM venda v
INNER JOIN produto p ON p.pk_produto = v.pk_produto
WHERE v.pk_produto = 1 AND v.quantidade = 3 -- 8

SELECT c.nome, SUM(v.valor_total) FROM cliente c
INNER JOIN venda v ON v.pk_cliente = c.pk_cliente
GROUP BY v.pk_cliente
ORDER BY SUM(v.valor_total) DESC; -- 9 Seleciona o cliente e o total que ele gastou e ordena do maior valor para o menor