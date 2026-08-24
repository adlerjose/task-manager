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

def update_task_name(tasks, task_index, new_task_name):
    ajusted_task_index = task_index - 1
    if 0 <= ajusted_task_index < len(tasks):
        tasks[ajusted_task_index]["task"] = new_task_name
        return f"Tarefa {task_index} atualizada para {new_task_name}"
    else:
        return "Índice de tarefa inválido!"

def complete_task(tasks, task_index):
    ajusted_task_index = task_index - 1
    tasks[ajusted_task_index]["completed"] = True
    return f"Tarefa {task_index} completada com sucesso!"

def delete_completed_task(tasks):
    for task in tasks:
        if task["completed"]:
            tasks.remove(task)
    return "Tarefa completada(s) deletada(s) com sucesso!"

tasks = []

while True:
    print("\nGerenciador de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefa(s)")
    print("3. Atualizar nome da tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefa(s) completada(s)")
    print("6. Sair")

    choice = int(input("Digite uma opção: "))

    match choice:
        case 1:
            task_name = input("Digite o nome do tarefa que deseja adicionar: ")
            print(add_task(tasks, task_name))
        case 2:
            view_task(tasks)
        case 3:
            view_task(tasks)
            task_index = int(input("Digite o número da tarefa que deseja atualizar: "))
            new_name = input("Digite o novo nome da tarefa: ")
            print(update_task_name(tasks, task_index, new_name))
        case 4:
            view_task(tasks)
            task_index = int(input("Digite o número da tarefa que deseja completar: "))
            print(complete_task(tasks, task_index))
        case 5:
            print(delete_completed_task(tasks))
            view_task(tasks)
        case 6:
            break

print("Programa finalizado com sucesso!")