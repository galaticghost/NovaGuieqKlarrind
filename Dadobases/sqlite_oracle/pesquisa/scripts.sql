SELECT --6 Seleciona a questao com a média superior a três.
    q.questao,
    AVG(l.resposta)
FROM
    questao q
    INNER JOIN likert l ON l.pk_questao = q.pk_questao
GROUP BY
    questao
HAVING
    AVG(l.resposta) > 3;