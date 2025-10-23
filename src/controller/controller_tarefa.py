class ControllerTarefa:
    def _init_(self, oracle):
        self.oracle = oracle

    def inserir(self):
        titulo = input("Título da tarefa: ").strip()
        descricao = input("Descrição: ").strip()
        status = input("Status [PENDENTE/EM ANDAMENTO/CONCLUÍDO]: ").strip().upper()

        # Buscar usuários com ID e NOME
        usuarios, _ = self.oracle.sqlToMatrix("SELECT ID_USUARIO, NOME FROM USUARIOS")
        print("Usuários disponíveis:")
        for u in usuarios:
            print(f"{u[0]} - {u[1]}")

        usuario_id = int(input("ID do usuário responsável: "))
        try:
            self.oracle.write(
                f"INSERT INTO TAREFAS (ID_TAREFA, TITULO, DESCRICAO, STATUS, USUARIO_TAREFA) "
                f"VALUES (TAREFAS_SEQ.NEXTVAL, '{titulo}', '{descricao}', '{status}', {usuario_id})"
            )
            print("Tarefa inserida com sucesso!")
        except Exception as e:
            print("Erro ao inserir tarefa:", e)

    def listar(self):
        tarefas, _ = self.oracle.sqlToMatrix(
            "SELECT ID_TAREFA, TITULO, STATUS FROM TAREFAS ORDER BY ID_TAREFA"
        )
        for t in tarefas:
            print(f"{t[0]} - {t[1]} ({t[2]})")
        return [t[0] for t in tarefas]

    def atualizar(self):
        # Listagem amigável
        tarefas, _ = self.oracle.sqlToMatrix(
            "SELECT t.ID_TAREFA, t.TITULO, t.STATUS, u.NOME FROM TAREFAS t "
            "JOIN USUARIOS u ON t.USUARIO_TAREFA = u.ID_USUARIO ORDER BY t.ID_TAREFA"
        )
        print("TAREFAS CADASTRADAS:")
        for t in tarefas:
            print(f"{t[0]} - {t[1]} ({t[2]}) - Usuário: {t[3]}")
        ids = [t[0] for t in tarefas]

        try:
            id_tarefa = int(input("ID da tarefa a atualizar: "))
            if id_tarefa not in ids:
                print("ID inválido.")
                return
            titulo = input("Novo título: ").strip()
            descricao = input("Nova descrição: ").strip()
            status = input("Novo status: ").strip().upper()

            # Lista usuários para selecionar
            usuarios, _ = self.oracle.sqlToMatrix("SELECT ID_USUARIO, NOME FROM USUARIOS")
            print("Usuários disponíveis:")
            for u in usuarios:
                print(f"{u[0]} - {u[1]}")
            usuario_id = int(input("Novo ID do usuário responsável: "))

            self.oracle.write(
                f"UPDATE TAREFAS SET TITULO='{titulo}', DESCRICAO='{descricao}', STATUS='{status}', USUARIO_TAREFA={usuario_id} "
                f"WHERE ID_TAREFA={id_tarefa}"
            )
            print("Tarefa atualizada com sucesso!")
        except Exception as e:
            print("Erro ao atualizar tarefa:", e)

    def excluir(self):
        ids = self.listar()
        try:
            id_tarefa = int(input("ID da tarefa a excluir: "))
            if id_tarefa not in ids:
                print("ID inválido.")
                return
            confirm = input("Deseja realmente excluir? (S/N): ").strip().upper()
            if confirm == "S":
                self.oracle.write(f"DELETE FROM TAREFAS WHERE ID_TAREFA={id_tarefa}")
                print("Tarefa excluída com sucesso!")
        except Exception as e:
            print("Erro ao excluir tarefa:", e)
