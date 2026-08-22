def add_task(tasks, task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    return f"Tarefa {task_name} adicionada com sucesso!"

def view_task(tasks):
    print("\nLista de Tarefas")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        task_name = task["task"]
        print(f"{index}. [{status}] {task_name}")

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
            print(add_task(tasks, task_name))
        case 2:
            view_task(tasks)
        case 6:
            break

print("Programa finalizado com sucesso!")