from cadastro import CadastroUsuario, carregar_catalogo, mostrar_catalogo, emprestar_livro, devolver_livro, salvar_catalogo


def main():
    sistema = CadastroUsuario()
    carregar_catalogo()

    while True:
        print("\n--- Sistema de Biblioteca ---")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("3. Mostrar catálogo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.cadastrar_usuario()
        elif opcao == "2":
            usuario = sistema.login()
            if usuario:
                while True:
                    print("\n--- Menu do Usuário ---")
                    print("1. Ver catálogo")
                    print("2. Emprestar livro")
                    print("3. Devolver livro")
                    print("4. Sair")
                    opcao_usuario = input("Escolha uma opção: ")

                    if opcao_usuario == "1":
                        mostrar_catalogo(sistema.get_usuarios_dict())
                    elif opcao_usuario == "2":
                        livro_nome = input("Digite o nome do livro que deseja emprestar: ")
                        emprestar_livro(livro_nome, usuario["id"], sistema.get_usuarios_dict(), usuario)
                        sistema.salvar_usuarios()
                    elif opcao_usuario == "3":
                        livro_nome = input("Digite o nome do livro que deseja devolver: ")
                        devolver_livro(livro_nome, usuario["id"], sistema.get_usuarios_dict(), usuario)
                        sistema.salvar_usuarios()
                    elif opcao_usuario == "4":
                        break
        elif opcao == "3":
            mostrar_catalogo(sistema.get_usuarios_dict())
        elif opcao == "4":
            salvar_catalogo()
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
