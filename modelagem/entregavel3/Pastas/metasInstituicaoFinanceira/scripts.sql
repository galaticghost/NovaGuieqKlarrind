SELECT * FROM funcionario WHERE pk_funcionario IN (SELECT pk_funcionario FROM metas GROUP BY pk_funcionario HAVING SUM(nota) >= 400);-- 1 vai dar 0 pq não tem nenhuma. se quiser um resultado poe 320 ou 328

SELECT AVG(nota) FROM metas INNER JOIN funcionario f GROUP BY f.gerente HAVING gerente = 0; -- 3 vai dar só um por que só há uma equipe

SELECT nome, categoria, (7 - quantidade ) AS faltando FROM funcionario f INNER JOIN metas m ON m.pk_funcionario = f.pk_funcionario WHERE faltando > 0  -- 4

