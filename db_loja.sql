CREATE DATABASE loja_do_seu_ze;

USE loja_do_seu_ze;

CREATE TABLE clientes ( 
	cli_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    cli_nome VARCHAR(50) NOT NULL,
    cli_email VARCHAR(50) NOT NULL,
    cli_telefone VARCHAR(14) NOT NULL
);

CREATE TABLE produtos(
	pro_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    pro_nome VARCHAR(50) NOT NULL,
    pro_descricao VARCHAR(50) NOT NULL,
    pro_preco FLOAT NOT NULL
);

CREATE TABLE pedidos(
	ped_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    cli_id_cli INT NOT NULL,
    pro_id_prod INT NOT NULL,
    ped_data DATE NOT NULL,
    FOREIGN KEY (pro_id_prod) REFERENCES produtos(pro_id),
    FOREIGN KEY (cli_id_cli) REFERENCES clientes(cli_id)
);