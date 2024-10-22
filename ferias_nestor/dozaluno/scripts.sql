INSERT INTO pessoa (nome_pessoa, cpf, cod_matricula, endereco) VALUES 
('Alice Pereira', '111.222.333-44', 'M061', 'Rua 1, 101'),
('Bruno Silva', '222.333.444-55', 'M062', NULL),
('Carla Santos', '333.444.555-66', 'M063', 'Avenida 2, 202'),
('Daniel Oliveira', '444.555.666-77', 'M064', NULL),
('Ester Nascimento', '555.666.777-88', 'M065', 'Rua 3, 303'),
('Felipe Lima', '666.777.888-99', 'M066', NULL),
('Gabi Almeida', '777.888.999-00', 'M067', 'Avenida 4, 404'),
('Hugo Costa', '888.999.000-11', 'M068', NULL),
('Isis Rocha', '999.000.111-22', 'M069', 'Rua 5, 505'),
('João Vitor', '000.111.222-33', 'M070', NULL),
('Karine Mendes', '111.222.444-55', 'M071', 'Avenida 6, 606'),
('Lucas Martins', '222.333.555-66', 'M072', NULL),
('Mariana Ferreira', '303.444.666-77', 'M073', 'Rua 7, 707'),
('Nicolas Teixeira', '436.555.777-88', 'M074', NULL),
('Olga Santos', '535.666.888-99', 'M075', 'Avenida 8, 808'),
('Paulo Almeida', '666.777.699-00', 'M076', NULL),
('Quésia Souza', '776.888.000-11', 'M077', 'Rua 9, 909'),
('Rafael Gomes', '828.999.111-22', 'M078', NULL),
('Sofia Costa', '952.000.222-33', 'M079', 'Avenida 10, 1010'),
('Thiago Dias', '036.111.333-44', 'M080', NULL),
('Ursula Ferreira', '153.222.444-55', 'M081', 'Rua 11, 1111'),
('Vinícius Almeida', '222.535.555-66', 'M082', NULL),
('Wesley Santos', '333.444.666-77', 'M083', 'Avenida 12, 1212'),
('Yasmin Rocha', '444.555.777-88', 'M084', NULL),
('Zé Carlos', '555.666.888-99', 'M085', 'Rua 13, 1313'),
('Ana Clara', '666.777.999-00', 'M086', NULL),
('Bruna Costa', '777.888.000-11', 'M087', 'Avenida 14, 1414'),
('Carlos Eduardo', '838.999.111-22', 'M088', NULL),
('Diana Martins', '999.000.222-33', 'M089', 'Rua 15, 1515'),
('Elisa Mendes', '000.111.333-44', 'M090', NULL),
('Fábio Teixeira', '111.222.444-69', 'M091', 'Avenida 16, 1616'),
('Gustavo Ribeiro', '235.333.555-66', 'M092', NULL);

INSERT INTO professor (pk_pessoa, titulacao, disponibilidade) VALUES 
(1, 'Professor', '20 horas'),
(2, 'Mestre', '15 horas'),
(3, 'Doutor', '10 horas'),
(4, 'Professor', '25 horas'),
(5, 'Mestre', '30 horas'),
(6, 'Doutor', '20 horas'),
(7, 'Professor', '15 horas'),
(8, 'Mestre', '10 horas'),
(9, 'Doutor', '20 horas'),
(10, 'Professor', '25 horas'),
(11, 'Mestre', '30 horas'),
(12, 'Doutor', '15 horas'),
(13, 'Professor', '20 horas'),
(14, 'Mestre', '10 horas'),
(15, 'Doutor', '30 horas');

INSERT INTO curso (nome_curso, area) VALUES 
('Administração', 'Ciências Sociais Aplicadas'),
('Engenharia de Computação', 'Exatas'),
('Medicina', 'Saúde'),
('Direito', 'Ciências Sociais'),
('Psicologia', 'Ciências Humanas'),
('Arquitetura', 'Humanas e Artes'),
('Biomedicina', 'Saúde'),
('Educação Física', 'Saúde e Bem-Estar'),
('Ciência da Computação', 'Exatas'),
('Engenharia Civil', 'Exatas'),
('Gestão de Recursos Humanos', 'Ciências Sociais Aplicadas'),
('Marketing', 'Ciências Sociais Aplicadas'),
('Matemática', 'Exatas'),
('Fisioterapia', 'Saúde'),
('Sistemas de Informação', 'Exatas');

INSERT INTO turma (semestre, pk_professor, pk_curso) VALUES 
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(1, 11, 11),
(2, 12, 12),
(3, 13, 13),
(4, 14, 14),
(5, 15, 15);

