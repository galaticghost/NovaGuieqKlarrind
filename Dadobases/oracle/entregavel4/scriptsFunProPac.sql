CREATE
OR REPLACE FUNCTION genero_mais_curtido RETURN VARCHAR2 AS v_genero VARCHAR2 (50); -- 1

BEGIN
SELECT
    genero INTO v_genero
FROM
    ARTHUR.USUARIO_GENEROS
GROUP BY
    genero
ORDER BY
    COUNT(genero) DESC
FETCH FIRST
    1 ROWS ONLY;

RETURN v_genero;

EXCEPTION WHEN NO_DATA_FOUND THEN RETURN NULL;

WHEN OTHERS THEN RETURN 'Houve um erro na execução dessa função';

END;

CREATE OR REPLACE PROCEDURE favoritar( -- 2
	p_musica IN VARCHAR2,
	p_artista IN VARCHAR2,
	p_user_id IN VARCHAR2
) AS
v_sql VARCHAR2(500);
v_musica NUMBER;
v_playlist NUMBER;
BEGIN
	v_sql := 'SELECT ID FROM ARTHUR.musica_musicasalva WHERE nome = :nome AND artista = :artista';
	EXECUTE IMMEDIATE v_sql INTO v_musica USING p_musica,p_artista;
	
	v_sql := 'INSERT INTO ARTHUR.MUSICA_MUSICASALVA_CURTIDA(musicasalva_id,user_id) VALUES (:id,:userid)';
	EXECUTE IMMEDIATE v_sql USING v_musica, p_user_id;
	
	v_sql := 'SELECT ID FROM ARTHUR.musica_playlist WHERE playlist_curtir = 1 AND user_id = :id';
	EXECUTE IMMEDIATE v_sql INTO v_playlist USING p_user_id;
	
	v_sql := 'INSERT INTO ARTHUR.MUSICA_MUSICASALVA_PLAYLISTS(musicasalva_id,playlist_id) VALUES (:musica,:playlist)';
	EXECUTE IMMEDIATE v_sql USING v_musica,v_playlist;
	
	EXCEPTION
		WHEN NO_DATA_FOUND THEN
			DBMS_OUTPUT.PUT_LINE('Música não encontrada');
			RETURN;
		WHEN DUP_VAL_ON_INDEX THEN
            DBMS_OUTPUT.PUT_LINE('A música já foi curtida');
			ROLLBACK;
		WHEN OTHERS THEN
			DBMS_OUTPUT.PUT_LINE('Ocorreu um erro na execução desse procedimento');
			ROLLBACK;
END;

CREATE OR REPLACE PROCEDURE buscar_usuario_por_campo ( -- 3
	p_coluna IN VARCHAR2,
	p_query IN VARCHAR2
) AS
	v_sql   VARCHAR2(500);
	v_cursor SYS_REFCURSOR; -- Esse SYS_REFCURSOR é declara que isso daqui é um cursor
	v_id  NUMBER;
	v_nome VARCHAR2(200);
	v_curtida NUMBER;
	v_curtida_musica NUMBER;
BEGIN
	v_sql := 'SELECT id FROM arthur.AUTH_USER WHERE ' || p_coluna || ' = :query';

	OPEN v_cursor FOR v_sql USING p_query; 

	LOOP
		FETCH v_cursor INTO v_id;
		EXIT WHEN v_cursor%NOTFOUND;
		SELECT first_name || ' ' || last_name AS nome INTO v_nome FROM arthur.auth_user WHERE id = v_id;
		SELECT COUNT(*) INTO v_curtida FROM arthur.COMUNIDADE_POST_CURTIDORES WHERE USER_ID = v_id;
		SELECT COUNT(*) INTO v_curtida_musica FROM arthur.MUSICA_MUSICASALVA_CURTIDA WHERE USER_ID = v_id;
		DBMS_OUTPUT.PUT_LINE('Nome: ' || v_nome || ' Posts curtidos: ' || v_curtida || ' Músicas curtidas: ' || v_curtida_musica);
	END LOOP;

	CLOSE v_cursor;
END;

CREATE OR REPLACE PROCEDURE segue_nao_seguido( -- 4
    p_nome IN VARCHAR2,
    p_cursor OUT SYS_REFCURSOR
) AS
    v_id arthur.auth_user.id%TYPE;
BEGIN 
    SELECT id INTO v_id FROM arthur.auth_user WHERE username = p_nome;

    OPEN p_cursor FOR
        SELECT au.username FROM arthur.auth_user au
        INNER JOIN arthur.usuario_seguidor us ON arthur.us.usuario_id = arthur.au.id
        WHERE arthur.us.seguidor_id = v_id AND NOT EXISTS -- ve os que ele segue
	    (SELECT 1 FROM arthur.usuario_seguidor uss  -- e tira os que seguem ele
	    WHERE arthur.uss.seguidor_id = au.id AND arthur.uss.usuario_id = v_id);

EXCEPTION
    WHEN NO_DATA_FOUND THEN -- Aqui ele não retorna nenhuma linha
        OPEN p_cursor FOR SELECT 'Nenhum usuário foi encontrado' AS username FROM dual WHERE 1 = 0;
	WHEN OTHERS THEN
		DBMS_OUTPUT.PUT_LINE('Ocorreu um erro na execução do procedimento');
END;