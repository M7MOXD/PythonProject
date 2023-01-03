import json


def view_all_projects():
    print(" All Projects ".center(48, "*"))
    try:
        with open("./projects.json", "r") as json_file:
            projects = json.load(json_file)
            if projects:
                for project in projects:
                    print(
                        f"Project Title: {project['Title']}, Project Details: {project['Details']}, Total Target: {project['Total_Target']}, Start Time: {project['Start_Time']}, End Time: {project['End_Time']}"
                    )
            else:
                print(" No Projects To View ".center(48, "*"))
    except Exception as e:
        print(" No Projects To View ".center(48, "*"))


def view_user_projects(user_email):
    print(" User Projects ".center(48, "*"))
    try:
        count = 0
        with open("./projects.json", "r") as json_file:
            projects = json.load(json_file)
            for project in projects:
                if project["User"] == user_email:
                    print(
                        f"Project Title: {project['Title']}, Project Details: {project['Details']}, Total Target: {project['Total_Target']}, Start Time: {project['Start_Time']}, End Time: {project['End_Time']}"
                    )
                    count += 1
            if not count:
                print(" No Projects To View ".center(48, "*"))
    except Exception as e:
        print(" No Projects To View ".center(48, "*"))
