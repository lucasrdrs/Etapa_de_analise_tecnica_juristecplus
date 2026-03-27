CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    estado VARCHAR(2) NOT NULL
);

CREATE TABLE processos (
    id_processo SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    assunto VARCHAR(150),
    data_abertura DATE NOT NULL,
    
CONSTRAINT fk_cliente 
    FOREIGN KEY (id_cliente) 
    REFERENCES clientes(id_cliente)
    ON DELETE CASCADE
);

INSERT INTO clientes (nome, estado) VALUES
('Luan', 'RJ'),
('Joao', 'SP');

INSERT INTO processos (id_cliente, assunto, data_abertura) VALUES
(1, 'Trabalhista', '2023-05-15'),
(2, 'Tributário', '2023-08-10'),
(2, 'Ambiental', '2024-01-10');

SELECT * FROM "clientes"
SELECT * FROM "processos"

SELECT 
    c.nome, 
    p.assunto, 
    p.data_abertura
FROM clientes c
INNER JOIN processos p ON c.id_cliente = p.id_cliente
WHERE c.estado = 'SP' 
  AND p.data_abertura BETWEEN '2023-01-01' AND '2023-12-31';