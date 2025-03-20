import csv
from project import Project
import os

def load_projects(filename='projects.txt'):
    projects = []
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)  # Skip the header
            for row in reader:
                name, start_date, priority, cost_estimate, completion_percentage = row
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
    return projects

def save_projects(projects, filename='projects.txt'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'), project.priority, project.cost_estimate, project.completion_percentage])
