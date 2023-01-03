import json, datetime, create_project
from utils import Validator


def edit_project(user_email):
    print(" Edit Project ".center(48, "*"))
    project_title = input("Project Title:\n")
    project = get_project(project_title, user_email)
    if project:
        print(
            f"Project Title: {project['Title']}, Project Details: {project['Details']}, Total Target: {project['Total_Target']}, Start Time: {project['Start_Time']}, End Time: {project['End_Time']}"
        )
        if input(f"Edit Project Title: {project['Title']}\nLeave It Empty To Not Change\nEnter Any Key and Press Enter To Change Value\n"):
            title = Validator.validate_name("Project Title")
        else:
            title = project["Title"]
        if input(f"Edit Project Details: {project['Details']}\nLeave It Empty To Not Change\nEnter Any Key and Press Enter To Change Value\n"):
            details = Validator.validate_name("Project Details")
        else:
            details = project["Details"]
        if input(f"Edit Project Total Target: {project['Total_Target']}\nLeave It Empty To Not Change\nEnter Any Key and Press Enter To Change Value\n"):
            total_target = Validator.validate_number("Total Target")
        else:
            total_target = project["Total_Target"]
        if input(f"Edit Project Start Time: {project['Start_Time']}\nLeave It Empty To Not Change\nEnter Any Key and Press Enter To Change Value\n"):
            start_date = Validator.validate_time("Start Time: dd/mm/yy")
        else:
            start_date = datetime.datetime.strptime(project["Start_Time"], "%Y-%m-%d %H:%M:%S")
        if start_date > datetime.datetime.strptime(project["End_Time"], "%Y-%m-%d %H:%M:%S") or input(
            f"Edit Project End Time: {project['End_Time']}\nLeave It Empty To Not Change\nEnter Any Key and Press Enter To Change Value\n"
        ):
            end_date = Validator.validate_time("End Time: dd/mm/yy", start_date)
        else:
            end_date = project["End_Time"]
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
