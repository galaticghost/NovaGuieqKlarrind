CREATE TABLE pacote(
    pk_pacote INTEGER PRIMARY KEY NOT NULL,
    dias INTEGER CHECK(dias > 0) NOT NULL,
    destino TEXT
);

CREATE TABLE saida(
    pk_saida INTEGER PRIMARY KEY NOT NULL,
    pk_pacote INTEGER REFERENCES pacote NOT NULL,
    preco NUMERIC CHECK(preco > 0) NOT NULL,
    data DATE NOT NULL
);

CREATE TABLE cliente(
    pk_cliente INTEGER PRIMARY KEY NOT NULL,
    nome_cliente VARCHAR(100) NOT NULL
);

CREATE TABLE leads(
    pk_cliente INTEGER REFERENCES cliente NOT NULL,
    faixa_etaria VARCHAR(20) NOT NULL,
    poder_aquisitivo VARCHAR(50) NOT NULL,
    composicao_familiar VARCHAR(100) NOT NULL
);

CREATE TABLE cliente_saida(
    pk_cliente_saida INTEGER PRIMARY KEY NOT NULL,
    pk_cliente INTEGER REFERENCES cliente NOT NULL,
    pk_saida INTEGER REFERENCES saida NOT NULL
);