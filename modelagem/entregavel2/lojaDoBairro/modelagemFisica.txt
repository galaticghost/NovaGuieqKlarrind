CREATE TABLE cliente(
    pk_cliente INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(14) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    endereco TEXT NOT NULL
);

CREATE TABLE fornecedor(
    pk_fornecedor INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cnpj VARCHAR(30) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    endereco TEXT NOT NULL
);

CREATE TABLE produto(
    pk_produto INTEGER PRIMARY KEY NOT NULL,
    pk_fornecedor REFERENCES fornecedor NOT NULL,
    nome VARCHAR(100) NOT NULL,
    prateleira VARCHAR(30) NOT NULL,
    quantidade INTEGER CHECK(quantidade >= 0) NOT NULL,
    preco NUMERIC CHECK(preco >= 0) NOT NULL
);

CREATE TABLE venda(
    pk_venda INTEGER PRIMARY KEY NOT NULL,
    pk_cliente REFERENCES cliente NOT NULL,
    pk_produto REFERENCES produto NOT NULL,
    quantidade INTEGER CHECK(quantidade >= 0) NOT NULL,
    valor_total NUMERIC CHECK(valor_total >= 0) NOT NULL
);