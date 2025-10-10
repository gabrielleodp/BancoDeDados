CREATE TABLE usuarios (
    id_usuario NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    email VARCHAR2(100) NOT NULL
);

CREATE TABLE tarefas (
    id_tarefa NUMBER PRIMARY KEY,
    titulo VARCHAR2(100) NOT NULL,
    descricao VARCHAR2(255),
    status VARCHAR2(50),
    responsavel NUMBER,
    CONSTRAINT fk_responsavel FOREIGN KEY (responsavel) REFERENCES usuarios(id_usuario)
);


