class ControllerUsuario:
    def _init_(self, oracle):
        self.oracle = oracle

    def inserir(self):
        nome = input("Nome: ").strip()
        email = input("Email: ").strip()
        try:
            self.oracle.write(
                f"INSERT INTO USUARIOS (ID_USUARIO, NOME, EMAIL) VALUES (USUARIOS_SEQ.NEXTVAL, '{nome}', '{email}')"
            )
            print("Usuário inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir usuário:", e)

    def listar(self):
        usuarios, _ = self.oracle.sqlToMatrix(
            "SELECT ID_USUARIO, NOME, EMAIL FROM USUARIOS ORDER BY ID_USUARIO"
        )
        for u in usuarios:
            print(f"{u[0]} - {u[1]} ({u[2]})")
        return [u[0] for u in usuarios]

    def atualizar(self):
        # Listagem amigável
        usuarios, _ = self.oracle.sqlToMatrix(
            "SELECT ID_USUARIO, NOME, EMAIL FROM USUARIOS ORDER BY ID_USUARIO"
        )
        print("USUÁRIOS CADASTRADOS:")
        for u in usuarios:
            print(f"{u[0]} - {u[1]} ({u[2]})")
        ids = [u[0] for u in usuarios]

        try:
            id_usuario = int(input("ID do usuário a atualizar: "))
            if id_usuario not in ids:
                print("ID inválido.")
                return
            nome = input("Novo nome: ").strip()
            email = input("Novo email: ").strip()
            self.oracle.write(
                f"UPDATE USUARIOS SET NOME='{nome}', EMAIL='{email}' WHERE ID_USUARIO={id_usuario}"
            )
            print("Usuário atualizado com sucesso!")
        except Exception as e:
            print("Erro ao atualizar usuário:", e)

    def excluir(self):
        ids = self.listar()
        try:
            id_usuario = int(input("ID do usuário a excluir: "))
            if id_usuario not in ids:
                print("ID inválido.")
                return
            confirm = input("Deseja realmente excluir? (S/N): ").strip().upper()
            if confirm == "S":
                try:
                    self.oracle.write(f"DELETE FROM USUARIOS WHERE ID_USUARIO={id_usuario}")
                    print("Usuário excluído com sucesso!")
                except Exception as e:
                    if "ORA-02292" in str(e):
                        print("Não é possível excluir este usuário. Existem tarefas vinculadas a ele.")
                    else:
                        print("Erro ao excluir usuário:", e)
        except Exception as e:
            print("Erro ao excluir usuário:", e)
