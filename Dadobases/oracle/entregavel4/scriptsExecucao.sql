SELECT
    arthur.genero_mais_curtido() -- 1
FROM
    DUAL;


DECLARE -- 2 (Tomei a liberdade de adicionar o nome do artista caso exista musicas com o mesmo nome)
	p_musica VARCHAR2(50) := 'Newlove'; -- (Além disso coloquei o id do usuário para referenciar a playlist de curtidas)
	p_artista VARCHAR2(50) := 'Sewesrslvt'; -- Essa daqui da erro devido não achar a musica no banco
	p_user_id NUMBER := 1;
BEGIN
	arthur.favoritar(p_musica,p_artista,p_user_id);
END;

DECLARE -- 2 Essa da erro por a musica já estar curtida
	p_musica VARCHAR2(50) := 'Money Trees';
	p_artista VARCHAR2(50) := 'Kendrick Lamar';
	p_user_id NUMBER := 1;
BEGIN
	arthur.favoritar(p_musica,p_artista,p_user_id);
END;

DECLARE -- 2 Essa deve funcionar
	p_musica VARCHAR2(50) := 'The art of dying';
	p_artista VARCHAR2(50) := 'Gojira';
	p_user_id NUMBER := 1;
BEGIN
	arthur.favoritar(p_musica,p_artista,p_user_id);
END;


DECLARE -- 3 (Isso daqui retorna todos os usuarios pq eles sempres são 0)
	p_coluna VARCHAR2(50) := 'IS_STAFF'; -- Se quiser mudar é só trocar os valores do auth_user
	p_query VARCHAR2(50) := '0';
BEGIN
	arthur.buscar_usuario_por_campo(p_coluna, p_query);
END;

DECLARE -- 4
	CURSOR c_usuarios IS -- Pega os usuários
		SELECT username FROM arthur.auth_user;

	v_cursor SYS_REFCURSOR; -- recebe um cursor
	v_username VARCHAR2(200); 
	v_contador NUMBER := 0; -- Conta os que não segue ele mas ele seue
	v_user_max NUMBER := 0; -- Quantidade que ele segue e não o segue do que tiver maior
	v_user_max_seguidores VARCHAR2(200); -- Nome do campeão que não é seguido por muita gente
BEGIN
	FOR user IN c_usuarios LOOP
		segue_nao_seguido(user.username,v_cursor); -- Pega o cursor com os nomes
	
		LOOP -- Conta todos que não o seguem e ele segue
			FETCH v_cursor INTO v_username;
			EXIT WHEN v_cursor%NOTFOUND;
			v_contador := v_contador + 1;
		END LOOP;
		
		CLOSE v_cursor;
		
		IF v_contador > v_user_max THEN -- Caso ele seja maior do que o maior no momento
			v_user_max := v_contador;
			v_user_max_seguidores := user.username;
		END IF;
	END LOOP;

    DBMS_OUTPUT.PUT_LINE('Usuário: ' || v_user_max_seguidores);
    DBMS_OUTPUT.PUT_LINE('Quantidade: ' || v_user_max);
END;

BEGIN -- 5 (Tu pediu uma procedure que retorne o email,etc em pipelined, mas até onde eu sei isso não é possível)
    comunidade_recomendacao;
END;

DECLARE -- 6
	v_id NUMBER;
	v_genero VARCHAR2(50) := 'rock';
	v_artista VARCHAR2(200);
BEGIN
  v_id := arthur.mydj.constructor('ricardao');
  DBMS_OUTPUT.PUT_LINE('ID: ' || v_id);
  arthur.mydj.gerar_playlist_genero(v_genero);
  arthur.mydj.sugerir_musicas;
  v_artista := arthur.mydj.artista_mais_curtido;
  DBMS_OUTPUT.PUT_LINE('Artista mais curtido: ' || v_artista);
END;

-- 7
BEGIN 
	arthur.listar_musica_playlist_mais_ouvidas();
END;