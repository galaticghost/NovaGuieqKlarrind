CREATE TABLE
    restaurante (
        restaurante_id NUMBER PRIMARY KEY NOT NULL,
        nome VARCHAR2 (100) NOT NULL,
        comissao NUMBER CHECK (comissao >= 0) NOT NULL,
        email_restaurante VARCHAR2 (200) NOT NULL,
        senha_restaurante VARCHAR2 (100) NOT NULL,
        criacao DATE DEFAULT CURRENT_TIMESTAMP NOT NULL,
        ultima_atualizacao DATE DEFAULT CURRENT_TIMESTAMP,
        tem_produtos INTEGER DEFAULT 0
    );

CREATE TABLE -- Res é de restaurante, já tinha tabela produto da pesquisa
    res_produto (
        produto_id NUMBER PRIMARY KEY,
        nome VARCHAR2 (100) NOT NULL,
        preco NUMBER CHECK (preco > 0) NOT NULL,
        restaurante_id INTEGER REFERENCES restaurante NOT NULL,
        estoque NUMBER default 50
    );

CREATE TABLE
    usuario (
        usuario_id NUMBER PRIMARY KEY NOT NULL,
        nome VARCHAR2 (200) NOT NULL,
        email VARCHAR2 (200) NOT NULL,
        senha VARCHAR2 (100) NOT NULL,
        criacao DATE DEFAULT CURRENT_TIMESTAMP,
        ultima_atualizacao DATE DEFAULT CURRENT_TIMESTAMP,
        admin NUMBER DEFAULT 0 NOT NULL,
        ativo INTEGER DEFAULT 0 NOT NULL
    );

CREATE TABLE
    venda (
        venda NUMBER PRIMARY KEY NOT NULL,
        valor NUMERIC CHECK (valor > 0) NOT NULL,
        usuario_id NUMBER REFERENCES usuario NOT NULL,
        restaurante_id NUMBER REFERENCES restaurante NOT NULL,
        criacao DATE DEFAULT CURRENT_TIMESTAMP,
        status VARCHAR2 (50) DEFAULT 'criado'
    );

CREATE TABLE
    venda_produto (
        venda_produto_id NUMBER PRIMARY KEY NOT NULL,
        venda_id NUMBER REFERENCES venda NOT NULL,
        produto_id NUMBER REFERENCES res_produto NOT NULL,
        quantidade NUMBER NOT NULL,
        valor_total NUMBER CHECK (valor_total > 0) NOT NULL
    );

INSERT INTO
    restaurante (
        restaurante_id,
        nome,
        comissao,
        email_restaurante,
        senha_restaurante,
        criacao,
        ultima_atualizacao,
        tem_produtos
    )
