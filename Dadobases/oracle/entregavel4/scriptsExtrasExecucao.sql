DECLARE v_res VARCHAR2 (500);

-- 1
-- já que não especificou quais produtos pegar e só coloquei um
BEGIN
SELECT
    desconto_10_porcento (preco) INTO v_res
FROM
    res_produto
FETCH FIRST
    1 ROWS ONLY;

DBMS_OUTPUT.PUT_LINE ('Valor final: R$' || v_res);

END;

SELECT -- 4
    random_squared (5)
FROM
    dual;

-- 5 (Eu não criei um bloco pq não fazia sentido, só se fizesse um put_line mas um select já basta)
SELECT listar_funcionarios_departamento('NUSYEWJS') FROM dual;

SELECT -- 6
    dividir_palavras ('BOLA ZAUL AZULAZ ZUKS ASe eu não sei ler!')
FROM
    dual;

SELECT -- 7
    contar_palavras ('BOLA ZAUL AZULAZ ZUKS ASe eu não sei ler!')
FROM
    dual;