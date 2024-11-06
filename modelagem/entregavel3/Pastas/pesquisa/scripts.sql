SELECT p.nome,p.data, pr.nome, AVG(resposta) FROM pesquisa p
INNER JOIN produto pr ON pr.pk_pesquisa = p.pk_pesquisa
INNER JOIN questao ON questao.pk_pesquisa = p.pk_pesquisa
INNER JOIN likert l ON l.pk_questao = questao.pk_questao
GROUP BY p.pk_pesquisa;-- 1

SELECT pr.nome, AVG(resposta) FROM pesquisa p
INNER JOIN produto pr ON pr.pk_pesquisa = p.pk_pesquisa
INNER JOIN questao ON questao.pk_pesquisa = p.pk_pesquisa
INNER JOIN likert l ON l.pk_questao = questao.pk_questao
GROUP BY p.pk_pesquisa; -- 2

SELECT p.nome FROM produto p
INNER JOIN pesquisa pe ON pe.pk_pesquisa = p.pk_pesquisa
INNER JOIN questao q ON pe.pk_pesquisa = q.pk_pesquisa
INNER JOIN likert l ON l.pk_questao = q.pk_questao
GROUP BY p.pk_produto
HAVING AVG(l.resposta) >= 3 -- 3, vai dar nada, mas se colocar 3 dá os dois

SELECT q.questao,AVG(l.resposta) FROM questao q
INNER JOIN likert l ON l.pk_questao = q.pk_questao
GROUP BY questao
HAVING AVG(l.resposta) > 3; --6 Seleciona a questao com a média superior a três.

