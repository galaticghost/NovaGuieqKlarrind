CREATE TABLE bairro(
    pk_bairro INTEGER PRIMARY KEY NOT NULL,
    nome_bairro VARCHAR(100) NOT NULL
);

CREATE TABLE carro(
    pk_carro INTEGER PRIMARY KEY NOT NULL,
    pk_bairro INTEGER REFERENCES bairro NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    combustivel NUMERIC CHECK(combustivel >= 0) NOT NULL,
    disponibilidade VARCHAR(100) NOT NULL
);

CREATE TABLE cliente(
    pk_cliente INTEGER PRIMARY KEY NOT NULL,
    nome_cliente VARCHAR(100) NOT NULL,
    endereco TEXT NOT NULL,
    cnh VARCHAR(30) NOT NULL
);

CREATE TABLE carro_cliente(
    pk_carro_cliente INTEGER PRIMARY KEY NOT NULL,
    pk_carro INTEGER REFERENCES carro NOT NULL,
    pk_cliente INTEGER REFERENCES cliente NOT NULL,
    horas INTEGER CHECK(horas >= 0) NOT NULL
);









