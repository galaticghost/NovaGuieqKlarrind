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


CREATE OR REPLACE PACKAGE mydj AS -- 6
	FUNCTION constructor (p_username VARCHAR2) RETURN NUMBER;
	PROCEDURE gerar_playlist_genero(p_genero IN VARCHAR2);
	PROCEDURE sugerir_musicas;
	FUNCTION artista_mais_curtido RETURN VARCHAR2;
END mydj;

CREATE OR REPLACE PACKAGE BODY mydj AS -- 6
	v_user_id NUMBER;

	FUNCTION constructor(
		p_username VARCHAR2
	) RETURN NUMBER
	AS
		v_sql VARCHAR2(500);
	BEGIN
		v_sql := 'SELECT id FROM auth_user WHERE username = :username';
		EXECUTE IMMEDIATE v_sql INTO v_user_id USING p_username;
		RETURN v_user_id;
	END;

	PROCEDURE gerar_playlist_genero(
		p_genero IN VARCHAR2
	) AS
		CURSOR c_musica IS SELECT id -- Pega o id de umas músicas com base no genero
		FROM (SELECT id
		FROM musica_musicasalva mm
		WHERE genero = p_genero
		ORDER BY DBMS_RANDOM.VALUE
		)
		FETCH FIRST 25 ROWS ONLY; 
	
        v_id_musica musica_musicasalva.id%TYPE;
        v_id_playlist musica_playlist.id%TYPE; -- Isso daqui é um elemento surpresa que vamos utilizar mais tarde
	BEGIN
		
		INSERT INTO MUSICA_PLAYLIST(nome, descricao, user_id,playlist_curtir)
	    VALUES ('Playlist '|| p_genero, 'Playlist de '|| p_genero || ' gerada automaticamente', v_user_id,0)
	    RETURNING id INTO v_id_playlist; -- Isso daqui retorna o id da playlist que ele acabou de criar


		OPEN c_musica;
        
        LOOP
        	FETCH c_musica INTO v_id_musica;
        	EXIT WHEN c_musica%NOTFOUND;
        	INSERT INTO MUSICA_MUSICASALVA_PLAYLISTS(MUSICASALVA_ID,PLAYLIST_ID) VALUES (v_id_musica,v_id_playlist);
        END LOOP;
        CLOSE c_musica;
	END;

	PROCEDURE sugerir_musicas AS
		CURSOR c_musica IS SELECT nome, artista
				FROM (
				  SELECT nome, artista
				  FROM MUSICA_MUSICASALVA mm
				  WHERE mm.id NOT IN (
				    SELECT MUSICASALVA_ID
				    FROM MUSICA_MUSICASALVA_CURTIDA
				    WHERE USER_ID = v_user_id
				  )
				  ORDER BY DBMS_RANDOM.VALUE
				)
				WHERE ROWNUM <= 10;
		v_nome musica_musicasalva.nome%TYPE;
		v_artista musica_musicasalva.artista%TYPE;
	BEGIN
		OPEN c_musica;
		
		LOOP
			FETCH c_musica INTO v_nome,v_artista;
			EXIT WHEN c_musica%NOTFOUND;
			DBMS_OUTPUT.PUT_LINE('Nome: ' || v_nome || '. Artista: ' || v_artista);
		END LOOP;
		CLOSE c_musica;
	END;
	FUNCTION artista_mais_curtido RETURN VARCHAR2
	AS
		v_artista VARCHAR2(200);
	BEGIN
		SELECT artista INTO v_artista FROM MUSICA_MUSICASALVA mm
		INNER JOIN MUSICA_MUSICASALVA_CURTIDA mmc 
		ON mm.ID = mmc.MUSICASALVA_ID
		WHERE mmc.USER_ID = v_user_id
		GROUP BY ARTISTA
		ORDER BY COUNT(1) DESC
		FETCH FIRST 1 ROWS ONLY;
		
		RETURN v_artista;
	END;
END;


CREATE OR REPLACE PROCEDURE listar_musica_playlist_mais_ouvidas -- 7
AS
	v_i NUMBER := 0;
	v_musica VARCHAR2(200);
	v_count NUMBER;
BEGIN
	WHILE v_i < 15 LOOP
		SELECT nome,COUNT(1) INTO v_musica,v_count FROM MUSICA_MUSICASALVA mm 
		INNER JOIN MUSICA_MUSICASALVA_PLAYLISTS mmp
		ON mm.ID = mmp.MUSICASALVA_ID 
		GROUP BY nome
		ORDER BY COUNT(1) DESC
		OFFSET v_i ROWS
		FETCH NEXT 1 ROWS ONLY;
		
		DBMS_OUTPUT.PUT_LINE(v_musica || ' está em ' || v_count || ' playlists');

		v_i := v_i + 1;
	END LOOP;
	
END;
