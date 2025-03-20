import os
from project import Project
import datetime


def load_projects(filename):
    projects = []
    if not os.path.exists(filename):
        print(f"Error: The file {filename} does not exist.")
        return projects

    with open(filename, 'r') as file:
        file.readline()  # Skip the header
        for line in file:
            project = Project.from_string(line)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete = [project for project in projects if not project.is_completed()]
    completed = [project for project in projects if project.is_completed()]

    print("Incomplete projects:")
    incomplete.sort(key=Project.sort_by_priority)
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    completed.sort(key=Project.sort_by_priority)
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects, filter_date):
    date_obj = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > date_obj]
    filtered_projects.sort(key=lambda p: p.start_date)

    for project in filtered_projects:
        print(f"{project}")


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    for index, project in enumerate(projects):
        print(f"{index} {project}")

    project_choice = int(input("Project choice: "))
    project = projects[project_choice]

    new_percentage = input(f"New Percentage (current: {project.completion_percentage}): ")
    if new_percentage:
        new_percentage = int(new_percentage)
    else:
        new_percentage = project.completion_percentage

    new_priority = input(f"New Priority (current: {project.priority}): ")
    if new_priority:
        new_priority = int(new_priority)
    else:
        new_priority = project.priority

    project.update(new_percentage, new_priority)


def main():
    filename = 'projects.txt'
    projects = load_projects(filename)

    while True:
        print(
            "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)

        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            filter_date = input("Show projects that start after date (dd/mm/yy): ")
            filter_projects_by_date(projects, filter_date)

        elif choice == 'a':
            add_new_project(projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? (y/n): ")
            if save_choice.lower() == 'y':
                save_projects(filename, projects)
            print("Thank you for using custom-built project management software.")
            break


if __name__ == "__main__":
    main()
