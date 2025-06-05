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

CREATE OR REPLACE TYPE palavra_divida AS TABLE OF VARCHAR2(1000); -- 3

CREATE OR REPLACE FUNCTION dividir_palavras(p_texto IN VARCHAR2)
RETURN palavra_divida PIPELINED
AS
    v_posicao INTEGER := 1;
    v_tamanho INTEGER;
    v_palavra VARCHAR2(100);
    v_texto VARCHAR2(500) := TRIM(p_texto);
BEGIN
    LOOP
        v_tamanho := INSTR(v_texto || ' ', ' ', v_posicao) - v_posicao;
        EXIT WHEN v_tamanho < 0;
        v_palavra := SUBSTR(v_texto, v_posicao, v_tamanho);
        IF v_palavra IS NOT NULL THEN
            PIPE ROW(v_palavra);
        END IF;
        v_posicao := v_posicao + v_tamanho + 1;
    END LOOP;

    RETURN;
END dividir_palavras;


CREATE OR REPLACE FUNCTION contar_palavras(p_texto IN VARCHAR2)
RETURN INTEGER
AS
    v_contador INTEGER := 0;
BEGIN
    FOR palavra IN (SELECT * FROM TABLE(dividir_palavras(p_texto))) LOOP
        v_contador := v_contador + 1;
    END LOOP;

    RETURN v_contador;
END contar_palavras;

DECLARE
    v_texto_total VARCHAR2(500);
    v_contador    INTEGER;
BEGIN
    FOR linha IN (SELECT resposta FROM texto WHERE pk_questao = 5) LOOP
        v_texto_total := v_texto_total || ' ' || linha.resposta;
    END LOOP;

    v_contador := contar_palavras(v_texto_total);

    DBMS_OUTPUT.PUT_LINE('Total palavras: ' || v_contador);
END;
