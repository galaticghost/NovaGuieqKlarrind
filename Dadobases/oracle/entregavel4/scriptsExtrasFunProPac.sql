CREATE OR REPLACE FUNCTION desconto_10_porcento( -- 1
	p_valor NUMBER
) RETURN NUMBER
AS
BEGIN
	RETURN p_valor * 0.9;
END;

CREATE OR REPLACE PROCEDURE aumentar_estoque ( -- 2
	p_quantidade IN OUT NUMBER
)
AS
BEGIN
	p_quantidade := p_quantidade + 10;
END;

CREATE OR REPLACE PROCEDURE consultar_email ( -- 3 
	p_id IN INTEGER,
	p_email OUT VARCHAR2
) AS
	v_code NUMBER;
	E_ID_INVALIDO EXCEPTION;
BEGIN
	IF p_id < 1 THEN
		RAISE E_ID_INVALIDO;
	END IF;

	SELECT email INTO p_email FROM usuario WHERE usuario_id = p_id;
	
	EXCEPTION
		WHEN E_ID_INVALIDO THEN
			DBMS_OUTPUT.PUT_LINE('O id inserido deve ser maior que 1');
			p_email := 'Não encontrado';
		WHEN NO_DATA_FOUND THEN
			DBMS_OUTPUT.PUT_LINE('Não foi encontrado nenhuma linha com esse id');
			p_email := 'Não encontrado';
		WHEN OTHERS THEN
			DBMS_OUTPUT.PUT_LINE('Ocorreu um erro na execução desse procedimento');
			v_code := SQLCODE;
			DBMS_OUTPUT.PUT_LINE('Erro: ' || v_code);
			p_email := 'Não encontrado';
END;


CREATE OR REPLACE TYPE t_quadrado AS TABLE OF NUMBER; -- 4

CREATE OR REPLACE FUNCTION random_squared( -- 4
    p_number INTEGER -- Interger para não te um loop de 3.5 números
) RETURN t_quadrado
AS
	resultado t_quadrado := t_quadrado(); -- inicia um 'array' vazio com tamanho zero
	num_random INTEGER; -- Coloquei integer para não ter número quebrado(Ficava feio)
BEGIN
	FOR valor IN 1 .. p_number LOOP -- Itera de 1 até o número escolhido
		num_random := DBMS_RANDOM.VALUE(1,500); 
		resultado.EXTEND; -- Aumenta o tamanho do array em +1
		resultado(resultado.COUNT) := POWER(num_random,2); -- adiciona o valor no resultado no index mais alto do resultado
	END LOOP;
	RETURN resultado;
END;

CREATE OR REPLACE TYPE funcionario_obj AS OBJECT ( -- 5
  id NUMBER,
  nome VARCHAR2(100),
  codigo VARCHAR2(10),
  departamento VARCHAR2(100)
);

CREATE OR REPLACE TYPE t_funcionarios AS TABLE OF funcionario_obj; -- 5

CREATE OR REPLACE FUNCTION listar_funcionarios_departamento( -- 5
	p_codigo VARCHAR2
) RETURN t_funcionarios PIPELINED
AS
BEGIN
	FOR l IN (SELECT id,nome, d.codigo,departamento FROM ARTHUR.DEPARTAMENTOS d 
	INNER JOIN EMPREGADOS e ON e.codigo = d.codigo
	WHERE d.CODIGO = p_codigo) 
	LOOP
		PIPE ROW (funcionario_obj(l.id,l.nome,l.codigo,l.departamento));
	END LOOP;

	RETURN;
END;
SELECT

CREATE OR REPLACE TYPE palavra_divida AS TABLE OF VARCHAR2(1000); -- 6

CREATE OR REPLACE FUNCTION dividir_palavras(p_texto IN VARCHAR2) -- 6
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


CREATE OR REPLACE FUNCTION contar_palavras(p_texto IN VARCHAR2) -- 7
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
    v_contador INTEGER;
BEGIN
    FOR linha IN (SELECT resposta FROM texto WHERE pk_questao = 5) LOOP
        v_texto_total := v_texto_total || ' ' || linha.resposta;
    END LOOP;

    v_contador := contar_palavras(v_texto_total);

    DBMS_OUTPUT.PUT_LINE('Total palavras: ' || v_contador);
END;