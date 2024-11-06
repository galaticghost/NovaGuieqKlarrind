CREATE TABLE produto(
  pk_produto INTEGER PRIMARY KEY NOT NULL,
  nome VARCHAR(100) NOT NULL,
  data DATE NOT NULL);

CREATE TABLE pesquisa(
  pk_pesquisa INTEGER PRIMARY KEY NOT NULL,
  nome VARCHAR(100) NOT NULL,
  data DATE NOT NULL
);

CREATE TABLE pesquisa_participante(
  pk_pesquisa_participante INTEGER PRIMARY KEY NOT NULL,
  pk_pesquisa REFERENCES pesquisa NOT NULL,
  pk_participante REFERENCES participante NOT NULL
);

--gpt
INSERT INTO produto(nome, data) VALUES
('Produto A', '2024-11-05'),
('Produto B', '2024-11-05'),
('Produto C', '2024-11-05'),
('Produto D', '2024-11-05'),
('Produto E', '2024-11-05'),
('Produto F', '2024-11-05'),
('Produto G', '2024-11-05'),
('Produto H', '2024-11-05'),
('Produto I', '2024-11-05'),
('Produto J', '2024-11-05'),
('Produto K', '2024-11-05'),
('Produto L', '2024-11-05'),
('Produto M', '2024-11-05'),
('Produto N', '2024-11-05'),
('Produto O', '2024-11-05'),
('Produto P', '2024-11-05'),
('Produto Q', '2024-11-05'),
('Produto R', '2024-11-05'),
('Produto S', '2024-11-05'),
('Produto T', '2024-11-05');

-- eu
INSERT INTO pesquisa(nome,data) VALUES ('Sabor produto','2024-11-11');

DELETE FROM texto;
DELETE FROM likert;
DELETE FROM questao;

INSERT INTO questao(questao,tipo) VALUES ('O sabor é bom?',0),('Gostou?',0),
('1 a 5: comer?',0),('Escala comeria de novo',0),('Sim ou não',0),('food scale',0),('COMER bo?',1)
,('Diga se é bom',1);

ALTER TABLE questao ADD COLUMN pk_pesquisa REFERENCES pesquisa;
UPDATE questao SET pk_pesquisa = 1;

INSERT INTO questao(questao,tipo,pk_pesquisa) values ('Bueno?',0,1),('Goid?',0,1)

-- GPT
INSERT INTO likert (pk_questao, pk_participante, resposta) VALUES 
(1, 1, 3), (1, 2, 4), (1, 3, 2), (1, 4, 5), (1, 5, 1), (1, 6, 4), (2, 1, 2), (2, 2, 5), 
(2, 3, 3), (2, 4, 1), (2, 5, 4), (2, 6, 2), (3, 1, 5), (3, 2, 3), (3, 3, 4), (3, 4, 2), 
(3, 5, 5), (3, 6, 1), (4, 1, 1), (4, 2, 2), (4, 3, 3), (4, 4, 4), (4, 5, 5), (4, 6, 3), 
(5, 1, 4), (5, 2, 1), (5, 3, 5), (5, 4, 2), (5, 5, 4), (5, 6, 1);

ALTER TABLE produto ADD COLUMN pk_pesquisa REFERENCES pesquisa;

UPDATE produto SET pk_pesquisa = 1 WHERE pk_produto = 1;

INSERT INTO pesquisa(nome,data) VALUES ('O futuro','2024-12-12');
UPDATE produto SET pk_pesquisa = 2 WHERE pk_produto = 2;

INSERT INTO questao(questao,tipo,pk_pesquisa) VALUES ('Futuro Escala',0,2),('Futuro 1 a 5',0,2),
('Vale a pena?',0,2),('de 1 a 5 como você ve o tempo?',0,2);
UPDATE questao SET pk_pesquisa = 2 WHERE pk_questao = 9 OR pk_questao = 10

-- GPT! GPT! GPT !G PGOPTEDOP GPT !

INSERT INTO likert (pk_questao, pk_participante, resposta) VALUES
(9, 7, 4),
(9, 8, 2),
(9, 9, 5),
(9, 10, 3),
(9, 11, 4),
(9, 12, 1),
(9, 13, 3),
(10, 7, 2),
(10, 8, 4),
(10, 9, 1),
(10, 10, 5),
(10, 11, 3),
(10, 12, 4),
(10, 13, 2),
(11, 7, 3),
(11, 8, 5),
(11, 9, 2),
(11, 10, 4),
(11, 11, 1),
(11, 12, 3),
(11, 13, 4),
(12, 7, 1),
(12, 8, 3),
(12, 9, 4),
(12, 10, 2),
(12, 11, 5),
(12, 12, 4),
(12, 13, 2),
(13, 7, 5),
(13, 8, 1),
(13, 9, 3),
(13, 10, 2),
(13, 11, 4),
(13, 12, 5),
(13, 13, 1),
(14, 7, 2),
(14, 8, 3),
(14, 9, 5),
(14, 10, 4),
(14, 11, 1),
(14, 12, 2),
(14, 13, 3);
