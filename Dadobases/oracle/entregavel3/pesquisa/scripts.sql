BEGIN FOR participante IN ( -- 1 (Como não tem nenhum participante com mais de 5 respostas, o resultado será zero)
    SELECT -- (Troque para 4 no Having para mostrar alguma coisa)
        nome,
        COUNT(*) as total,
        AVG(resposta) as media
    FROM
        PARTICIPANTE p
        INNER JOIN likert l ON p.pk_participante = l.pk_participante
    GROUP BY
        nome
    HAVING
        COUNT(*) > 5
) LOOP DBMS_OUTPUT.PUT_LINE (
    participante.nome || ': ' || participante.total || ' perguntas. Média ' || participante.media
);

END LOOP;

END;

CREATE OR REPLACE FUNCTION calcular_nps( -- 2 (Eu tomei a liberdade de converter os valores de 1 a 10 para 1 a 5)
	p_questao NUMBER -- (Porque o meu banco só tem resposta de no máximo 5)
) RETURN VARCHAR2
AS
	v_sql VARCHAR2(500);
	v_promotores NUMBER;
	v_detratores NUMBER;
	v_res_total NUMBER;
	v_nps NUMBER;
BEGIN
	v_sql := 'SELECT COUNT(1) FROM likert WHERE pk_questao = :id AND resposta >= 4.5';
	EXECUTE IMMEDIATE v_sql INTO v_promotores USING p_questao;
	v_sql := 'SELECT COUNT(1) FROM likert WHERE pk_questao = :id AND resposta <= 3';
	EXECUTE IMMEDIATE v_sql INTO v_detratores USING p_questao;
	v_sql := 'SELECT COUNT(1) FROM likert WHERE pk_questao = :id';
	EXECUTE IMMEDIATE v_sql INTO v_res_total USING p_questao;

	v_nps := (v_promotores - v_detratores) / v_res_total;
	RETURN v_nps;
END;