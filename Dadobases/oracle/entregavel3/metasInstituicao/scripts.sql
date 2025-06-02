CREATE
OR REPLACE PROCEDURE alterar_quantidade_pos_janeiro -- 1
AS BEGIN
UPDATE metas
SET
    quantidade = 0
WHERE
    data > to_date ('2025-01-31', 'YYYY-MM-DD');
    COMMIT;
END;

-- 2
CREATE OR REPLACE FUNCTION calcular_nota_final_meta( 
	p_colaborador VARCHAR2,
	p_categoria VARCHAR2
) RETURN VARCHAR2
AS
	v_sql VARCHAR2(1000);
	v_nota_final NUMBER;
	v_porcentagem VARCHAR2(5);
BEGIN
	v_sql := 'SELECT m.nota FROM metas m INNER JOIN funcionario f ON f.pk_funcionario = m.pk_funcionario WHERE m.categoria = :categoria AND f.nome = :colaborador';
	EXECUTE IMMEDIATE v_sql INTO v_nota_final USING p_categoria,p_colaborador;
	IF v_nota_final > 100 THEN
		v_nota_final := 100;
	END IF;
	v_porcentagem := v_nota_final || '%';
	return v_porcentagem;
END;

CREATE OR REPLACE PROCEDURE adicionar_notas_metas( -- 3 em andamento
	p_nome IN VARCHAR2
)
AS
	v_sql VARCHAR2(1000);
	v_nota VARCHAR2(5);
	v_id_funcionario NUMBER;
BEGIN
	v_sql := 'SELECT pk_funcionario FROM funcionario WHERE nome = :nome';
	EXECUTE IMMEDIATE v_sql INTO v_id_funcionario USING p_nome;
	
	v_nota := calcular_nota_final_meta(p_nome,'seguros');
	v_sql := 'UPDATE metas SET nota_final = :nota WHERE categoria = ''seguros'' AND pk_funcionario = :id';
	EXECUTE IMMEDIATE v_sql USING v_nota,v_id_funcionario;
	
	v_nota := calcular_nota_final_meta(p_nome,'contas');
	v_sql := 'UPDATE metas SET nota_final = :nota WHERE categoria = ''contas'' AND pk_funcionario = :id';
	EXECUTE IMMEDIATE v_sql USING v_nota,v_id_funcionario;
		
	v_nota := calcular_nota_final_meta(p_nome,'financiamentos');
	v_sql := 'UPDATE metas SET nota_final = :nota WHERE categoria = ''financiamentos'' AND pk_funcionario = :id';
	EXECUTE IMMEDIATE v_sql USING v_nota,v_id_funcionario;
			
	v_nota := calcular_nota_final_meta(p_nome,'empréstimo');
	v_sql := 'UPDATE metas SET nota_final = :nota WHERE categoria = ''empréstimo'' AND pk_funcionario = :id';
	EXECUTE IMMEDIATE v_sql USING v_nota,v_id_funcionario;
	
	COMMIT;
END;

	