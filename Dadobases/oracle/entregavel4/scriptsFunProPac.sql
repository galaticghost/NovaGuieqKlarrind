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

CREATE OR REPLACE PROCEDURE favoritar(
	p_musica IN VARCHAR2,
	p_artista IN VARCHAR2,
	p_user_id IN VARCHAR2
) AS
v_sql VARCHAR2(500);
v_id NUMBER;
BEGIN
	v_sql := 'SELECT ID FROM musica_musicasalva WHERE nome = :nome AND artista = :artista';
	EXECUTE IMMEDIATE v_sql INTO v_id USING p_musica,p_artista;

	v_sql := 'INSERT INTO MUSICA_MUSICASALVA_CURTIDA(musicasalva_id,user_id) VALUES (:id,:userid)';
	EXECUTE IMMEDIATE v_sql USING v_id, p_user_id;
	
	
END;


SELECT * FROM MUSICA_PLAYLIST mmp   