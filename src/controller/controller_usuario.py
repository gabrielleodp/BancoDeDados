from src.model.usuario import Usuario
import cx_Oracle

class ControllerUsuario:
    def __init__(self, connection):
        self.connection = connection

    def inserir(self, usuario: Usuario):
        cursor = self.connection.cursor()
        if usuario.obter_id_usuario() == 0 or usuario.obter_id_usuario() is None:
            cursor.execute(
                "INSERT INTO usuarios (nome, email) VALUES (:1, :2)",
                [usuario.obter_nome(), usuario.obter_email()]
            )
        else:
            cursor.execute(
                "INSERT INTO usuarios (id_usuario, nome, email) VALUES (:1, :2, :3)",
                [usuario.obter_id_usuario(), usuario.obter_nome(), usuario.obter_email()]
            )
        self.connection.commit()

    def atualizar(self, usuario: Usuario):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE usuarios SET nome=:1, email=:2 WHERE id_usuario=:3",
            [usuario.obter_nome(), usuario.obter_email(), usuario.obter_id_usuario()]
        )
        self.connection.commit()

    def excluir(self, id_usuario):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM usuarios WHERE id_usuario=:1",
                [id_usuario]
            )
            self.connection.commit()
        except cx_Oracle.IntegrityError as e:
            # Mensagem amigável para violação de integridade
            print("Não é possível excluir o usuário pois existem tarefas associadas a ele.")

    def listar(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id_usuario, nome, email FROM usuarios")
        # Retorna uma lista de objetos Usuario
        return [Usuario(row[0], row[1], row[2]) for row in cursor.fetchall()]