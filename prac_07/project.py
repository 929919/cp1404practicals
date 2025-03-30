import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    @classmethod
    def from_string(cls, project_str):
        name, start_date, priority, cost_estimate, completion_percentage = project_str.strip().split("\t")
        return cls(name, start_date, priority, cost_estimate, completion_percentage)

    def is_completed(self):
        return self.completion_percentage == 100

    def update(self, new_percentage=None, new_priority=None):
        if new_percentage is not None:
            self.completion_percentage = new_percentage
        if new_priority is not None:
            self.priority = new_priority

    @staticmethod
    def sort_by_priority(project):
        return project.priority
