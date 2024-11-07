SELECT * FROM funcionario WHERE pk_funcionario IN (SELECT pk_funcionario FROM metas GROUP BY pk_funcionario HAVING SUM(nota) >= 400);-- 1 vai dar 0 pq não tem nenhuma. se quiser um resultado poe 320 ou 328

SELECT (SELECT AVG(quantidade) FROM metas GROUP BY categoria ORDER BY AVG(quantidade) DESC LIMIT 1) AS Melhor,
(SELECT AVG(quantidade) FROM metas GROUP BY categoria ORDER BY AVG(quantidade) LIMIT 1) AS Pior,
(SELECT AVG(quantidade) FROM metas GROUP BY categoria ORDER BY AVG(quantidade) LIMIT 1 OFFSET 1) AS Mediano,
(SELECT AVG(quantidade) FROM metas GROUP BY categoria ORDER BY AVG(quantidade) LIMIT 1 OFFSET 2) AS Mediano
FROM metas GROUP BY categoria LIMIT 1; -- 2

SELECT AVG(nota) FROM metas INNER JOIN funcionario f GROUP BY f.gerente HAVING gerente = 0; -- 3 vai dar só um por que só há uma equipe

SELECT nome, categoria, (7 - quantidade ) AS faltando FROM funcionario f INNER JOIN metas m ON m.pk_funcionario = f.pk_funcionario WHERE faltando > 0  -- 4

SELECT f.nome FROM metas m INNER JOIN funcionario f ON f.pk_funcionario = m.pk_funcionario
GROUP BY m.pk_funcionario HAVING AVG(quantidade) > 10 AND SUM(nota) > 250;  -- 5 Nome do funcionario que tiver uma quantidade media acima de 10 e a soma das notas maior que 250; 