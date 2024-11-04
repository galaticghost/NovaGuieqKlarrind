DELETE FROM metas;
DELETE FROM funcionario;

CREATE TABLE funcionario(
    pk_funcionario INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    gerente BOOLEAN NOT NULL DEFAULT 0,
	pk_gerente INTEGER REFERENCES funcionario DEFAULT NULL
);

INSERT INTO funcionario(nome, gerente,pk_gerente) VALUES -- ChatGpt até o "lucas"
('Carlos Souza', 1,NULL),
('Ana Silva', 0,1),
('Mariana Oliveira',0,1),
('Ricardo Lima', 0,1),
('Fernanda Costa', 0,1),
('Pedro Santos', 0,1),
('Juliana Ferreira', 0,1),
('Bruno Almeida', 0,1),
('Tatiane Martins', 0,1),
('Lucas Pereira', 0,1);

CREATE TABLE metas(
  pk_metas INTEGER PRIMARY KEY NOT NULL,
  pk_funcionario INTEGER REFERENCES funcionario,
  categoria VARCHAR(30) NOT NULL,
  data DATE NOT NULL,
  quantidade INTEGER NOT NULL
);

INSERT INTO metas(pk_funcionario, categoria, data, quantidade) VALUES  -- ChatGpt ("Menos umas datas")
(2, 'seguros', '2024-10-15', 10),
(2, 'contas', '2024-10-22', 5),
(2, 'financiamentos', '2024-09-30', 8),
(2, 'empréstimo', '2024-10-05', 12),

(3, 'seguros', '2024-10-10', 7),
(3, 'contas', '2024-10-14', 9),
(3, 'financiamentos', '2024-10-21', 4),
(3, 'empréstimo', '2024-10-12', 15),

(4, 'seguros', '2024-10-20', 6),
(4, 'contas', '2024-10-18', 11),
(4, 'financiamentos', '2024-10-02', 5),
(4, 'empréstimo', '2024-10-25', 9),

(5, 'seguros', '2024-10-05', 8),
(5, 'contas', '2024-10-11', 10),
(5, 'financiamentos', '2024-10-15', 7),
(5, 'empréstimo', '2024-10-18', 14),

(6, 'seguros', '2024-10-30', 5),
(6, 'contas', '2024-10-01', 6),
(6, 'financiamentos', '2024-10-10', 9),
(6, 'empréstimo', '2024-10-01', 11),

(7, 'seguros', '2024-10-25', 12),
(7, 'contas', '2024-10-30', 7),
(7, 'financiamentos', '2024-10-13', 10),
(7, 'empréstimo', '2024-10-20', 13),

(8, 'seguros', '2024-10-15', 9),
(8, 'contas', '2024-10-27', 4),
(8, 'financiamentos', '2024-10-05', 8),
(8, 'empréstimo', '2024-10-15', 6),

(9, 'seguros', '2024-10-12', 11),
(9, 'contas', '2024-10-18', 3),
(9, 'financiamentos', '2024-09-24', 5),
(9, 'empréstimo', '2024-10-30', 7),

(10, 'seguros', '2024-09-05', 10),
(10, 'contas', '2024-10-20', 8),
(10, 'financiamentos', '2024-10-17', 12),
(10, 'empréstimo', '2024-10-10', 14);

ALTER TABLE metas ADD COLUMN nota INTEGER CHECK (nota <= 100);
ALTER TABLE metas ADD COLUMN data_avaliacao DATE;

-- tudo abaixo chatgpt
UPDATE metas SET nota = 75, data_avaliacao = '2025-02-01' WHERE pk_funcionario = 2;
UPDATE metas SET nota = 85, data_avaliacao = '2025-02-10' WHERE pk_funcionario = 2;
UPDATE metas SET nota = 90, data_avaliacao = '2025-02-15' WHERE pk_funcionario = 2;
UPDATE metas SET nota = 78, data_avaliacao = '2025-02-20' WHERE pk_funcionario = 2;