VALUES
    (
        2,
        'Comidas Chinesas',
        35,
        'xijiping@alipay.cn',
        '3a1200279b514ca4409dd8136527046a',
        TO_DATE ('2024-11-13 08:44:35', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-13 08:44:44', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    restaurante
VALUES
    (
        3,
        'Caduzinho Foods',
        32,
        'cadu@gmail.com',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-13 08:55:00', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-26 08:13:15', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    restaurante
VALUES
    (
        4,
        'Jão Lauro Carnes Veganas',
        26,
        'jaolauro@carne.com.br',
        '0ba0dd14265fced34a1202aeced9f02d',
        TO_DATE ('2024-11-13 08:56:34', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-13 08:56:43', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    restaurante
VALUES
    (
        5,
        'Restaurante não aguento mais',
        2,
        'ca@du.com',
        '8b45d551498d78d0123dd0f635f6d89b',
        TO_DATE ('2024-11-13 08:57:52', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-13 08:57:56', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    restaurante
VALUES
    (
        6,
        'Restaurante sem produtos',
        0,
        'restaurante@gmail.com',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-13 08:58:37', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-13 08:58:43', 'YYYY-MM-DD HH24:MI:SS'),
        0
    );

INSERT INTO
    restaurante
VALUES
    (
        7,
        'Zeca Lanches',
        69,
        'zecalanches@gmail.com',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-25 11:01:41', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-25 11:01:48', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    restaurante
VALUES
    (
        8,
        'BurgasBrownie',
        23,
        'burgasbrownie@gmail.com',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-25 11:03:16', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-25 11:03:21', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    restaurante
VALUES
    (
        9,
        'Brohas Sushi',
        43,
        'brohassushi@gmail.com',
        '3a1200279b514ca4409dd8136527046a',
        TO_DATE ('2024-11-25 11:05:57', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-25 11:06:03', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    restaurante
VALUES
    (
        10,
        'Clinica H. Romeu',
        0,
        'hromeu@hotmail.com',
        '030ea7a3f57f399ecc51def9f1e44e02',
        TO_DATE ('2024-11-25 11:09:56', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-25 11:10:26', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    restaurante
VALUES
    (
        11,
        'Shaxcrimetus SHaslVogus',
        13,
        'maranax@infernux.bl',
        '35aa44097c4da581cc04cb7f843ca9c1',
        TO_DATE ('2024-11-25 11:12:41', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-25 11:12:50', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    restaurante
VALUES
    (
        12,
        'Restaurante com muitos produtos',
        5,
        'res@pro.co',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-25 11:14:11', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-25 11:14:11', 'YYYY-MM-DD HH24:MI:SS'),
        0
    );

INSERT INTO
    restaurante
VALUES
    (
        13,
        'Ratoeira do JE',
        35,
        'joaoeduardo@yahoo.com.br',
        '8b9763252f53b9ce24c3dc04c1caacf0',
        TO_DATE ('2024-11-26 07:57:11', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-26 07:57:29', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    restaurante
VALUES
    (
        14,
        'Linguiças do Jeremias',
        45,
        'jeremias@gmail.com',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-26 07:58:27', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-26 07:58:32', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    restaurante
VALUES
    (
        15,
        'Churrasco do Ricardão',
        41,
        'ricardo@hotmail.com',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-26 07:59:31', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-26 07:59:57', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (1, 'Comida mexicana', 35, 2);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (2, 'Sopa de gelo', 32, 2);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (3, 'Cadu ao sugo', 30, 3);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (4, 'Agua com gas', 50, 3);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (5, 'agua sem gas', 2, 3);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (6, 'Massa com terra', 25, 3);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (7, 'A la hora', 100, 3);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (8, 'Carne vegana', 50, 4);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (9, 'Carne', 49, 4);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (10, 'vegana', 1, 4);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (11, 'Sopa de gelo', 40, 5);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (12, 'Pedra com terra', 30, 5);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (13, 'Um vírus', 10, 5);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (14, 'Molho do Zeca', 40, 7);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (15, 'Especial do zeca de dias das mães', 24, 7);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (16, 'Podrão', 2, 7);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (17, 'agua sem gas', 3, 7);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (18, 'cachorro quente', 12, 7);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (19, 'batata frita', 20, 7);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (20, 'Brownie burguer clássico', 10.5, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (21, 'Brownie burguer de nutella', 12, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (22, 'Brownie burguer de chocolate belga', 11, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (23, 'Brownie burguer de doce de leite', 11.5, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (24, 'Brownie burguer de paçoca', 11.5, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (25, 'Brownie burguer de oreo', 11.75, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (26, 'Brownie burguer de ovomaltine', 11, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (27, 'Brownie burguer de flocos', 11, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (28, 'Brownie burguer de baunilha', 10.5, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (29, 'Brownie burguer de morango', 11, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (30, 'Brownie burguer de pistache', 11, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (31, 'Brownie burguer de cookies', 11.5, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (32, 'agua com gas', 3.5, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (33, 'agua sem gas', 3.5, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (34, 'refil um litro', 6, 8);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (35, 'Hossomaki de terra', 10, 9);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (36, 'niguiri de pedra', 12, 9);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (37, 'um salmao cru inteiro', 85, 9);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (38, 'shoyu cem ml', 100, 9);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (39, 'hossomaki de rocha', 4, 9);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (40, 'uramaki de terra', 34, 9);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (41, 'um hossomaki normal', 10, 9);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (42, 'Sangue o positivo', 40, 10);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (44, 'Tipo o negativo', 27, 10);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (45, 'Tipo O negativo', 37, 10);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (46, 'Yakisoba de alho', 560, 10);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (47, 'geroxe cruo', 6, 11);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (48, 'maranax pallex', 6, 11);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (49, 'crudux cruo', 6, 11);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (50, 'Queijo', 20, 13);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (51, 'queijo mofado', 50, 13);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (52, 'Chorume', 10, 13);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (53, 'Linguiça pequena', 8, 14);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (54, 'Linguiça média', 15, 14);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (55, 'Linguiça grande', 23, 14);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (56, 'Linguição', 30, 14);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (57, 'Linguição', 30, 15);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (58, 'Picanha', 20, 15);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (59, 'Varão', 40, 15);

INSERT INTO
    res_produto (produto_id, nome, preco, restaurante_id)
VALUES
    (60, 'Pescoção', 40, 15);

INSERT INTO
    usuario (
        usuario_id,
        nome,
        email,
        senha,
        criacao,
        ultima_atualizacao,
        admin
    )
VALUES
    (
        1,
        'Theo Bola Cunha',
        'bola@gmail.com',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-13 09:42:47', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-21 10:33:16', 'YYYY-MM-DD HH24:MI:SS'),
        0
    );

INSERT INTO
    usuario (
        usuario_id,
        nome,
        email,
        senha,
        criacao,
        ultima_atualizacao,
        admin
    )
VALUES
    (
        2,
        'Carlos Dias',
        'cadu@cadu.com',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-16 17:49:51', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-21 09:11:26', 'YYYY-MM-DD HH24:MI:SS'),
        0
    );

INSERT INTO
    usuario (
        usuario_id,
        nome,
        email,
        senha,
        criacao,
        ultima_atualizacao,
        admin
    )
VALUES
    (
        3,
        'Jão Lauro',
        'joaolauro@gmail.com',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-19 09:09:07', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-26 08:27:49', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    usuario (
        usuario_id,
        nome,
        email,
        senha,
        criacao,
        ultima_atualizacao,
        admin
    )
VALUES
    (
        5,
        'admin',
        'admin@androidfood.com',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-25 11:00:15', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-25 11:00:15', 'YYYY-MM-DD HH24:MI:SS'),
        1
    );

INSERT INTO
    usuario (
        usuario_id,
        nome,
        email,
        senha,
        criacao,
        ultima_atualizacao,
        admin
    )
VALUES
    (
        9,
        'Mestor Yiliotto Talamon',
        'mestor@gmail.com',
        '4c9f82895cc9ea0c86c7ba5f3372a25a',
        TO_DATE ('2024-11-25 11:16:26', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-25 11:16:34', 'YYYY-MM-DD HH24:MI:SS'),
        0
    );

INSERT INTO
    usuario (
        usuario_id,
        nome,
        email,
        senha,
        criacao,
        ultima_atualizacao,
        admin
    )
VALUES
    (
        10,
        'Joaozinho Um Dois Tres',
        'joaozinho@youtube.com',
        '274672838a8002344fed81ca1228bf05',
        TO_DATE ('2024-11-26 08:00:53', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-26 08:01:02', 'YYYY-MM-DD HH24:MI:SS'),
        0
    );

INSERT INTO
    usuario (
        usuario_id,
        nome,
        email,
        senha,
        criacao,
        ultima_atualizacao,
        admin
    )
VALUES
    (
        11,
        'Xi Jinping China',
        'xijiping@alibaba.cn',
        '5f414d0e802b620c988d6acca4d80301',
        TO_DATE ('2024-11-26 08:03:39', 'YYYY-MM-DD HH24:MI:SS'),
        TO_DATE ('2024-11-26 08:03:51', 'YYYY-MM-DD HH24:MI:SS'),
        0
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        1,
        306,
        1,
        2,
        TO_DATE ('2024-11-13 09:43:05', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        2,
        100,
        1,
        4,
        TO_DATE ('2024-11-13 09:51:18', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        3,
        250,
        1,
        3,
        TO_DATE ('2024-11-13 09:59:35', 'YYYY-MM-DD HH24:MI:SS'),
        'entregue'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        4,
        360,
        1,
        3,
        TO_DATE ('2024-11-14 09:01:22', 'YYYY-MM-DD HH24:MI:SS'),
        'entregue'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        6,
        310,
        1,
        3,
        TO_DATE ('2024-11-14 10:48:49', 'YYYY-MM-DD HH24:MI:SS'),
        'entregue'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        7,
        150,
        1,
        3,
        TO_DATE ('2024-11-14 10:54:52', 'YYYY-MM-DD HH24:MI:SS'),
        'entregue'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        8,
        228,
        2,
        3,
        TO_DATE ('2024-11-16 17:50:14', 'YYYY-MM-DD HH24:MI:SS'),
        'entregue'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        9,
        170,
        2,
        5,
        TO_DATE ('2024-11-21 09:11:33', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        10,
        1496,
        2,
        2,
        TO_DATE ('2024-11-21 09:11:40', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        11,
        90,
        2,
        5,
        TO_DATE ('2024-11-21 09:11:46', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        12,
        296,
        2,
        4,
        TO_DATE ('2024-11-21 09:12:03', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        13,
        268,
        2,
        3,
        TO_DATE ('2024-11-21 09:12:29', 'YYYY-MM-DD HH24:MI:SS'),
        'rejeitado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        14,
        150,
        2,
        3,
        TO_DATE ('2024-11-21 09:12:33', 'YYYY-MM-DD HH24:MI:SS'),
        'aceito'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        15,
        250,
        2,
        3,
        TO_DATE ('2024-11-21 09:12:40', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        16,
        18,
        2,
        3,
        TO_DATE ('2024-11-21 09:12:45', 'YYYY-MM-DD HH24:MI:SS'),
        'entregue'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        17,
        1600,
        1,
        2,
        TO_DATE ('2024-11-21 10:33:20', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        18,
        2605,
        9,
        7,
        TO_DATE ('2024-11-25 11:16:52', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        19,
        100002,
        9,
        3,
        TO_DATE ('2024-11-25 11:17:07', 'YYYY-MM-DD HH24:MI:SS'),
        'rejeitado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        20,
        29.5,
        9,
        8,
        TO_DATE ('2024-11-25 11:17:20', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        21,
        51,
        9,
        4,
        TO_DATE ('2024-11-25 11:17:32', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        22,
        560,
        9,
        10,
        TO_DATE ('2024-11-25 11:17:39', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        23,
        64,
        9,
        2,
        TO_DATE ('2024-11-25 11:17:46', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        24,
        108,
        9,
        11,
        TO_DATE ('2024-11-25 11:17:59', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        25,
        20,
        9,
        5,
        TO_DATE ('2024-11-25 11:18:16', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        26,
        30,
        9,
        3,
        TO_DATE ('2024-11-25 11:18:44', 'YYYY-MM-DD HH24:MI:SS'),
        'saiu para a entrega'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        27,
        105,
        10,
        9,
        TO_DATE ('2024-11-26 08:01:15', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        28,
        50,
        10,
        13,
        TO_DATE ('2024-11-26 08:01:25', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        29,
        2078,
        10,
        14,
        TO_DATE ('2024-11-26 08:01:51', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        30,
        21,
        10,
        8,
        TO_DATE ('2024-11-26 08:02:22', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        31,
        120,
        10,
        15,
        TO_DATE ('2024-11-26 08:02:37', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        32,
        74,
        11,
        10,
        TO_DATE ('2024-11-26 08:04:18', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        33,
        14.5,
        11,
        8,
        TO_DATE ('2024-11-26 08:04:29', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        34,
        1080,
        11,
        9,
        TO_DATE ('2024-11-26 08:04:40', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        35,
        88,
        11,
        7,
        TO_DATE ('2024-11-26 08:04:57', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        36,
        108,
        11,
        11,
        TO_DATE ('2024-11-26 08:05:10', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        37,
        102,
        11,
        2,
        TO_DATE ('2024-11-26 08:05:17', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda (
        venda_id,
        valor,
        usuario_id,
        restaurante_id,
        criacao,
        status
    )
VALUES
    (
        38,
        100,
        11,
        4,
        TO_DATE ('2024-11-26 08:05:26', 'YYYY-MM-DD HH24:MI:SS'),
        'criado'
    );

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (1, 1, 1, 6, 210);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (2, 1, 2, 3, 96);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (3, 2, 8, 2, 100);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (4, 3, 3, 5, 150);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (5, 3, 4, 2, 100);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (6, 4, 7, 3, 300);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (7, 4, 3, 2, 60);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (11, 6, 4, 5, 250);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (12, 6, 3, 2, 60);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (13, 7, 4, 3, 150);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (14, 8, 5, 4, 8);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (15, 8, 3, 4, 120);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (16, 8, 6, 4, 100);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (17, 9, 11, 2, 80);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (18, 9, 12, 3, 90);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (19, 10, 1, 40, 1400);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (20, 10, 2, 3, 96);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (21, 11, 12, 3, 90);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (22, 12, 8, 1, 50);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (23, 12, 9, 4, 196);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (24, 12, 10, 50, 50);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (25, 13, 6, 2, 50);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (26, 13, 3, 2, 60);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (27, 13, 4, 3, 150);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (28, 13, 5, 4, 8);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (29, 14, 4, 3, 150);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (30, 15, 4, 5, 250);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (31, 16, 5, 9, 18);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (32, 17, 2, 50, 1600);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (33, 18, 14, 60, 2400);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (34, 18, 16, 4, 8);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (35, 18, 17, 59, 177);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (36, 18, 19, 1, 20);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (37, 19, 7, 1000, 100000);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (38, 19, 5, 1, 2);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (39, 20, 34, 1, 6);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (40, 20, 25, 2, 23.5);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (41, 21, 10, 1, 1);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (42, 21, 8, 1, 50);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (43, 22, 46, 1, 560);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (44, 23, 2, 2, 64);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (45, 24, 49, 6, 36);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (46, 24, 48, 6, 36);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (47, 24, 47, 6, 36);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (48, 25, 13, 2, 20);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (49, 26, 3, 1, 30);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (50, 27, 35, 2, 20);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (51, 27, 37, 1, 85);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (52, 28, 52, 3, 30);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (53, 28, 50, 1, 20);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (54, 29, 56, 69, 2070);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (55, 29, 53, 1, 8);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (56, 30, 28, 2, 21);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (57, 31, 60, 1, 40);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (58, 31, 59, 1, 40);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (59, 31, 58, 2, 40);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (60, 32, 45, 2, 74);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (61, 33, 32, 1, 3.5);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (62, 33, 26, 1, 11);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (63, 34, 40, 2, 68);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (64, 34, 39, 3, 12);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (65, 34, 38, 10, 1000);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (66, 35, 14, 1, 40);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (67, 35, 15, 2, 48);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (68, 36, 47, 6, 36);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (69, 36, 48, 6, 36);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (70, 36, 49, 6, 36);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (71, 37, 1, 2, 70);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (72, 37, 2, 1, 32);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (73, 38, 10, 50, 50);

INSERT INTO
    venda_produto (
        venda_produto_id,
        venda_id,
        produto_id,
        quantidade,
        valor_total
    )
VALUES
    (74, 38, 8, 1, 50);