INSERT INTO sala(nome_sala, capacidade) VALUES ('101', 25);
INSERT INTO sala(nome_sala, capacidade) VALUES ('102', 30);
INSERT INTO sala(nome_sala, capacidade) VALUES ('103', 35);
INSERT INTO sala(nome_sala, capacidade) VALUES ('201', 20);
INSERT INTO sala(nome_sala, capacidade) VALUES ('202', 40);
INSERT INTO sala(nome_sala, capacidade) VALUES ('203', 45);
INSERT INTO sala(nome_sala, capacidade) VALUES ('301', 50);
INSERT INTO sala(nome_sala, capacidade) VALUES ('302', 22);
INSERT INTO sala(nome_sala, capacidade) VALUES ('303', 28);
INSERT INTO sala(nome_sala, capacidade) VALUES ('401', 33);
INSERT INTO sala(nome_sala, capacidade) VALUES ('402', 29);
INSERT INTO sala(nome_sala, capacidade) VALUES ('403', 38);
INSERT INTO sala(nome_sala, capacidade) VALUES ('404', 24);
INSERT INTO sala(nome_sala, capacidade) VALUES ('501', 42);
INSERT INTO sala(nome_sala, capacidade) VALUES ('502', 27);

INSERT INTO comodidade(nome_comodidade) VALUES 
('Projetor'),
('Ar Condicionado'),
('Lousa Branca'),
('Computador'),
('Cadeiras Confortáveis');

INSERT INTO comodidade_sala(pk_comodidade, pk_sala) VALUES 
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
(1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
(1, 11), (1, 12), (1, 13), (1, 14), (1, 15),
(2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
(2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
(2, 11), (2, 12), (2, 13), (2, 14), (2, 15),
(3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
(3, 6), (3, 7), (3, 8), (3, 9), (3, 10),
(3, 11), (3, 12), (3, 13), (3, 14), (3, 15),
(4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
(4, 6), (4, 7), (4, 8), (4, 9), (4, 10),
(4, 11), (4, 12), (4, 13), (4, 14), (4, 15),
(5, 1), (5, 2), (5, 3), (5, 4), (5, 5),
(5, 6), (5, 7), (5, 8), (5, 9), (5, 10),
(5, 11), (5, 12), (5, 13), (5, 14), (5, 15);

INSERT INTO disciplina(pk_professor, pk_sala, nome_disciplina) VALUES 
(1, 1, 'Matemática'),
(2, 2, 'Física'),
(3, 3, 'Química'),
(4, 4, 'Biologia'),
(5, 5, 'História'),
(6, 6, 'Geografia'),
(7, 7, 'Literatura'),
(8, 8, 'Educação Física'),
(9, 9, 'Arte'),
(10, 10, 'Informática'),
(11, 11, 'Filosofia'),
(12, 12, 'Sociologia'),
(13, 13, 'Inglês'),
(14, 14, 'Espanhol'),
(15, 15, 'Música'),
(1, 2, 'Matemática Avançada'),
(2, 3, 'Física Moderna'),
(3, 4, 'Química Orgânica'),
(4, 5, 'Biologia Celular'),
(5, 6, 'História do Brasil'),
(6, 7, 'Geografia Humana'),
(7, 8, 'Literatura Brasileira'),
(8, 9, 'Educação Artística'),
(9, 10, 'Tecnologia da Informação'),
(10, 11, 'Ética'),
(11, 12, 'Antropologia'),
(12, 13, 'Francês'),
(13, 14, 'Literatura Estrangeira'),
(14, 15, 'Canto Coral'),
(15, 1, 'Matemática Básica'),
(1, 3, 'Estatística'),
(2, 4, 'Química Inorgânica'),
(3, 5, 'Botânica'),
(4, 6, 'Geografia Física'),
(5, 7, 'Redação'),
(6, 8, 'Educação Ambiental');

INSERT INTO curso_disciplina(pk_curso, pk_disciplina) VALUES 
(1, 1),
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(3, 6),
(3, 7),
(4, 8),
(4, 9),
(5, 10),
(5, 11),
(6, 12),
(6, 13),
(7, 14),
(7, 15),
(8, 16),
(8, 17),
(9, 18),
(9, 19),
(10, 20),
(10, 21),
(11, 22),
(11, 23),
(12, 24),
(12, 25),
(13, 26),
(13, 27),
(14, 28),
(14, 29),
(15, 30),
(15, 1);

INSERT INTO aluno(pk_pessoa, pk_curso, pk_turma) VALUES 
(16, 1, 1),
(17, 2, 3),
(18, 3, 5),
(19, 4, 2),
(20, 5, 4),
(21, 6, 6),
(22, 7, 7),
(23, 8, 8),
(24, 9, 9),
(25, 10, 10),
(26, 11, 11),
(27, 12, 12),
(28, 13, 13),
(29, 14, 14),
(30, 15, 15),
(31, 1, 2),
(32, 2, 5);

SELECT * FROM pessoa;
SELECT * FROM aluno;
SELECT * FROM curso;
SELECT * FROM professor;
SELECT * FROM turma;
SELECT * FROM disciplina;
SELECT * FROM sala;
SELECT * FROM comodidade;
SELECT * FROM comodidade_sala;
SELECT * FROM curso_disciplina;
