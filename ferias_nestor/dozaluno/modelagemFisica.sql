CREATE TABLE pessoa (
    pk_pessoa INTEGER PRIMARY KEY NOT NULL,
    nome_pessoa VARCHAR(200) NOT NULL,
    cpf VARCHAR(20) NOT NULL UNIQUE,
    cod_matricula VARCHAR(20) NOT NULL UNIQUE,
    endereco TEXT
);

CREATE TABLE professor(
    pk_pessoa INTEGER REFERENCES pessoa NOT NULL,
    titulacao TEXT NOT NULL,
    disponibilidade INTEGER NOT NULL
);

CREATE TABLE curso(
    pk_curso INTEGER PRIMARY KEY NOT NULL,
    nome_curso VARCHAR(100) NOT NULL,
    area VARCHAR(100) NOT NULL
);

CREATE TABLE turma(
    pk_turma INTEGER PRIMARY KEY NOT NULL,
    semestre INTEGER NOT NULL,
    pk_professor INTEGER REFERENCES pessoa NOT NULL,
    pk_curso INTEGER REFERENCES curso NOT NULL
);

CREATE TABLE aluno(
    pk_pessoa INTEGER REFERENCES pessoa NOT NULL, 
    pk_curso INTEGER REFERENCES curso NOT NULL,
    pk_turma INTEGER REFERENCES turma NOT NULL
);

CREATE TABLE sala(
    pk_sala INTEGER PRIMARY KEY NOT NULL,
    nome_sala VARCHAR(100) NOT NULL,
    capacidade INTEGER NOT NULL
);

CREATE TABLE disciplina(
    pk_disciplina INTEGER PRIMARY KEY NOT NULL,
    nome_disciplina VARCHAR(100) NOT NULL,
    pk_professor INTEGER REFERENCES pessoa NOT NULL,
    pk_sala INTEGER REFERENCES sala NOT NULL
);

CREATE TABLE curso_disciplina(
    pk_curso_disciplina INTEGER PRIMARY KEY NOT NULL,
    pk_curso INTEGER REFERENCES curso NOT NULL,
    pk_disciplina REFERENCES disciplina NOT NULL
);

CREATE TABLE comodidade(
    pk_comodidade INTEGER PRIMARY KEY NOT NULL,
    nome_comodidade VARCHAR(100) NOT NULL
);

CREATE TABLE comodidade_sala(
    pk_comodidade_sala INTEGER PRIMARY KEY NOT NULL,
    pk_comodidade INTEGER REFERENCES comodidade NOT NULL,
    pk_sala INTEGER REFERENCES sala NOT NULL
);