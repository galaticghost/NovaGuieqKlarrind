CREATE OR REPLACE PACKAGE faturamento_pkg AS -- 1
	PROCEDURE processar_pedido(p_id_venda NUMBER);
END;

CREATE OR REPLACE PACKAGE BODY faturamento_pkg AS
	PROCEDURE registrar_falha(p_mensagem VARCHAR2,p_pedido_id NUMBER) AS
	BEGIN
		INSERT INTO log_erros(pedido_id,mensagem_erro) VALUES (p_pedido_id,p_mensagem);
	END;

FUNCTION verificar_estoque(p_id_produto NUMBER,p_quantidade NUMBER) RETURN VARCHAR2
AS	
v_sql VARCHAR2(1000);
v_estoque NUMBER;
	BEGIN
		v_sql := 'SELECT estoque FROM res_produto WHERE produto_id = :id';
		EXECUTE IMMEDIATE v_sql INTO v_estoque USING p_id_produto;
		IF p_quantidade > v_estoque THEN
			RETURN 'F';
		ELSE
			RETURN 'V';
		END IF;
	EXCEPTION
	    WHEN NO_DATA_FOUND THEN
	        RETURN 'F';
	    WHEN OTHERS THEN
	        RETURN 'F';
	END;

PROCEDURE processar_pedido(p_id_venda NUMBER) AS
	
	CURSOR c_vp(p_id_venda NUMBER) IS
			SELECT VALOR_TOTAL, quantidade, produto_id FROM venda_produto WHERE venda_id = p_id_venda;
		
		v_valor venda_produto.valor_total%TYPE;
		v_quantidade venda_produto.quantidade%TYPE;
		v_produto_id venda_produto.produto_id%TYPE;
		v_valor_total NUMBER := 0;
	BEGIN
		OPEN c_vp(p_id_venda);
		LOOP
			FETCH c_vp INTO v_valor, v_quantidade, v_produto_id;
			EXIT WHEN c_vp%NOTFOUND;
			UPDATE res_produto SET estoque = estoque - v_quantidade WHERE produto_id = v_produto_id;
			v_valor_total := v_valor_total + v_valor;
		END LOOP;
		CLOSE c_vp;
		
		DBMS_OUTPUT.PUT_LINE(v_valor_total);
		COMMIT;

		EXCEPTION
		WHEN OTHERS THEN
		
		registrar_falha(SQLERRM, p_id_venda);
		ROLLBACK;
	END;
	
END;

CREATE OR REPLACE PACKAGE clientes_pkg AS -- 2
	FUNCTION inativo(p_id_clientes NUMBER) RETURN VARCHAR2;
	PROCEDURE inativar_clientes;
END;

CREATE OR REPLACE PACKAGE BODY clientes_pkg AS
	FUNCTION inativo(p_id_clientes NUMBER) RETURN VARCHAR2 AS
	BEGIN
		FOR dat IN (SELECT criacao FROM venda WHERE usuario_id = p_id_clientes) LOOP
		      IF dat.criacao >= TRUNC(ADD_MONTHS(SYSDATE, -12)) THEN
		        RETURN 'F';
		      END IF;
		    END LOOP;
		RETURN 'V';
	END;
	
	PROCEDURE inativar_clientes AS
	BEGIN
		FOR cliente IN (SELECT usuario_id FROM venda) LOOP
			IF inativo(cliente.usuario_id) = 'V' THEN
				UPDATE usuario SET ATIVO = 0  WHERE usuario_id = cliente.usuario_id;
			END IF;
		END LOOP;
	END;
END;
