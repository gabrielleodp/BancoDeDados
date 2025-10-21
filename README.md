# Projeto Banco de Dados – Sistema de Gerenciamento de Tarefas

## Descrição
Este projeto é um sistema de gerenciamento de tarefas e usuários, desenvolvido como atividade acadêmica da disciplina de Banco de Dados.
O sistema foi implementado em Python com banco de dados Oracle, utilizando o padrão MVC (Model-View-Controller) e integrando consultas SQL relacionais com operações CRUD (criar, ler, atualizar e excluir).

O sistema exibe uma tela inicial (splash screen), realiza a verificação de tabelas, contagem de registros, e oferece menus interativos para gerenciamento de dados e relatórios.

## Estrutura do Projeto
- `src/`
  - `controller/` → classes responsáveis pelo CRUD das entidades
  - 'controller_usuario.py'
│ └── controller_tarefa.py
  - `model/` → classes que representam as entidades do sistema (Usuario, Tarefa)
│ ├── usuario.py
│ └── tarefa.py
  - `utils/` → utilitários e configuração do sistema
│ ├── splash_screen.py
│ └── config.py
└── main.py
- `sql/` → scripts SQL de criação de tabelas e inserção de dados
└── script.sql
- `diagrams/` → diagramas do banco de dados
└── diagrama_relacional.png

---

## Tecnologias Utilizadas

- Python 3.10+
- Oracle Database XE
- SQL
- Biblioteca `cx_Oracle` para integração entre Python e Oracle

---

## Funcionalidades Principais

### Usuários
- Inserir usuário  
- Atualizar usuário  
- Excluir usuário (com verificação de integridade)  
- Listar usuários  

### Tarefas
- Inserir tarefa  
- Atualizar tarefa  
- Excluir tarefa  
- Listar tarefas  

### Relatórios
- **Relatório de Tarefas por Usuário (GROUP BY)** – mostra o nome do usuário e o total de tarefas associadas.  
- **Relatório Detalhado de Tarefas (JOIN)** – mostra ID, título, descrição, status e nome do usuário responsável.  

---

## Contagem de Registros

Ao iniciar o sistema, são exibidos:
- O total de **usuários cadastrados**  
- O total de **tarefas cadastradas**

## Como Executar:

Requisitos:
- Python
- Oracle
- Intalar a biblioteca necessária: pip install cx_Oracle


## Configurar Conexão

No arquivo src/main.py, atualize conforme o seu ambiente Oracle:
- dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
- conn = cx_Oracle.connect(user="system", password="admin", dsn=dsn)

## Executar o Sistema

No terminal, dentro da pasta do projeto, execute:
- python src/main.py

O sistema exibirá a splash screen, verificará as tabelas existentes e mostrará a quantidade de registros antes de abrir o menu principal.

## Grupo
- Adrielly Costa
- Gabrielle Oliveira de Paula
- Luísa Vernersbach Varejão


**Professor:** Howard
**Disciplina:** Banco de Dados  
**Semestre:** 2025/2