UPDATE metas SET nota = 82, data_avaliacao = '2025-02-05' WHERE pk_funcionario = 3;
UPDATE metas SET nota = 88, data_avaliacao = '2025-02-12' WHERE pk_funcionario = 3;
UPDATE metas SET nota = 92, data_avaliacao = '2025-02-18' WHERE pk_funcionario = 3;
UPDATE metas SET nota = 76, data_avaliacao = '2025-02-25' WHERE pk_funcionario = 3;

UPDATE metas SET nota = 80, data_avaliacao = '2025-02-03' WHERE pk_funcionario = 4;
UPDATE metas SET nota = 89, data_avaliacao = '2025-02-08' WHERE pk_funcionario = 4;
UPDATE metas SET nota = 91, data_avaliacao = '2025-02-14' WHERE pk_funcionario = 4;
UPDATE metas SET nota = 77, data_avaliacao = '2025-02-22' WHERE pk_funcionario = 4;

UPDATE metas SET nota = 84, data_avaliacao = '2025-02-04' WHERE pk_funcionario = 5;
UPDATE metas SET nota = 86, data_avaliacao = '2025-02-11' WHERE pk_funcionario = 5;
UPDATE metas SET nota = 90, data_avaliacao = '2025-02-16' WHERE pk_funcionario = 5;
UPDATE metas SET nota = 79, data_avaliacao = '2025-02-21' WHERE pk_funcionario = 5;

UPDATE metas SET nota = 81, data_avaliacao = '2025-02-02' WHERE pk_funcionario = 6;
UPDATE metas SET nota = 87, data_avaliacao = '2025-02-09' WHERE pk_funcionario = 6;
UPDATE metas SET nota = 93, data_avaliacao = '2025-02-17' WHERE pk_funcionario = 6;
UPDATE metas SET nota = 74, data_avaliacao = '2025-02-26' WHERE pk_funcionario = 6;

UPDATE metas SET nota = 83, data_avaliacao = '2025-02-06' WHERE pk_funcionario = 7;
UPDATE metas SET nota = 88, data_avaliacao = '2025-02-13' WHERE pk_funcionario = 7;
UPDATE metas SET nota = 94, data_avaliacao = '2025-02-19' WHERE pk_funcionario = 7;
UPDATE metas SET nota = 76, data_avaliacao = '2025-02-27' WHERE pk_funcionario = 7;

UPDATE metas SET nota = 79, data_avaliacao = '2025-02-07' WHERE pk_funcionario = 8;
UPDATE metas SET nota = 85, data_avaliacao = '2025-02-15' WHERE pk_funcionario = 8;
UPDATE metas SET nota = 91, data_avaliacao = '2025-02-20' WHERE pk_funcionario = 8;
UPDATE metas SET nota = 82, data_avaliacao = '2025-02-28' WHERE pk_funcionario = 8;

UPDATE metas SET nota = 77, data_avaliacao = '2025-02-08' WHERE pk_funcionario = 9;
UPDATE metas SET nota = 84, data_avaliacao = '2025-02-14' WHERE pk_funcionario = 9;
UPDATE metas SET nota = 89, data_avaliacao = '2025-02-21' WHERE pk_funcionario = 9;
UPDATE metas SET nota = 73, data_avaliacao = '2025-02-26' WHERE pk_funcionario = 9;

UPDATE metas SET nota = 80, data_avaliacao = '2025-02-10' WHERE pk_funcionario = 10;
UPDATE metas SET nota = 86, data_avaliacao = '2025-02-16' WHERE pk_funcionario = 10;
UPDATE metas SET nota = 88, data_avaliacao = '2025-02-22' WHERE pk_funcionario = 10;
UPDATE metas SET nota = 75, data_avaliacao = '2025-02-27' WHERE pk_funcionario = 10;
