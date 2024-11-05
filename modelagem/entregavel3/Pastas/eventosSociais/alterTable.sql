CREATE TABLE mensagem(
  pk_mensagem INTEGER PRIMARY KEY NOT NULL,
  texto TEXT NOT NULL,
  mensagem_anterior REFERENCES mensagem,
  proxima_mensagem REFERENCES mensagem,
  pk_cliente REFERENCES cliente NOT NULL
);

CREATE TABLE categoria_favorita(
  pk_categoria_favorita INTEGER PRIMARY KEY NOT NULL,
  pk_categoria INTEGER REFERENCES categoria NOT NULL,
  pk_cliente INTEGER REFERENCES cliente NOT NULL
);

INSERT INTO cliente_evento(pk_cliente,pk_evento) VALUES (1,2),(6,2),(3,7),(4,7),(6,7),(10,11),(14,11);


-- Tudo ChatGPT
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (1, 1);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (2, 1);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (3, 2);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (4, 2);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (5, 3);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (6, 3);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (7, 4);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (8, 4);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (9, 5);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (10, 5);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (11, 6);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (12, 6);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (13, 7);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (14, 7);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (15, 8);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (1, 8);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (2, 9);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (3, 9);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (4, 10);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (5, 10);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (6, 11);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (7, 12);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (8, 12);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (9, 13);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (10, 13);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (11, 14);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (12, 15);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (13, 15);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (14, 15);
INSERT INTO categoria_favorita(pk_categoria, pk_cliente) VALUES (15, 15);


-- eu
INSERT INTO mensagem(texto,mensagem_anterior,proxima_mensagem,pk_cliente) VALUES ('Oi',NULL,NULL,1);
INSERT INTO mensagem(texto,mensagem_anterior,proxima_mensagem,pk_cliente) VALUES ('Olá',1,NULL,2);
INSERT INTO mensagem(texto,mensagem_anterior,proxima_mensagem,pk_cliente) VALUES ('Futuro?',2,NULL,1);
INSERT INTO mensagem(texto,mensagem_anterior,proxima_mensagem,pk_cliente) VALUES ('Sim dois ao quadro',3,NULL,2);
INSERT INTO mensagem(texto,mensagem_anterior,proxima_mensagem,pk_cliente) VALUES ('Quadro?',4,NULL,1);
INSERT INTO mensagem(texto,mensagem_anterior,proxima_mensagem,pk_cliente) VALUES ('Quatro 57',5,NULL,2);

UPDATE mensagem SET proxima_mensagem = 2 WHERE pk_mensagem = 1;
UPDATE mensagem SET proxima_mensagem = 3 WHERE pk_mensagem = 2;
UPDATE mensagem SET proxima_mensagem = 4 WHERE pk_mensagem = 3;
UPDATE mensagem SET proxima_mensagem = 5 WHERE pk_mensagem = 4;
UPDATE mensagem SET proxima_mensagem = 6 WHERE pk_mensagem = 5;

ALTER TABLE evento ADD COLUMN pk_categoria REFERENCES categoria;

UPDATE evento SET pk_categoria = 1 WHERE pk_evento = 1;
UPDATE evento SET pk_categoria = 4 WHERE pk_evento = 2;
UPDATE evento SET pk_categoria = 5 WHERE pk_evento = 3;
UPDATE evento SET pk_categoria = 8 WHERE pk_evento = 4;
UPDATE evento SET pk_categoria = 9 WHERE pk_evento = 5;
UPDATE evento SET pk_categoria = 1 WHERE pk_evento = 6;
UPDATE evento SET pk_categoria = 13 WHERE pk_evento = 7;
UPDATE evento SET pk_categoria = 11 WHERE pk_evento = 8;
UPDATE evento SET pk_categoria = 12 WHERE pk_evento = 9;
UPDATE evento SET pk_categoria = 14 WHERE pk_evento = 10;
UPDATE evento SET pk_categoria = 3 WHERE pk_evento = 11;
INSERT INTO categoria(nome) VALUES ('Caminhada');
UPDATE evento SET pk_categoria = 16 WHERE pk_evento = 12;
UPDATE evento SET pk_categoria = 6 WHERE pk_evento = 13;
UPDATE evento SET pk_categoria = 10 WHERE pk_evento = 14;
INSERT INTO categoria(nome) VALUES ('Lançamento');
UPDATE evento SET pk_categoria = 17 WHERE pk_evento = 15;