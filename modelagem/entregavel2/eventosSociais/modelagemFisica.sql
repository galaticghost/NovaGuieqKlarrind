CREATE TABLE administrador(
    pk_administrador INTEGER PRIMARY KEY NOT NULL,
    email VARCHAR(200) NOT NULL,
    senha VARCHAR(100) NOT NULL
);


CREATE TABLE evento(
    pk_evento INTEGER PRIMARY KEY NOT NULL,
    data DATE NOT NULL,
    local TEXT NOT NULL,
    lista_categorias TEXT NOT NULL,
    pk_administrador REFERENCES administrador NOT NULL
);

CREATE TABLE cliente(
    pk_cliente INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    genero VARCHAR(2) NOT NULL,
    idade INTEGER CHECK (idade >= 0) NOT NULL,
    endereco TEXT NOT NULL
);

CREATE TABLE cliente_evento(
    pk_cliente_evento INTEGER PRIMARY KEY NOT NULL,
    pk_cliente REFERENCES cliente NOT NULL,
    pk_evento REFERENCES evento NOT NULL
);