CREATE TABLE usuario(
    pk_usuario INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(200) NOT NULL,
    senha VARCHAR(100) NOT NULL
);

CREATE TABLE banda(
    pk_banda INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE album(
    pk_album INTEGER PRIMARY KEY NOT NULL,
    pk_banda REFERENCES banda NOT NULL,
    nome VARCHAR(100) NOT NULL,
    genero VARCHAR(100) NOT NULL,
    duarcao VARCHAR(9) NOT NULL,
    tipo VARCHAR(30) NOT NULL
);

CREATE TABLE turne(
    pk_turne INTEGER PRIMARY KEY NOT NULL,
    pk_banda REFERENCES banda NOT NULL,
    data DATE NOT NULL
);

CREATE TABLE avaliacao_album(
    pk_avaliacao_album INTEGER PRIMARY KEY NOT NULL,
    pk_album REFERENCES album NOT NULL,
    pk_usuario REFERENCES usuario NOT NULL,
    avaliacao TEXT,
    nota INTEGER
);

CREATE TABLE avaliacao_turne(
    pk_avaliacao_turne INTEGER PRIMARY KEY NOT NULL,
    pk_turne REFERENCES turne NOT NULL,
    pk_usuario REFERENCES usuario NOT NULL,
    avaliacao TEXT,
    nota INTEGER
);