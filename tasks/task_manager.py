from tasks.task_storage import TaskStorage

class TaskManager:
    def __init__(self):
        self.storage = TaskStorage()

    def add_task(self, title, description):
        task = {"title": title, "description": description}
        self.storage.save_task(task)
        print("Tarefa adicionada com sucesso!")

    def list_tasks(self):
        tasks = self.storage.load_tasks()
        if tasks:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task['title']} - {task['description']}")
        else:
            print("Nenhuma tarefa cadastrada.")

    def edit_task(self, task_id, new_title, new_description):
        tasks = self.storage.load_tasks()
        if 0 < task_id <= len(tasks):
            tasks[task_id - 1]['title'] = new_title
            tasks[task_id - 1]['description'] = new_description
            self.storage.save_all_tasks(tasks)
            print("Tarefa editada com sucesso!")
        else:
            print("ID de tarefa inválido.")

    def remove_task(self, task_id):
        tasks = self.storage.load_tasks()
        if 0 < task_id <= len(tasks):
            tasks.pop(task_id - 1)
            self.storage.save_all_tasks(tasks)
            print("Tarefa removida com sucesso!")
        else:
            print("ID de tarefa inválido.")