tarefas = []


def criar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição: ")

    tarefa = {
        "titulo": titulo,
        "descricao": descricao
    }

    tarefas.append(tarefa)
    print("Tarefa criada com sucesso!")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1}. {tarefa['titulo']} - {tarefa['descricao']}")


def atualizar_tarefa():
    listar_tarefas()

    indice = int(input("Digite o número da tarefa: ")) - 1

    if 0 <= indice < len(tarefas):
        novo_titulo = input("Novo título: ")
        nova_descricao = input("Nova descrição: ")

        tarefas[indice]["titulo"] = novo_titulo
        tarefas[indice]["descricao"] = nova_descricao

        print("Tarefa atualizada!")
    else:
        print("Tarefa inválida.")


def excluir_tarefa():
    listar_tarefas()

    indice = int(input("Digite o número da tarefa para excluir: ")) - 1

    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida!")
    else:
        print("Tarefa inválida.")


while True:
    print("\n1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        atualizar_tarefa()
    elif opcao == "4":
        excluir_tarefa()
    elif opcao == "5":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida!")
