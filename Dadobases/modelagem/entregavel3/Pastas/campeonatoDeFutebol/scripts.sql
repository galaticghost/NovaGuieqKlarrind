SELECT local, e.nome AS visitante, p.gols_do_visitante,p.gols_do_mandante, m.nome FROM partida p
INNER JOIN equipe e ON e.pk_equipe = p.pk_visitante
INNER JOIN equipe m ON m.pk_equipe = p.pk_casa; -- 1

SELECT j.nome, e.nome, SUM(g.gols) AS 'Soma' FROM jogador j
INNER JOIN equipe e ON e.pk_equipe = j.pk_equipe
INNER JOIN jogador_partida g ON g.pk_jogador = j.pk_jogador
GROUP BY j.pk_jogador
ORDER BY Soma
DESC LIMIT 1; -- 2

SELECT j.nome, SUM(jp.cartao_amarelo) AS 'Cartão Amarelo', SUM(jp.cartao_vermelho) AS 'Cartão Vermelho'FROM jogador_partida jp
INNER JOIN jogador j ON j.pk_jogador = jp.pk_jogador
GROUP BY j.pk_jogador
HAVING SUM(jp.cartao_amarelo) <> 0 OR SUM(jp.cartao_vermelho) <> 0; -- 3

SELECT e.nome FROM equipe e
INNER JOIN jogador j ON e.pk_equipe = j.pk_equipe
INNER JOIN jogador_partida p ON p.pk_jogador = j.pk_jogador 
GROUP BY e.pk_equipe
HAVING SUM(cartao_vermelho) = 0 AND SUM(cartao_amarelo) = 0; -- 4

SELECT local, COUNT(local) FROM partida GROUP BY local
ORDER BY COUNT(local) DESC LIMIT 1; -- 5



SELECT j.nome, e.nome FROM jogador j
INNER JOIN equipe e ON e.pk_equipe = j.pk_equipe
LEFT JOIN jogador_partida jp ON j.pk_jogador = jp.pk_jogador
WHERE jp.pk_jogador IS NULL -- 8 Seleciona o nome do jogador e sua equipe, apenas os que não participaram de nenhum jogo 