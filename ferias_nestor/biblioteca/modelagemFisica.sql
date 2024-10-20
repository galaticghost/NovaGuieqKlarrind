CREATE TABLE autor(
    pk_autor INTEGER PRIMARY KEY NOT NULL,
    nome_autor VARCHAR(200) NOT NULL
);

CREATE TABLE livro(
    pk_livro INTEGER PRIMARY KEY NOT NULL,
    isbn VARCHAR(20) NOT NULL UNIQUE,
    nome_livro VARCHAR(100) NOT NULL,
    genero VARCHAR(100) NOT NULL,
    status BOOLEAN DEFAULT 0 NOT NULL
);

CREATE TABLE autor_livro(
    pk_autor_livro INTEGER PRIMARY KEY NOT NULL,
    pk_autor INTEGER REFERENCES autor NOT NULL,
    pk_livro INTEGER REFERENCES livro NOT NULL
);

CREATE TABLE usuario(
    pk_usuario INTEGER PRIMARY KEY NOT NULL,
    nome_usuario VARCHAR(200) NOT NULL,
    data_nascimento DATE NOT NULL
);

CREATE TABLE interesse(
    pk_interesse INTEGER PRIMARY KEY NOT NULL,
    interesse VARCHAR(100) NOT NULL
);

CREATE TABLE usuario_interesse(
    pk_usuario_interesse INTEGER PRIMARY KEY NOT NULL,
    pk_usuario INTEGER REFERENCES usuario NOT NULL,
    pk_interesse INTEGER REFERENCES interesse NOT NULL
);

CREATE TABLE emprestimo(
    pk_emprestimo INTEGER PRIMARY KEY NOT NULL,
    pk_usuario INTEGER REFERENCES usuario NOT NULL,
    pk_livro INTEGER REFERENCES livro NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_vencimento DATE NOT NULL
);