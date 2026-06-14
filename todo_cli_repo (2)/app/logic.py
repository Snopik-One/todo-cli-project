def add_task(tasks, title):
    tasks.append({"id": len(tasks)+1, "title": title, "done": False})

def list_tasks(tasks):
    for t in tasks:
        status = "done" if t["done"] else "pending"
        print(f'{t["id"]}. {t["title"]} [{status}]')

def complete_task(tasks, task_id):
    for t in tasks:
        if str(t["id"]) == str(task_id):
            t["done"] = True

def delete_task(tasks, task_id):
    tasks[:] = [t for t in tasks if str(t["id"]) != str(task_id)]
# Module responsible for saving and loading tasks
