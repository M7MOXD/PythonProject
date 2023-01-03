import json, create_project
from utils import Validator


def edit_project(user_email):
    print(" Edit Project ".center(48, "*"))
    project_title = input("Project Title:\n")
    project = get_project(project_title, user_email)
    if project:
        print(
            f"Project Title: {project['Title']}, Project Details: {project['Details']}, Total Target: {project['Total_Target']}, Start Time: {project['Start_Time']}, End Time: {project['End_Time']}"
        )
        title = Validator.validate_name("Project Title")
        details = Validator.validate_name("Project Details")
        total_target = Validator.validate_number("Total Target")
        start_date = Validator.validate_time("Start Time: dd/mm/yy")
        end_date = Validator.validate_time("End Time: dd/mm/yy", start_date)
        edited_project = {
            "Title": title,
            "Details": details,
            "Total_Target": total_target,
            "Start_Time": str(start_date),
            "End_Time": str(end_date),
            "User": user_email,
        }
        edit(project, edited_project)
        print(" Project Edited Successfully ".center(48, "*"))
    else:
        print(" No Project With That Title ".center(48, "*"))


def edit(old_project, edited_project):
    try:
        updated_projects = []
        projects = create_project.get_projects()
        with open("./projects.json", "w") as json_file:
            for project in projects:
                if project["Title"] == old_project["Title"] and project["User"] == old_project["User"]:
                    updated_projects.append(edited_project)
                else:
                    updated_projects.append(project)
            json.dump(updated_projects, json_file)
    except Exception as e:
        print(e)


def get_project(title, email):
    try:
        with open("./projects.json", "r") as json_file:
            projects = json.load(json_file)
            for project in projects:
                if project["Title"] == title and project["User"] == email:
                    return project
    except Exception as e:
        print(e)
