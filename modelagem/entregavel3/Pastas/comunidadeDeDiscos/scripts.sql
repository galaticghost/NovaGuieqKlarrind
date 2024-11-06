SELECT a.nome, AVG(b.nota) FROM album a INNER JOIN avaliacao_album b ON a.pk_album = b.pk_album 
GROUP BY b.pk_album ORDER BY SUM(nota) DESC LIMIT 3; -- 1, agr eu percebi que tem uns albuns sem nome (E tem o nome da banda no caso (Não é os self-titled))

SELECT COUNT(aa.pk_album), a.nome FROM avaliacao_album aa 
INNER JOIN album a ON aa.pk_album = a.pk_album GROUP BY aa.pk_album ORDER BY COUNT(aa.pk_album); DESC -- 2

SELECT midia FROM album GROUP BY midia ORDER BY COUNT(midia); DESC LIMIT 1 -- 3

SELECT u.nome,COUNT(a.pk_usuario) AS 'Contribuições' FROM usuario u  -- 4
INNER JOIN avaliacao_album a ON u.pk_usuario = a.pk_usuario GROUP BY a.pk_usuario;


SELECT u.nome,COUNT(a.pk_usuario) AS 'Contribuições' FROM usuario u 
INNER JOIN avaliacao_album a ON u.pk_usuario = a.pk_usuario GROUP BY a.pk_usuario; -- 4.5

SELECT u.nome AS 'Contribuições' FROM usuario u
LEFT JOIN avaliacao_show a ON u.pk_usuario = a.pk_usuario 
LEFT JOIN avaliacao_album ava ON u.pk_usuario = ava.pk_usuario WHERE a.pk_usuario IS NULL AND ava.pk_usuario; IS NULL -- 5

SELECT b.nome, AVG(aa.nota) FROM banda b 
INNER JOIN album a ON b.pk_banda = a.pk_banda
INNER JOIN avaliacao_album aa ON a.pk_album = aa.pk_album
GROUP BY b.pk_banda
ORDER BY AVG(aa.nota) DESC; -- 6

SELECT b.nome, AVG(aa.nota) FROM banda b 
INNER JOIN turne a ON b.pk_banda = a.pk_banda
INNER JOIN avaliacao_show aa ON a.pk_turne = aa.pk_show
GROUP BY b.pk_banda
ORDER BY AVG(aa.nota) DESC; -- 6.5


SELECT t.pk_turne, b.nome,t.data FROM turne t
INNER JOIN banda b ON b.pk_banda = t.pk_banda ORDER BY data LIMIT 5; -- 7 Selecione as turnes mais proximas