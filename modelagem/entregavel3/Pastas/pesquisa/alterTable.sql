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




