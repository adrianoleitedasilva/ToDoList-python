import csv
import os

class TaskStorage:
    def __init__(self, filename="tasks.csv"):
        self.filename = filename

    def save_task(self, task):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "description"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(task)

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def save_all_tasks(self, tasks):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "description"])
            writer.writeheader()
            writer.writerows(tasks)