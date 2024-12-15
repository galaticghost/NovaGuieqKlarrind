DELETE FROM jogador_partida;
DELETE FROM partida;
DELETE FROM jogador;

DELETE FROM equipe WHERE pk_equipe > 4;

-- chat gpt
INSERT INTO jogador(pk_equipe,nome,n_contrato,tipo_contrato,publicacao,data_inicio,inscricao,nascimento,apelido) VALUES
(1,'Carlos Silva',101,'Efetivo','2024-11-01','2024-11-05','ABC123','1993-04-12','Carlito'),
(1,'André Pereira',102,'Emprestado','2024-10-15','2024-10-17','DEF456','1994-07-18',NULL),
(1,'Gabriel Costa',103,'Efetivo','2024-09-20','2024-09-22','GHI789','1995-06-10','Gabs'),
(1,'Thiago Souza',104,'Emprestado','2024-08-30','2024-09-02','JKL012','1992-03-25',NULL),
(1,'Lucas Oliveira',105,'Efetivo','2024-07-12','2024-07-15','MNO345','1996-05-20','Luquinha'),
(1,'Rafael Lima',106,'Efetivo','2024-06-05','2024-06-08','PQR678','1994-12-30','Rafa'),
(1,'Felipe Alves',107,'Emprestado','2024-05-10','2024-05-13','STU901','1993-08-22','Fê'),
(1,'Marcos Santos',108,'Efetivo','2024-04-15','2024-04-18','VWX234','1996-11-14','Marcão'),
(1,'Diego Rocha',109,'Emprestado','2024-03-25','2024-03-28','YZA567','1995-02-02',NULL),
(1,'Eduardo Martins',110,'Efetivo','2024-02-10','2024-02-12','BCD890','1992-09-30','Duda'),
(1,'Vinícius Gomes',111,'Emprestado','2024-01-15','2024-01-17','EFG123','1994-04-18','Vini'),
(1,'João Barbosa',112,'Efetivo','2023-12-05','2023-12-07','HIJ456','1997-06-20','Joãozinho'),

(2,'Felipe Rocha',201,'Efetivo','2024-11-12','2024-11-15','JKL789','1992-08-11','Félix'),
(2,'Renato Alves',202,'Emprestado','2024-10-18','2024-10-20','MNO123','1996-02-22',NULL),
(2,'Lucas Martins',203,'Efetivo','2024-09-02','2024-09-04','PQR456','1993-12-05','Luka'),
(2,'Rodolfo Costa',204,'Efetivo','2024-08-20','2024-08-22','STU567','1995-09-11','Rafa'),
(2,'Gabriel Silva',205,'Emprestado','2024-07-15','2024-07-17','VWX890','1994-11-19',NULL),
(2,'Lucas Lima',206,'Efetivo','2024-06-10','2024-06-12','YZA123','1997-04-28','Luquinhas'),
(2,'José Souza',207,'Efetivo','2024-05-25','2024-05-27','BCD456','1995-01-15','Zé'),
(2,'Juliano Pereira',208,'Emprestado','2024-04-05','2024-04-08','EFG789','1996-07-30','Juca'),
(2,'Marcos Rocha',209,'Efetivo','2024-03-20','2024-03-23','HIJ012','1993-02-05',NULL),
(2,'Fábio Barbosa',210,'Efetivo','2024-02-01','2024-02-03','KLM345','1994-10-18','Fabinho'),
(2,'Fernando Gomes',211,'Emprestado','2024-01-10','2024-01-12','NOP678','1992-06-21','Nando'),
(2,'Carlos Martins',212,'Efetivo','2023-12-20','2023-12-22','QRS901','1995-03-25','Carlão'),

(3,'Matheus Lima',301,'Efetivo','2024-11-20','2024-11-23','TUV234','1997-05-16',NULL),
(3,'Bruno Costa',302,'Emprestado','2024-10-25','2024-10-28','WXY567','1996-12-12','Bru'),
(3,'Rodrigo Rocha',303,'Efetivo','2024-09-10','2024-09-12','ZAB890','1995-11-04','Digão'),
(3,'Thiago Santos',304,'Efetivo','2024-08-01','2024-08-03','CDE123','1994-07-15','Tite'),
(3,'Marcos Oliveira',305,'Emprestado','2024-07-15','2024-07-18','FGH456','1992-04-19','Marcinho'),
(3,'Felipe Pereira',306,'Efetivo','2024-06-10','2024-06-12','IJK789','1997-03-22','Fê'),
(3,'Gabriel Rocha',307,'Efetivo','2024-05-30','2024-06-02','LMN012','1994-11-28',NULL),
(3,'Douglas Barbosa',308,'Emprestado','2024-04-10','2024-04-12','OPQ345','1995-08-06','Doug'),
(3,'Lucas Pereira',309,'Efetivo','2024-03-15','2024-03-17','RST678','1996-09-30','Luquinha'),
(3,'Fábio Gomes',310,'Efetivo','2024-02-25','2024-02-27','UVW901','1993-01-05','Fabinho'),
(3,'Juliano Rocha',311,'Emprestado','2024-01-30','2024-02-02','XYZ234','1997-10-02',NULL),
(3,'Ricardo Costa',312,'Efetivo','2023-12-15','2023-12-17','BCD567','1995-06-30','Ricardinho'),

