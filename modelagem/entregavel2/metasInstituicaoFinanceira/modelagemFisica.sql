CREATE TABLE funcionario(
    pk_funcionario INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    gerente BOOLEAN NOT NULL DEFAULT 0
);


CREATE TABLE metas(
    pk_metas INTEGER PRIMARY KEY NOT NULL,
    pk_funcionario REFERENCES funcionario,
    seguros_vendidos INTEGER NOT NULL,
    contas_abertas INTEGER NOT NULL,
    financiamentos INTEGER NOT NULL,
    emprestimos_realizados INTEGER NOT NULL
);