from app.logic import add_task, list_tasks, complete_task, delete_task
from app.storage import load_tasks, save_tasks

def handle_command(cmd: str):
    tasks = load_tasks()

    parts = cmd.split(" ", 1)
    action = parts[0]

    arg = parts[1] if len(parts) > 1 else ""

    if action == "add":
        add_task(tasks, arg)
        save_tasks(tasks)
        print("Task added")

    elif action == "list":
        list_tasks(tasks)

    elif action == "done":
        complete_task(tasks, arg)
        save_tasks(tasks)

    elif action == "delete":
        delete_task(tasks, arg)
        save_tasks(tasks)

    elif action == "help":
        print("add <task>, list, done <id>, delete <id>, exit")

    else:
        print("Unknown command")