(4,'Alan Souza',401,'Efetivo','2024-11-25','2024-11-28','EFG012','1993-09-05',NULL),
(4,'Eduardo Lima',402,'Efetivo','2024-10-01','2024-10-03','HIJ345','1996-02-18','Duda'),
(4,'Lucas Rocha',403,'Emprestado','2024-09-15','2024-09-17','KLM678','1994-05-24',NULL),
(4,'Ricardo Almeida',404,'Efetivo','2024-08-25','2024-08-27','NOP901','1995-07-30','Ricardo'),
(4,'Bruno Gomes',405,'Emprestado','2024-07-30','2024-08-02','PQR234','1996-11-09','Bru'),
(4,'Gustavo Pereira',406,'Efetivo','2024-06-15','2024-06-18','STU567','1992-03-30',NULL),
(4,'Vinícius Costa',407,'Efetivo','2024-05-10','2024-05-12','VWX890','1997-01-11','Vini'),
(4,'Felipe China',408,'Emprestado','2024-04-20','2024-04-23','YZA123','1994-10-12','Félix'),
(4,'José Martins',409,'Efetivo','2024-03-05','2024-03-08','BCD234','1995-08-19','Zé'),
(4,'Marcos Lima',410,'Efetivo','2024-02-15','2024-02-18','EFG567','1996-06-06',NULL),
(4,'Rodrigo Oliveira',411,'Emprestado','2024-01-10','2024-01-13','GHI890','1993-04-09','Digão'),
(4,'Felipe Barbosa',412,'Efetivo','2023-12-05','2023-12-07','JKL234','1994-12-28','Fê');

-- CHAT GPT 
INSERT INTO partida(pk_casa, pk_visitante, data, local, qtd_cartoes, gols) VALUES
(1, 2, '2024-11-05', 'Estádio do Maracanã', 4, '3 X 1'),  -- pk_casa 1 contra pk_visitante 2
(1, 3, '2024-11-08', 'Arena Castelão', 3, '2 X 0'),       -- pk_casa 1 contra pk_visitante 3
(1, 4, '2024-11-12', 'Estádio Mineirão', 5, '1 X 2'),      -- pk_casa 1 contra pk_visitante 4
(2, 3, '2024-11-15', 'Estádio Beira-Rio', 2, '1 X 3'),     -- pk_casa 2 contra pk_visitante 3
(2, 4, '2024-11-18', 'Arena Corinthians', 4, '2 X 2'),     -- pk_casa 2 contra pk_visitante 4
(3, 4, '2024-11-20', 'Estádio Morumbi', 3, '0 X 1'),       -- pk_casa 3 contra pk_visitante 4
(2, 1, '2024-11-22', 'Estádio Beira-Rio', 3, '2 X 1'),     -- pk_casa 2 contra pk_visitante 1
(3, 1, '2024-11-25', 'Arena Castelão', 2, '1 X 3'),        -- pk_casa 3 contra pk_visitante 1
(4, 1, '2024-11-28', 'Estádio Mineirão', 6, '4 X 0'),      -- pk_casa 4 contra pk_visitante 1
(3, 2, '2024-12-01', 'Estádio Morumbi', 4, '2 X 1');       -- pk_casa 3 contra pk_visitante 2
INSERT INTO partida(pk_casa, pk_visitante, data, local, qtd_cartoes, gols) VALUES
(4, 2, '2024-11-08', 'Estádio Beira-Rio', 4, '3 X 2'),  -- pk_casa 4 contra pk_visitante 2
(4, 3, '2024-11-12', 'Arena Corinthians', 2, '1 X 0');  -- pk_casa 4 contra pk_visitante 3
-- Esses ai é tudo gpt
INSERT INTO jogador_partida(pk_jogador, pk_partida) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 7),
(1, 8),
(1, 9),

(2, 1),
(2, 2),
(2, 3),
(2, 7),
(2, 8),
(2, 9),

(3, 1),
(3, 2),
(3, 3),
(3, 7),
(3, 8),
(3, 9),

(4, 1),
(4, 2),
(4, 3),
(4, 7),
(4, 8),
(4, 9),

(5, 1),
(5, 2),
(5, 3),
(5, 7),
(5, 8),
(5, 9),

(6, 1),
(6, 2),
(6, 3),
(6, 7),
(6, 8),
(6, 9),

(7, 1),
(7, 2),
(7, 3),
(7, 7),
(7, 8),
(7, 9),

(8, 1),
(8, 2),
(8, 3),
(8, 7),
(8, 8),
(8, 9),

