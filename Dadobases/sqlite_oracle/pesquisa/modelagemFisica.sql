CREATE TABLE
    participante (
        pk_participante NUMBER (10) PRIMARY KEY NOT NULL,
        nome VARCHAR2 (100) NOT NULL,
        idade INTEGER CHECK (idade >= 0) NOT NULL,
        genero VARCHAR2 (2) NOT NULL,
        renda NUMERIC CHECK (renda >= 0) NOT NULL,
        regiao CHAR(2) NOT NULL,
        endereco TEXT NOT NULL
    );

CREATE TABLE
    questao (
        pk_questao INTEGER PRIMARY KEY NOT NULL,
        questao TEXT NOT NULL,
        tipo CHAR(1) NOT NULL
    );

CREATE TABLE
    likert (
        pk_likert INTEGER PRIMARY KEY NOT NULL,
        pk_questao REFERENCES questao,
        pk_participante REFERENCES participante,
        resposta INTEGER CHECK (
            resposta >= 1
            OR resposta < 6
        ) NOT NULL
    );

CREATE TABLE
    texto (
        pk_texto INTEGER PRIMARY KEY NOT NULL,
        pk_questao REFERENCES questao,
        pk_participante REFERENCES participante,
        resposta TEXT NOT NULL
    );

CREATE TABLE
    produto (
        pk_produto INTEGER PRIMARY KEY NOT NULL,
        nome VARCHAR(100) NOT NULL,
        data DATE NOT NULL
    );

CREATE TABLE
    pesquisa (
        pk_pesquisa INTEGER PRIMARY KEY NOT NULL,
        nome VARCHAR(100) NOT NULL,
        data DATE NOT NULL
    );

CREATE TABLE
    pesquisa_participante (
        pk_pesquisa_participante INTEGER PRIMARY KEY NOT NULL,
        pk_pesquisa REFERENCES pesquisa NOT NULL,
        pk_participante REFERENCES participante NOT NULL
    );