import cx_Oracle
from src.utils.splash_screen import mostrar_splash
from src.utils.config import MENUS
from src.controller.controller_usuario import ControllerUsuario
from src.controller.controller_tarefa import ControllerTarefa
from src.model.usuario import Usuario
from src.model.tarefa import Tarefa

def conectar():
    # Altere para seu usuário, senha e serviço do Oracle
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
    return cx_Oracle.connect(user="system", password="admin", dsn=dsn)

def ver_tabelas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT table_name FROM user_tables WHERE table_name IN ('USUARIOS', 'TAREFAS')")
    for row in cursor.fetchall():
        print(row[0])

# 🟢 Função nova exigida pelo edital
def contar_registros(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(1) FROM usuarios")
    total_usuarios = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(1) FROM tarefas")
    total_tarefas = cursor.fetchone()[0]
    print(f"Usuários cadastrados: {total_usuarios}")
    print(f"Tarefas cadastradas: {total_tarefas}")
    print("===================================")

def menu_usuarios(ctrl_usuario):
    while True:
        print(MENUS["usuarios"])
        op = input("Escolha: ")
        if op == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            id_usuario = int(input("ID (deixe 0 para automático): "))
            usuario = Usuario(id_usuario if id_usuario != 0 else None, nome, email)
            ctrl_usuario.inserir(usuario)
            print("Usuário inserido com sucesso!")
        elif op == "2":
            id_usuario = int(input("ID do usuário a atualizar: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            usuario = Usuario(id_usuario, nome, email)
            ctrl_usuario.atualizar(usuario)
            print("Usuário atualizado com sucesso!")
        elif op == "3":
            id_usuario = int(input("ID do usuário a excluir: "))
            ctrl_usuario.excluir(id_usuario)
            print("Usuário excluído com sucesso!")
        elif op == "4":
            usuarios = ctrl_usuario.listar()
            for u in usuarios:
                print(u)
        elif op == "0":
            break
        else:
            print("Opção inválida.")

def menu_tarefas(ctrl_tarefa):
    while True:
        print(MENUS["tarefas"])
        op = input("Escolha: ")
        if op == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            status = input("Status (PENDENTE/EM ANDAMENTO/CONCLUÍDA): ")
            id_usuario = int(input("ID do usuário responsável: "))
            id_tarefa = int(input("ID (deixe 0 para automático): "))
            tarefa = Tarefa(id_tarefa if id_tarefa != 0 else None,
                            titulo,
                            descricao,
                            status,
                            id_usuario)
            ctrl_tarefa.inserir(tarefa)
            print("Tarefa inserida com sucesso!")
        elif op == "2":
            id_tarefa = int(input("ID da tarefa a atualizar: "))
            titulo = input("Novo título: ")
            descricao = input("Nova descrição: ")
            status = input("Novo status: ")
            id_usuario = int(input("Novo ID do usuário responsável: "))
            tarefa = Tarefa(id_tarefa, titulo, descricao, status, id_usuario)
            ctrl_tarefa.atualizar(tarefa)
            print("Tarefa atualizada com sucesso!")
        elif op == "3":
            id_tarefa = int(input("ID da tarefa a excluir: "))
            ctrl_tarefa.excluir(id_tarefa)
            print("Tarefa excluída com sucesso!")
        elif op == "4":
            tarefas = ctrl_tarefa.listar()
            for t in tarefas:
                print(t)
        elif op == "0":
            break
        else:
            print("Opção inválida.")

def menu_relatorios(conn):
    while True:
        print(MENUS["relatorios"])
        op = input("Escolha: ")
        if op == "1":
            cursor = conn.cursor()
            cursor.execute("""
                SELECT u.nome, COUNT(t.id_tarefa) AS total_tarefas
                FROM usuarios u
                LEFT JOIN tarefas t ON u.id_usuario = t.usuario_tarefa
                GROUP BY u.nome
            """)
            for row in cursor.fetchall():
                print(f"Usuário: {row[0]}, Total de Tarefas: {row[1]}")
        elif op == "2":
            cursor = conn.cursor()
            cursor.execute("""
                SELECT t.id_tarefa, t.titulo, t.descricao, t.status, u.nome
                FROM tarefas t
                JOIN usuarios u ON t.usuario_tarefa = u.id_usuario
            """)
            for row in cursor.fetchall():
                print(f"ID: {row[0]}, Título: {row[1]}, Descrição: {row[2]}, Status: {row[3]}, Usuário: {row[4]}")
        elif op == "0":
            break
        else:
            print("Opção inválida.")

def main():
    mostrar_splash()
    conn = conectar()
    print("Conexão com o banco realizada com sucesso!")
    ver_tabelas(conn)
    contar_registros(conn)  # 🟢 Adicionado conforme o edital
    ctrl_usuario = ControllerUsuario(conn)
    ctrl_tarefa = ControllerTarefa(conn)

    while True:
        print(MENUS["principal"])
        op = input("Escolha: ")
        if op == "1":
            menu_usuarios(ctrl_usuario)
        elif op == "2":
            menu_tarefas(ctrl_tarefa)
        elif op == "3":
            menu_relatorios(conn)
        elif op == "0":
            break

    conn.close()

if __name__ == "__main__":
    main()
