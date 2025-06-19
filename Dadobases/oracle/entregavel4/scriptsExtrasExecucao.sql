DECLARE v_res VARCHAR2 (500);

-- 1
-- já que não especificou quais produtos pegar e só coloquei um
BEGIN
SELECT
    arthur.desconto_10_porcento (preco) INTO v_res
FROM
    res_produto
FETCH FIRST
    1 ROWS ONLY;

DBMS_OUTPUT.PUT_LINE ('Valor final: R$' || v_res);

END;

DECLARE -- 2
v_quantidade NUMBER;

BEGIN
SELECT
    estoque INTO v_quantidade
FROM
    arthur.res_produto
WHERE
    produto_id = 1;

aumentar_estoque (v_quantidade);

UPDATE arthur.res_produto
SET
    estoque = v_quantidade
WHERE
    produto_id = 1;

DBMS_OUTPUT.PUT_LINE (v_quantidade);

END;

DECLARE -- 3 
    p_id NUMBER := 1;
    p_email VARCHAR2(200);
BEGIN
	arthur.consultar_email(p_id,p_email);
	DBMS_OUTPUT.PUT_LINE('Email: ' || p_email);

END;

SELECT -- 4
    arthur.random_squared (5)
FROM
    dual;

-- 5 (Eu não criei um bloco pq não fazia sentido, só se fizesse um put_line mas um select já basta)
SELECT
    arthur.listar_funcionarios_departamento ('NUSYEWJS')
FROM
    dual;

SELECT -- 6
    arthur.dividir_palavras ('BOLA ZAUL AZULAZ ZUKS ASe eu não sei ler!')
FROM
    dual;

SELECT -- 7
    arthur.contar_palavras ('BOLA ZAUL AZULAZ ZUKS ASe eu não sei ler!')
FROM
    dual;

DECLARE -- 8
    TYPE num_lista_type IS TABLE OF NUMBER; -- cria uma coleção para poder criar a lista
    num_lista num_lista_type := num_lista_type(4, 54, 320, 53, 2, 294, -94); -- cria a lista
    numero NUMBER := 94; -- Váriavel usada para ver se está na lista
    existe BOOLEAN := FALSE;
BEGIN
    FOR i IN 1 .. num_lista.COUNT LOOP -- Loopa por toda a lista
        IF num_lista(i) = numero THEN -- Se achar termina o loop e coloca existe como true
            existe := TRUE;
            EXIT;
        END IF;
    END LOOP;

    IF existe THEN
        DBMS_OUTPUT.PUT_LINE('O número ' || numero || ' está na lista.');
    ELSE
        DBMS_OUTPUT.PUT_LINE('O número ' || numero || ' não está na lista.');
    END IF;
END;

BEGIN -- 9 (primeiro o id do restaurante e depois a porcentagem (10% no caso))
	arthur.desconto_porcento(2,10);	
END;

BEGIN -- 10 (aqui não funcionou, mas foi por conta de permissões da minha conta)
	arthur.grant_permissions('nestor','select','arthur.res_produto');
END; -- ORA-00990: missing or invalid privilege
