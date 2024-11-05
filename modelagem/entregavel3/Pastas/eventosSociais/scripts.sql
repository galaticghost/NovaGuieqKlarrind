SELECT * FROM evento ORDER BY data; -- 1
SELECT * FROM evento WHERE pk_evento IN (SELECT pk_evento FROM cliente_evento); -- 2, virá todos no caso

SELECT COUNT(evento.pk_categoria),categoria.nome FROM evento 
INNER JOIN categoria ON evento.pk_categoria = categoria.pk_categoria 
GROUP BY evento.pk_categoria ORDER BY COUNT(evento.pk_categoria) DESC -- 3

SELECT c.nome FROM categoria c FULL JOIN evento e ON c.pk_categoria = e.pk_categoria WHERE e.pk_categoria IS NULL -- 4 

SELECT nome,texto FROM mensagem INNER JOIN cliente c ON mensagem.pk_cliente = c.pk_cliente -- 5, o contéudo das mensagem está correto, é nonsense mesmo

                                        --6