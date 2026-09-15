TODO_FILE = "todos.txt"


def read_tasks():
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]

    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(task):
    tasks = read_tasks()
    tasks.append(f"[ ] {task}")
    save_tasks(tasks)
    return f'Task added: "{task}"'


def complete_task(task_name):
    tasks = read_tasks()
    task_name = task_name.lower().strip()
    for i, task in enumerate(tasks):
        if task.startswith("[ ]"):
            existing_task = task[3:].strip()
            if existing_task.lower() == task_name:
                tasks[i] = f"[✓] {existing_task}"
                save_tasks(tasks)
                return f'Task completed: "{existing_task}"'
    return f'Could not find a pending task named "{task_name}".'


def get_status():
    tasks = read_tasks()
    completed = []
    pending = []
    for task in tasks:
        if task.startswith("[✓]"):
            completed.append(task[3:].strip())

        elif task.startswith("[ ]"):
            pending.append(task[3:].strip())

    return {
        "total": len(tasks),
        "completed_count": len(completed),
        "completed": completed,
        "pending_count": len(pending),
        "pending": pending
    }