class Usuario:
    def __init__(self, id_usuario, nome, email):
        self.__id_usuario = id_usuario
        self.__nome = nome
        self.__email = email

    def obter_id_usuario(self):
        return self.__id_usuario

    def obter_nome(self):
        return self.__nome

    def obter_email(self):
        return self.__email

    def definir_nome(self, nome):
        self.__nome = nome

    def definir_email(self, email):
        self.__email = email

    def __str__(self):
        return f"ID: {self.__id_usuario}, Nome: {self.__nome}, Email: {self.__email}"
