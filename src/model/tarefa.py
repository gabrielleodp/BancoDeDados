class Tarefa:
    def __init__(self, id_tarefa, descricao, status, id_usuario):
        self.__id_tarefa = id_tarefa
        self.__descricao = descricao
        self.__status = status
        self.__id_usuario = id_usuario

    def obter_id_tarefa(self):
        return self.__id_tarefa

    def obter_descricao(self):
        return self.__descricao

    def obter_status(self):
        return self.__status

    def obter_id_usuario(self):
        return self.__id_usuario

    def definir_descricao(self, descricao):
        self.__descricao = descricao

    def definir_status(self, status):
        self.__status = status

    def definir_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def __str__(self):
        return f"ID: {self.__id_tarefa}, Descrição: {self.__descricao}, Status: {self.__status}, Usuário: {self.__id_usuario}"