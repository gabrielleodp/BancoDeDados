from src.model.Usuario import Usuario
import cx_Oracle

class ControllerUsuario:
    def __init__(self, connection):
        self.connection = connection

    def inserir(self, usuario: Usuario):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO usuarios (id_usuario, nome, email) VALUES (:1, :2, :3)",
            [usuario.get_id_usuario(), usuario.get_nome(), usuario.get_email()]
        )
        self.connection.commit()

    def atualizar(self, usuario: Usuario):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE usuarios SET nome=:1, email=:2 WHERE id_usuario=:3",
            [usuario.get_nome(), usuario.get_email(), usuario.get_id_usuario()]
        )
        self.connection.commit()

    def excluir(self, id_usuario):
        cursor = self.connection.cursor()
        cursor.execute(
            "DELETE FROM usuarios WHERE id_usuario=:1", [id_usuario]
        )
        self.connection.commit()

    def listar(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id_usuario, nome, email FROM usuarios")
        return [Usuario(row[0], row[1], row[2]) for row in cursor.fetchall()]

