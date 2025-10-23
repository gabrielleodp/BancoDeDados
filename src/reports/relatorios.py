from src.conexion.oracle_queries import OracleQueries

class Relatorio:
    def _init_(self, oracle: OracleQueries):
        self.oracle = oracle  # usa a conexão existente

    def rel_usuarios(self):
        resultado, _ = self.oracle.sqlToMatrix("SELECT id_usuario, nome, email FROM usuarios")
        print("\nUSUÁRIOS CADASTRADOS:")
        print("-" * 40)
        for row in resultado:
            print(f"ID: {row[0]} | Nome: {row[1]} | Email: {row[2]}")
        print("-" * 40)

    def rel_tarefas(self):
        resultado, _ = self.oracle.sqlToMatrix("""
            SELECT t.id_tarefa, t.titulo, t.status, u.nome
            FROM tarefas t
            JOIN usuarios u ON t.usuario_tarefa = u.id_usuario
            ORDER BY t.id_tarefa
        """)
        print("\nTAREFAS CADASTRADAS:")
        print("-" * 50)
        for row in resultado:
            print(f"ID: {row[0]} | Título: {row[1]} | Status: {row[2]} | Responsável: {row[3]}")
        print("-" * 50)

    def rel_tarefas_group_by(self):
        resultado, _ = self.oracle.sqlToMatrix("""
            SELECT u.nome, COUNT(t.id_tarefa) AS total_tarefas
            FROM tarefas t
            JOIN usuarios u ON t.usuario_tarefa = u.id_usuario
            GROUP BY u.nome
            ORDER BY total_tarefas DESC
        """)
        print("\nTOTAL DE TAREFAS POR USUÁRIO:")
        print("-" * 40)
        for row in resultado:
            print(f"Usuário: {row[0]} | Total de Tarefas: {row[1]}")
        print("-" * 40)

    def rel_tarefas_join(self):
        resultado, _ = self.oracle.sqlToMatrix("""
            SELECT t.id_tarefa, t.titulo, t.status, u.nome
            FROM tarefas t
            JOIN usuarios u ON t.usuario_tarefa = u.id_usuario
            ORDER BY t.id_tarefa
        """)
        print("\nTAREFAS COM DADOS DO USUÁRIO (JOIN):")
        print("-" * 50)
        for row in resultado:
            print(f"ID: {row[0]} | Título: {row[1]} | Status: {row[2]} | Usuário: {row[3]}")
        print("-" * 50)
