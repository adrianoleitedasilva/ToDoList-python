from tasks.task_manager import TaskManager

def main():
    task_manager = TaskManager()

    while True:
        print("\nSistema de Gerenciamento de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Editar Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            task_manager.add_task(titulo, descricao)
        elif escolha == '2':
            task_manager.list_tasks()
        elif escolha == '3':
            task_id = int(input("Digite o ID da tarefa a ser editada: "))
            novo_titulo = input("Digite o novo título: ")
            nova_descricao = input("Digite a nova descrição: ")
            task_manager.edit_task(task_id, novo_titulo, nova_descricao)
        elif escolha == '4':
            task_id = int(input("Digite o ID da tarefa a ser removida: "))
            task_manager.remove_task(task_id)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
