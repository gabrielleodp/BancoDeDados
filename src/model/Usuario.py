class Usuario:
    def __init__(self, id_usuario=None, nome=None, email=None):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email

    # Getters
    def get_id_usuario(self):
        return self.id_usuario

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    # Setters
    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def set_nome(self, nome):
        self.nome = nome

    def set_email(self, email):
        self.email = email

    # To string
    def to_string(self):
        return f"Usuario(id={self.id_usuario}, nome={self.nome}, email={self.email})"

