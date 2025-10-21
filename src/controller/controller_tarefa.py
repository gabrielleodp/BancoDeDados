from src.model.tarefa import Tarefa
import cx_Oracle

class ControllerTarefa:
    def __init__(self, connection):
        self.connection = connection

    def inserir(self, tarefa: Tarefa):
        cursor = self.connection.cursor()
        if tarefa.obter_id_tarefa() is None:
            cursor.execute(
                "INSERT INTO tarefas (titulo, descricao, status, usuario_tarefa) VALUES (:1, :2, :3, :4)",
                [tarefa.obter_titulo(), tarefa.obter_descricao(), tarefa.obter_status(), tarefa.obter_id_usuario()]
            )
        else:
            cursor.execute(
                "INSERT INTO tarefas (id_tarefa, titulo, descricao, status, usuario_tarefa) VALUES (:1, :2, :3, :4, :5)",
                [tarefa.obter_id_tarefa(), tarefa.obter_titulo(), tarefa.obter_descricao(), tarefa.obter_status(), tarefa.obter_id_usuario()]
            )

        self.connection.commit()

    def atualizar(self, tarefa: Tarefa):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE tarefas SET titulo=:1, descricao=:2, status=:3, usuario_tarefa=:4 WHERE id_tarefa=:5",
            [tarefa.obter_titulo(), tarefa.obter_descricao(), tarefa.obter_status(), tarefa.obter_id_usuario(), tarefa.obter_id_tarefa()]
        )
        self.connection.commit()

    def excluir(self, id_tarefa):
        cursor = self.connection.cursor()
        cursor.execute(
            "DELETE FROM tarefas WHERE id_tarefa=:1",
            [id_tarefa]
        )
        self.connection.commit()

    def listar(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id_tarefa, titulo, descricao, status, usuario_tarefa FROM tarefas")
        return [Tarefa(row[0], row[1], row[2], row[3], row[4]) for row in cursor.fetchall()]
