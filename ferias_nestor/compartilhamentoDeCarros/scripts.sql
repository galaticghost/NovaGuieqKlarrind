INSERT INTO bairro(nome_bairro) VALUES 
('Centro'),
('Jardim das Flores'),
('Vila Nova'),
('Bairro Alto'),
('São Pedro'),
('Alto da Boa Vista'),
('Jardim América'),
('Bela Vista'),
('Parque São Jorge'),
('Vila Mariana'),
('Morumbi'),
('Grajaú'),
('Pirituba'),
('Jardim São Paulo'),
('Ipanema');


INSERT INTO carro(pk_bairro, modelo, combustivel, disponibilidade) VALUES 
(1, 'Fusca', 40.5, '08:00, 18:00'),
(2, 'Civic', 50.0, '09:30, 19:30'),
(3, 'Fiesta', 30.2, '10:15, 20:15'),
(4, 'Corolla', 45.0, '11:00, 21:00'),
(5, 'Uno', 25.7, '13:30, 22:30'),
(6, 'HB20', 60.0, '14:45, 23:45'),
(7, 'Gol', 35.3, '15:00, 21:00'),
(8, 'Sandero', 55.0, '16:15, 20:30'),
(9, 'Kwid', 20.5, '17:30, 22:00'),
(10, 'Tracker', 75.0, '18:00, 21:45'),
(11, 'Tiguan', 80.0, '09:00, 18:30'),
(12, 'Renegade', 65.0, '12:00, 19:00'),
(13, 'Jetta', 42.3, '10:45, 20:45'),
(14, 'A3', 48.0, '11:30, 21:30'),
(15, 'Onix', 38.9, '14:00, 22:00');

INSERT INTO cliente(nome_cliente, endereco, cnh) VALUES 
('Ana Silva', 'Rua A, 123, Centro', '12345678900'),
('João Souza', 'Avenida B, 456, Jardim das Flores', '23456789001'),
('Maria Oliveira', 'Travessa C, 789, Vila Nova', '34567890102'),
('Pedro Santos', 'Rua D, 321, Bairro Alto', '45678901203'),
('Lucas Lima', 'Avenida E, 654, São Pedro', '56789012304'),
('Julia Costa', 'Rua F, 987, Alto da Boa Vista', '67890123405'),
('Mariana Ferreira', 'Rua G, 159, Jardim América', '78901234506'),
('Thiago Almeida', 'Avenida H, 753, Bela Vista', '89012345607'),
('Fernanda Rocha', 'Travessa I, 852, Parque São Jorge', '90123456708'),
('Rafael Mendes', 'Rua J, 963, Vila Mariana', '01234567809'),
('Tatiane Pires', 'Avenida K, 147, Morumbi', '12345678010'),
('Carlos Santos', 'Rua L, 258, Grajaú', '23456789011'),
('Gabriela Martins', 'Travessa M, 369, Pirituba', '34567890112'),
('Eduardo Pereira', 'Rua N, 456, Jardim São Paulo', '45678901213'),
('Isabela Almeida', 'Avenida O, 789, Ipanema', '56789012314');

INSERT INTO carro_cliente(pk_carro, pk_cliente, horas) VALUES 
(1, 1, 2),
(2, 2, 3),
(3, 3, 1),
(4, 4, 5),
(5, 5, 4),
(6, 6, 2),
(7, 7, 3),
(8, 8, 1),
(9, 9, 6),
(10, 10, 4),
(11, 11, 2),
(12, 12, 3),
(13, 13, 5),
(14, 14, 4),
(15, 15, 2);

SELECT * FROM bairro;
SELECT * FROM carro;
SELECT * FROM cliente;
SELECT * FROM carro_cliente;