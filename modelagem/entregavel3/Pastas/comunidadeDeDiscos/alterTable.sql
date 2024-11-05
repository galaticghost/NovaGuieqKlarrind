DELETE FROM usuario;

DELETE FROM banda WHERE pk_banda > 15;
--chatgpt. insert de emergencia
INSERT INTO usuario(nome, email, senha) VALUES ('Ana Costa', 'ana.costa@example.com', 'senha123');
INSERT INTO usuario(nome, email, senha) VALUES ('Bruno Silva', 'bruno.silva@example.com', 'senha456');
INSERT INTO usuario(nome, email, senha) VALUES ('Carla Mendes', 'carla.mendes@example.com', 'senha789');
INSERT INTO usuario(nome, email, senha) VALUES ('Daniel Oliveira', 'daniel.oliveira@example.com', 'senhaabc');
INSERT INTO usuario(nome, email, senha) VALUES ('Eduardo Lima', 'eduardo.lima@example.com', 'senhadfgh');
INSERT INTO usuario(nome, email, senha) VALUES ('Fernanda Rocha', 'fernanda.rocha@example.com', 'senhajkl');
INSERT INTO usuario(nome, email, senha) VALUES ('Gabriel Almeida', 'gabriel.almeida@example.com', 'senhaqwe');
INSERT INTO usuario(nome, email, senha) VALUES ('Helena Ferreira', 'helena.ferreira@example.com', 'senhapoiuy');
INSERT INTO usuario(nome, email, senha) VALUES ('Igor Santos', 'igor.santos@example.com', 'senhasdfg');
INSERT INTO usuario(nome, email, senha) VALUES ('Juliana Nascimento', 'juliana.nascimento@example.com', 'senhahjk');
INSERT INTO usuario(nome, email, senha) VALUES ('Lucas Pereira', 'lucas.pereira@example.com', 'senhamnbv');
INSERT INTO usuario(nome, email, senha) VALUES ('Mariana Souza', 'mariana.souza@example.com', 'senhalkjh');
INSERT INTO usuario(nome, email, senha) VALUES ('Natalia Gomes', 'natalia.gomes@example.com', 'senhacvbn');
INSERT INTO usuario(nome, email, senha) VALUES ('Otávio Martins', 'otavio.martins@example.com', 'senhazyx');
INSERT INTO usuario(nome, email, senha) VALUES ('Paula Ribeiro', 'paula.ribeiro@example.com', 'senhamnb');

-- chatgpt
INSERT INTO avaliacao_album(pk_album, pk_usuario, avaliacao, nota) VALUES
(1, 1, 'Muito bom', 4),
(2, 1, 'Excelente', 5),
(3, 1, 'Bom, mas poderia ser melhor', 3),
(4, 1, 'Eu gostei', 4),
(5, 1, 'Ótimo álbum', 5),

(6, 2, 'Não gostei muito', 2),
(7, 2, 'Média, sem nada de especial', 3),
(8, 2, 'Fraco, não me agradou', 2),
(9, 2, 'Interessante, mas faltou algo', 3),
(10, 2, 'Bom trabalho, mas poderia ser mais inovador', 4),

(11, 3, 'Sensacional', 5),
(12, 3, 'Incrível, recomendo demais', 5),
(13, 3, 'Gostei, mas não é perfeito', 4),
(14, 3, 'Muito bom, merece mais atenção', 4),
(15, 3, 'É bom, mas não é o melhor álbum', 3);

-- chatgpt
INSERT INTO avaliacao_album(pk_album, pk_usuario, avaliacao, nota) VALUES
(5, 4, 'Muito bom, mas ainda falta algo', 4),
(5, 6, 'Eu gostei, mas não é o melhor álbum', 3),
(15, 7, 'Álbum incrível, totalmente recomendado', 5),
(15, 8, 'Ótimo trabalho, mas algumas músicas são repetitivas', 4);
--chat
INSERT INTO avaliacao_album(pk_album, pk_usuario, avaliacao, nota) VALUES
(10, 14, 'Bom álbum, mas falta mais energia nas faixas', 3),
(10, 12, 'Gostei das letras, mas o ritmo poderia ser melhor', 4);


CREATE TABLE show(
  pk_show INTEGER PRIMARY KEY NOT NULL,
  pk_turne INTEGER REFERENCES turne NOT NULL,
  data DATE NOT NULL
);


CREATE TABLE avaliacao_show(
    pk_avaliacao_show INTEGER PRIMARY KEY NOT NULL,
    pk_show REFERENCES turne NOT NULL,
    pk_usuario REFERENCES usuario NOT NULL,
    avaliacao TEXT,
    nota INTEGER
);

DROP TABLE avaliacao_turne;

-- gpt
INSERT INTO turne(pk_banda, data) VALUES
(1, '2024-11-10'),
(2, '2024-11-15'),
(3, '2024-11-20'),
(4, '2024-11-25'),
(5, '2024-12-01'),

(6, '2024-12-05'),
(7, '2024-12-10'),
(8, '2024-12-15'),
(9, '2024-12-20'),
(10, '2024-12-25'),

(11, '2025-01-05'),
(12, '2025-01-10'),
(13, '2025-01-15'),
(14, '2025-01-20'),
(15, '2025-01-25');

--gpt

INSERT INTO show(pk_turne, data) VALUES
(1, '2024-11-12'),
(1, '2024-11-18'),
(1, '2024-11-22'),
(1, '2024-11-28'),
(1, '2024-12-02'),

(10, '2024-12-06'),
(10, '2024-12-09'),
(10, '2024-12-13'),
(10, '2024-12-17'),
(10, '2024-12-21');
--gpt
INSERT INTO avaliacao_show(pk_show, pk_usuario, avaliacao, nota) VALUES
(3, 1, 'Show incrível, energia total!', 5),
(3, 2, 'Gostei muito, mas achei que poderia ter mais interação com o público', 4),
(3, 3, 'Foi bom, mas a acústica estava ruim', 3),
(3, 4, 'Excelente apresentação, não vejo a hora de ir novamente', 5),
(3, 5, 'Show mediano, algumas músicas não me agradaram muito', 2),

(8, 6, 'Amei o show! A banda estava muito afinada', 5),
(8, 7, 'Muito bom, mas as luzes estavam um pouco fortes', 4),
(8, 8, 'O show foi ótimo, mas a organização deixou a desejar', 3),
(8, 9, 'Espetacular! A energia da banda foi contagiante', 5),
(8, 10, 'Banda boa, mas faltou algo nas músicas mais lentas', 4);
