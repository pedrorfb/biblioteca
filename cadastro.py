import json
from livro import Livro

class CadastroUsuario:
    def __init__(self, arquivo_usuarios="usuarios.json"):
        self.__arquivo_usuarios = arquivo_usuarios
        self.__usuarios = []
        self.__carregar_usuarios()

    def __carregar_usuarios(self):
        try:
            with open(self.__arquivo_usuarios, "r") as file:
                self.__usuarios = json.load(file)
        except FileNotFoundError:
            self.__usuarios = []

    def salvar_usuarios(self):
        with open(self.__arquivo_usuarios, "w") as file:
            json.dump(self.__usuarios, file, indent=4)

    def cadastrar_usuario(self):
        nome_do_usuario = input('Insira o nome do usuário que você deseja criar: ')
        id_do_usuario = str(len(self.__usuarios) + 1)
        novo_usuario = {
            "nome": nome_do_usuario,
            "id": id_do_usuario,
            "livros": []
        }
        self.__usuarios.append(novo_usuario)
        self.salvar_usuarios()
        print(f'Usuário {nome_do_usuario} cadastrado com sucesso!')

    def login(self):
        nome = input('Insira o nome do usuário: ')
        for usuario in self.__usuarios:
            if usuario["nome"] == nome:
                print(f'Bem-vindo(a), {nome}!')
                return usuario
        print("Usuário não encontrado.")
        return None

    def get_usuarios_dict(self):
        return {usuario["id"]: usuario["nome"] for usuario in self.__usuarios}

catalogo = []

CATALOGO_ARQUIVO = "catalogo.json"

def carregar_catalogo():
    global catalogo
    try:
        with open(CATALOGO_ARQUIVO, "r") as file:
            dados = json.load(file)
            catalogo = [Livro.from_dict(livro) for livro in dados]
    except FileNotFoundError:
        catalogo = [
            Livro("Senhor dos Anéis", "1", "J.R.R. Tolkien"),
            Livro("1984", "2", "George Orwell"),
            Livro("Cem Anos de Solidão", "3", "Gabriel García Márquez"),
            Livro("O Morro dos Ventos Uivantes", "4", "Emily Brontë"),
            Livro("Moby Dick", "5", "Herman Melville"),
            Livro("Neuromancer", "6", "William Gibson"),
            Livro("A Culpa é das Estrelas", "7", "John Green"),
            Livro("O Homem Invisível", "8", "H.G. Wells"),
            Livro("O Pequeno Príncipe",  "9", "Antoine de Saint-Exupéry"),
            Livro("O Código Da Vinci", "10", "Dan Brown"),
            Livro("O Pistoleiro", "11", "Stephen King"),
            Livro("Ulisses", "12", "James Joyce"),
            Livro("A Ilha do Tesouro", "13", "Robert Louis Stevenson"),
            Livro("Percy Jackson e o Ladrão de Raios", "14", "Rick Riordan"),
            Livro("Dom Quixote", "15", "Miguel de Cervantes"),
            Livro("A Dança dos Dragões", "16", "George R.R. Martin"),
            Livro("Os Três Mosqueteiros", "17", "Alexandre Dumas"),
            Livro("O Alquimista", "18", "Paulo Coelho"),
            Livro("Admirável Mundo Novo", "19", "Aldous Huxley"),
            Livro("Orgulho e Preconceito", "20  ", "Jane Austen"),
            Livro("Drácula", "21", "Bram Stoker"),
            Livro("Frankenstein", "22", "Mary Shelley"),
            Livro("O Grande Gatsby", "23", "F. Scott Fitzgerald"),
            Livro("Crime e Castigo", "24", "Fyodor Dostoyevsky"),
            Livro("O Senhor das Moscas", "25", "William Golding")
    ]

def salvar_catalogo():
    with open(CATALOGO_ARQUIVO, "w") as file:
        json.dump([livro.to_dict() for livro in catalogo], file, indent=4)

def mostrar_catalogo(usuarios):
    print('Catálogo de livros:\n')
    for livro in catalogo:
        status = "Disponível" if livro.is_disponivel() else f"Emprestado por {usuarios.get(livro.get_emprestado_por(), 'Desconhecido')}"
        print(f'- {livro.get_nome()} (ID: {livro.get_id()}, Autor: {livro.get_autor()}) - {status}')

def emprestar_livro(nome_do_livro, usuario_id, usuarios, usuario):
    for livro in catalogo:
        if livro.get_nome().lower() == nome_do_livro.lower():
            if livro.emprestar(usuario_id):
                usuario["livros"].append(livro.get_nome())
                nome_usuario = usuarios.get(usuario_id, "Desconhecido")
                print(f"O livro '{livro.get_nome()}' foi emprestado com sucesso para o usuário {nome_usuario}!")
                salvar_catalogo()
                return livro
            print(f"O livro '{livro.get_nome()}' já está emprestado.")
            return None
    print(f"O livro '{nome_do_livro}' não foi encontrado no catálogo.")
    return None

def devolver_livro(nome_do_livro, usuario_id, usuarios, usuario):
    for livro in catalogo:
        if livro.get_nome().lower() == nome_do_livro.lower():
            if livro.devolver(usuario_id):
                usuario["livros"].remove(livro.get_nome())
                nome_usuario = usuarios.get(usuario_id, "Desconhecido")
                print(f"O livro '{livro.get_nome()}' foi devolvido com sucesso pelo usuário {nome_usuario}!")
                salvar_catalogo()
                return
            print(f"Você não pode devolver o livro '{livro.get_nome()}', pois ele foi emprestado por outro usuário.")
            return
    print(f"O livro '{nome_do_livro}' não foi encontrado no catálogo.")