(9, 1),
(9, 2),
(9, 3),
(9, 7),
(9, 8),
(9, 9),

(10, 1),
(10, 2),
(10, 3),
(10, 7),
(10, 8),
(10, 9),

(11, 1),
(11, 2),
(11, 3),
(11, 7),
(11, 8),
(11, 9);


INSERT INTO jogador_partida(pk_jogador, pk_partida) VALUES
(13, 1),
(13, 4),
(13, 5),
(13, 7),
(13, 10),
(13, 11),

(14, 1),
(14, 4),
(14, 5),
(14, 7),
(14, 10),
(14, 11),

(15, 1),
(15, 4),
(15, 5),
(15, 7),
(15, 10),
(15, 11),

(16, 1),
(16, 4),
(16, 5),
(16, 7),
(16, 10),
(16, 11),

(17, 1),
(17, 4),
(17, 5),
(17, 7),
(17, 10),
(17, 11),

(18, 1),
(18, 4),
(18, 5),
(18, 7),
(18, 10),
(18, 11),

(19, 1),
(19, 4),
(19, 5),
(19, 7),
(19, 10),
(19, 11),

(20, 1),
(20, 4),
(20, 5),
(20, 7),
(20, 10),
(20, 11),

(21, 1),
(21, 4),
(21, 5),
(21, 7),
(21, 10),
(21, 11),

(22, 1),
(22, 4),
(22, 5),
(22, 7),
(22, 10),
(22, 11),

(23, 1),
(23, 4),
(23, 5),
(23, 7),
(23, 10),
(23, 11);

INSERT INTO jogador_partida(pk_jogador, pk_partida) VALUES
(25, 2),
(25, 4),
(25, 6),
(25, 8),
(25, 10),
(25, 12),

(26, 2),
(26, 4),
(26, 6),
(26, 8),
(26, 10),
(26, 12),

(27, 2),
(27, 4),
(27, 6),
(27, 8),
(27, 10),
(27, 12),

(28, 2),
(28, 4),
(28, 6),
(28, 8),
(28, 10),
(28, 12),

(29, 2),
(29, 4),
(29, 6),
(29, 8),
(29, 10),
(29, 12),

(30, 2),
(30, 4),
(30, 6),
(30, 8),
(30, 10),
(30, 12),

(31, 2),
(31, 4),
(31, 6),
(31, 8),
(31, 10),
(31, 12),

(32, 2),
(32, 4),
(32, 6),
(32, 8),
(32, 10),
(32, 12),

(33, 2),
(33, 4),
(33, 6),
(33, 8),
(33, 10),
(33, 12),

(34, 2),
(34, 4),
(34, 6),
(34, 8),
(34, 10),
(34, 12),

(35, 2),
(35, 4),
(35, 6),
(35, 8),
(35, 10),
(35, 12);

INSERT INTO jogador_partida(pk_jogador, pk_partida) VALUES
(37, 3),
(37, 5),
(37, 6),
(37, 9),
(37, 11),
(37, 12),

(38, 3),
(38, 5),
(38, 6),
(38, 9),
(38, 11),
(38, 12),

(39, 3),
(39, 5),
(39, 6),
(39, 9),
(39, 11),
(39, 12),

(40, 3),
(40, 5),
(40, 6),
(40, 9),
(40, 11),
(40, 12),

(41, 3),
(41, 5),
(41, 6),
(41, 9),
(41, 11),
(41, 12),

(42, 3),
(42, 5),
(42, 6),
(42, 9),
(42, 11),
(42, 12),

(43, 3),
(43, 5),
(43, 6),
(43, 9),
(43, 11),
(43, 12),

(44, 3),
(44, 5),
(44, 6),
(44, 9),
(44, 11),
(44, 12),

(45, 3),
(45, 5),
(45, 6),
(45, 9),
(45, 11),
(45, 12),

(46, 3),
(46, 5),
(46, 6),
(46, 9),
(46, 11),
(46, 12),

(47, 3),
(47, 5),
(47, 6),
(47, 9),
(47, 11),
(47, 12);

-- esse foi eu 
ALTER TABLE jogador_partida ADD COLUMN cartao_amarelo INTEGER DEFAULT 0;
ALTER TABLE jogador_partida ADD COLUMN cartao_vermelho INTEGER DEFAULT 0;

UPDATE jogador_partida SET cartao_amarelo = 1 WHERE pk_jogador = 18 AND (pk_partida = 7 OR pk_partida = 10 OR pk_partida = 11);
UPDATE jogador_partida SET cartao_amarelo = 1 WHERE pk_jogador = 13 AND (pk_partida = 7 OR pk_partida = 10 OR pk_partida = 11);
UPDATE jogador_partida SET cartao_vermelho = 1 WHERE pk_jogador = 14 AND (pk_partida = 1);
UPDATE partida SET gols  = '0 X 2';