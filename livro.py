class ItemBiblioteca:
    def __init__(self, nome, id, autor):
        self.__nome = nome
        self.__id = id
        self.__autor = autor
        self.__disponibilidade = True
        self.__emprestado_por = None

    def get_nome(self):
        return self.__nome

    def get_id(self):
        return self.__id

    def get_autor(self):
        return self.__autor

    def is_disponivel(self):
        return self.__disponibilidade

    def get_emprestado_por(self):
        return self.__emprestado_por

    def emprestar(self, usuario_id):
        if self.__disponibilidade:
            self.__disponibilidade = False
            self.__emprestado_por = usuario_id
            return True
        return False

    def devolver(self, usuario_id):
        if not self.__disponibilidade and self.__emprestado_por == usuario_id:
            self.__disponibilidade = True
            self.__emprestado_por = None
            return True
        return False

    def to_dict(self):
        return {
            "nome": self.__nome,
            "id": self.__id,
            "autor": self.__autor,
            "disponibilidade": self.__disponibilidade,
            "emprestado_por": self.__emprestado_por
        }

    @classmethod
    def from_dict(cls, data):
        item = cls(data["nome"], data["id"], data["autor"])
        item.__disponibilidade = data["disponibilidade"]
        item.__emprestado_por = data["emprestado_por"]
        return item

    def __str__(self):
        status = "Disponível" if self.__disponibilidade else f"Emprestado por {self.__emprestado_por}"
        return f"{self.__nome} (ID: {self.__id}, Autor: {self.__autor}) - {status}"

class Livro(ItemBiblioteca):
    pass