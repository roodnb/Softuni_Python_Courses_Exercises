from project.task import Task


class Section:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        try:
            current_task = [el for el in self.tasks if el.name == task_name][0]
            current_task.completed = True
            return f"Completed task {task_name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        # completed = [el for el in self.tasks if el.completed]
        # not_completed = [el for el in self.tasks if not el.completed]
        # self.tasks = not_completed
        # return f"Cleared {len(completed)} tasks."

        count = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                count += 1
        return f"Cleared {count} tasks."

    def view_section(self):
        # result = f"Section {self.name}:\n"
        # result += "\n".join([el.details() for el in self.tasks])

        result = f"Section {self.name}:"
        for t in self.tasks:
            result += f"\n{t.details()}"
        return result