SELECT * FROM evento ORDER BY data; -- 1
SELECT * FROM evento WHERE pk_evento IN (SELECT pk_evento FROM cliente_evento); -- 2, virá todos no caso

SELECT COUNT(evento.pk_categoria),categoria.nome FROM evento 
INNER JOIN categoria ON evento.pk_categoria = categoria.pk_categoria 
GROUP BY evento.pk_categoria ORDER BY COUNT(evento.pk_categoria) DESC -- 3

SELECT c.nome FROM categoria c FULL JOIN evento e ON c.pk_categoria = e.pk_categoria WHERE e.pk_categoria IS NULL -- 4 

SELECT nome,texto FROM mensagem INNER JOIN cliente c ON mensagem.pk_cliente = c.pk_cliente -- 5, o contéudo das mensagem está correto, é nonsense mesmo

SELECT (SELECT COUNT(*) FROM cliente WHERE idade > 17 AND idade < 23) AS '18-22',
(SELECT COUNT(*) FROM cliente WHERE idade > 22 AND idade < 29) AS '23-28',
(SELECT COUNT(*) FROM cliente WHERE idade > 28 AND idade < 36) AS '29-35',
(SELECT COUNT(*) FROM cliente WHERE idade > 35 AND idade < 45) AS '34-44',
(SELECT COUNT(*) FROM cliente WHERE idade > 44 AND idade < 60) AS '45-59',
(SELECT COUNT(*) FROM cliente WHERE idade > 59) AS '60-100'
FROM cliente LIMIT 1; --6 

SELECT a.email, COUNT(e.pk_administrador) AS 'Eventos administrados' FROM administrador a INNER JOIN evento e ON a.pk_administrador = e.pk_administrador
GROUP BY (e.pk_administrador) -- 7 Seleciona o email e a quantidade de eventos administrado por cada administrador