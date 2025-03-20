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

def display_projects(projects):
    print("Incomplete projects: ")
    incomplete_projects = sorted([p for p in projects if not p.is_completed()], key=lambda p: p.priority)
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects: ")
    completed_projects = sorted([p for p in projects if p.is_completed()], key=lambda p: p.priority)
    for project in completed_projects:
        print(f"  {project}")

import datetime

def filter_projects_by_date(projects, date_string):
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > date]
    return sorted(filtered_projects, key=lambda p: p.start_date)

def add_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print(f"Added: {new_project}")

def update_project(projects):
    print("Choose a project to update:")
    for idx, project in enumerate(projects):
        print(f"{idx} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(f"Updating: {project}")
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)
    if new_priority:
        project.priority = int(new_priority)
    print(f"Updated: {project}")
