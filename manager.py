def add_task(tasks, task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    return f"Tarefa {task_name} adicionada com sucesso!"

tasks = []

while True:
    print("\nGerenciador de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefa")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefa")
    print("6. Sair")

    choice = int(input("Digite uma opção: "))

    match choice:
        case 1:
            task_name = input("Digite o nome do tarefa que deseja adicionar: ")
            add_task(tasks, task_name)
        case 6:
            break

print("Programa finalizado com sucesso!")