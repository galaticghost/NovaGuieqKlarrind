SELECT -- 1 
    pr.nome,
    p.NOME,
    p."DATA",
    AVG(l.RESPOSTA)
FROM
    likert l
    INNER JOIN questao q ON q.PK_QUESTAO = l.PK_QUESTAO
    INNER JOIN PESQUISA p ON p.PK_PESQUISA = q.PK_PESQUISA
    INNER JOIN produto pr ON pr.PK_PESQUISA = p.PK_PESQUISA
GROUP by
    p.NOME,
    pr.nome,
    p."DATA";

SELECT -- 2
    pr.nome,
    AVG(resposta)
FROM
    pesquisa p
    INNER JOIN produto pr ON pr.pk_pesquisa = p.pk_pesquisa
    INNER JOIN questao ON questao.pk_pesquisa = p.pk_pesquisa
    INNER JOIN likert l ON l.pk_questao = questao.pk_questao
GROUP BY
    pr.nome;

SELECT -- 3
    p.nome
FROM
    produto p
    INNER JOIN pesquisa pe ON pe.pk_pesquisa = p.pk_pesquisa
    INNER JOIN questao q ON pe.pk_pesquisa = q.pk_pesquisa
    INNER JOIN likert l ON l.pk_questao = q.pk_questao
GROUP BY
    p.nome
HAVING
    AVG(l.resposta) >= 4;

SELECT -- 4 
    *  --Eu demorei decadas para perceber que eu já terminei a consulta 
FROM   -- ao inves de colocar o produto pivotado nas questões
    (
        SELECT
            q.questao,
            l.RESPOSTA,
            p.nome
        FROM
            QUESTAO q
            INNER JOIN LIKERT l ON l.PK_QUESTAO = q.PK_QUESTAO
            INNER JOIN pesquisa pe ON q.PK_pesquisa = pe.PK_PESQUISA
            INNER JOIN PRODUTO p ON p.PK_PESQUISA = pe.PK_PESQUISA
    ) PIVOT (
        AVG(resposta) FOR questao IN (
            'O sabor é bom?',
            'Gostou?',
            '1 a 5: comer?',
            'Sim ou não',
            'food scale'
        )
    );

SELECT * -- 5
FROM (
    SELECT p.nome, 
           l.RESPOSTA, 
           CASE 
               WHEN pa.IDADE BETWEEN 18 AND 24 THEN 1
               WHEN pa.IDADE BETWEEN 25 AND 30 THEN 2
               WHEN pa.IDADE BETWEEN 31 AND 40 THEN 3
				ELSE 4
           END AS FaixaEtaria
    FROM produto p
    INNER JOIN pesquisa pe ON pe.PK_PESQUISA = p.PK_PESQUISA
    INNER JOIN QUESTAO q ON q.PK_PESQUISA = p.PK_PESQUISA
    INNER JOIN LIKERT l ON l.PK_QUESTAO = q.pk_questao
    INNER JOIN PARTICIPANTE pa ON pa.PK_PARTICIPANTE = l.PK_PARTICIPANTE
    WHERE l.RESPOSTA >= 4
)
PIVOT (
    COUNT(RESPOSTA)
    FOR FaixaEtaria IN (1 AS "18-24", 2 AS "25-30", 3 AS "31-40", 4 AS "41+")
);

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