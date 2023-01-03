import json
from utils import Validator


def create_project(user_email):
    print(" Create Project ".center(48, "*"))
    title = Validator.validate_name("Project Title")
    details = Validator.validate_name("Project Details")
    total_target = Validator.validate_number("Total Target")
    start_date = Validator.validate_time("Start Time: dd/mm/yy")
    end_date = Validator.validate_time("End Time: dd/mm/yy", start_date)
    project = {
        "Title": title,
        "Details": details,
        "Total_Target": total_target,
        "Start_Time": str(start_date),
        "End_Time": str(end_date),
        "User": user_email,
    }
    if project:
        add_project(project)
        print(" Project Created ".center(48, "*"))
    else:
        print(" Project Creation Failed ".center(48, "*"))


def add_project(project):
    try:
        projects = get_projects()
        with open("./projects.json", "w") as json_file:
            projects.append(project)
            json.dump(projects, json_file)
    except Exception as e:
        print(e)


def get_projects():
    try:
        with open("./projects.json", "r") as json_file:
            projects = json.load(json_file)
            return projects
    except Exception as e:
        return []
