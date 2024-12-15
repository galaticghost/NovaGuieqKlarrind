INSERT INTO pacote(dias, destino) VALUES 
(5, 'Punta Cana, República Dominicana'),
(7, 'Cancún, México'),
(6, 'Jamaica'),
(8, 'Bahamas'),
(4, 'Cuba'),
(10, 'Aruba'),
(5, 'Saint Lucia'),
(7, 'Barbados'),
(6, 'Antígua e Barbuda'),
(8, 'São Martinho'),
(5, 'Turks e Caicos'),
(9, 'Porto Rico'),
(7, 'Cayman Islands'),
(10, 'Dominica'),
(6, 'Grenada');

INSERT INTO saida(pk_pacote, preco, data) VALUES 
(1, 1500.00, '2024-05-10'),
(2, 2000.00, '2024-05-12'),
(3, 1800.00, '2024-05-15'),
(4, 2200.00, '2024-06-01'),
(5, 1600.00, '2024-06-05'),
(6, 2500.00, '2024-06-10'),
(7, 1700.00, '2024-06-15'),
(8, 2100.00, '2024-07-01'),
(9, 1400.00, '2024-07-05'),
(10, 3000.00, '2024-07-10'),
(11, 1900.00, '2024-07-15'),
(12, 2600.00, '2024-08-01'),
(13, 2300.00, '2024-08-05'),
(14, 1750.00, '2024-08-10'),
(15, 1550.00, '2024-09-01');

INSERT INTO cliente(nome_cliente) VALUES 
('Ana Beatriz'),
('Carlos Eduardo'),
('Mariana Silva'),
('Felipe Costa'),
('Juliana Almeida'),
('Lucas Martins'),
('Tatiane Pires'),
('Rafael Mendes'),
('Fernanda Lima'),
('Gabriela Rocha'),
('Thiago Oliveira'),
('Isabela Ferreira'),
('Eduardo Souza'),
('Roberta Dias'),
('Daniela Nunes');


INSERT INTO leads(pk_cliente, faixa_etaria, poder_aquisitivo, composicao_familiar) VALUES 
(1, '18-24', 'Baixo', 'Sozinho'),
(2, '25-34', 'Médio', 'Casado'),
(3, '35-44', 'Alto', 'Casado com filhos'),
(4, '45-54', 'Médio', 'Sozinho'),
(5, '55-64', 'Alto', 'Casado'),
(6, '18-24', 'Baixo', 'Filhos adultos'),
(7, '25-34', 'Médio', 'Casado com filhos'),
(8, '35-44', 'Alto', 'Sozinho'),
(9, '45-54', 'Baixo', 'Casado'),
(10, '55-64', 'Médio', 'Sozinho'),
(11, '18-24', 'Alto', 'Filhos'),
(12, '25-34', 'Médio', 'Casado com filhos'),
(13, '35-44', 'Baixo', 'Sozinho'),
(14, '45-54', 'Alto', 'Casado'),
(15, '55-64', 'Médio', 'Filhos adultos');

INSERT INTO cliente_saida(pk_cliente, pk_saida) VALUES 
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 6),
(4, 7),
(4, 8),
(5, 9),
(5, 10),
(6, 11),
(6, 12),
(7, 13),
(7, 14),
(8, 15);

SELECT * FROM pacote;
SELECT * FROM saida;
SELECT * FROM cliente;
SELECT * FROM leads;
SELECT * FROM cliente_saida;