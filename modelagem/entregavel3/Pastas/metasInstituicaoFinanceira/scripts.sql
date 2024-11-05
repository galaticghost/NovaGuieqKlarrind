SELECT (
  SELECT AVG(quantidade) FROM metas WHERE categoria = 'contas') AS 'Contas', 
  (SELECT AVG(quantidade) FROM metas WHERE categoria = 'empréstimo') AS 'Empréstimos',
  (SELECT AVG(quantidade) FROM metas WHERE categoria = 'seguros') AS 'Seguros',
  (SELECT AVG(quantidade) FROM metas WHERE categoria = 'financiamentos') AS 'Financiamentos'
 FROM metas ORDER BY ;