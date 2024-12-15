CREATE TABLE cliente(
    pk_cliente INTEGER PRIMARY KEY NOT NULL,
    nome_cliente VARCHAR(100) NOT NULL,
    telefone VARCHAR(30) NOT NULL,
    vegetariano BOOLEAN DEFAULT 0
);

CREATE TABLE produto(
    pk_produto INTEGER PRIMARY KEY NOT NULL,
    nome_produto VARCHAR(100) NOT NULL,
    quantidade INTEGER NOT NULL,
    vencimento DATE NOT NULL
);

CREATE TABLE fornecedor(
    pk_fornecedor INTEGER PRIMARY KEY NOT NULL,
    nome_fornecedor VARCHAR(100) NOT NULL,
    cpf_cnpj VARCHAR(18) NOT NULL
);

CREATE TABLE lanche(
    pk_lanche INTEGER PRIMARY KEY NOT NULL,
    nome_lanche VARCHAR(100) NOT NULL,
    preco NUMERIC CHECK(preco > 0) NOT NULL
);

CREATE TABLE passo(
    pk_passo INTEGER PRIMARY KEY NOT NULL,
    numero_passo INTEGER NOT NULL,
    passo TEXT NOT NULL,
    pk_lanche INTEGER REFERENCES lanche NOT NULL
);

CREATE TABLE produto_fornecedor(
    pk_produto_fornecedor INTEGER PRIMARY KEY NOT NULL,
    pk_produto INTEGER REFERENCES produto NOT NULL,
    pk_fornecedor INTEGER REFERENCES fornecedor NOT NULL
);

CREATE TABLE produto_lanche(
    pk_produto_lanche INTEGER PRIMARY KEY NOT NULL,
    pk_produto INTEGER REFERENCES produto NOT NULL,
    pk_lanche INTEGER REFERENCES lanche NOT NULL
);