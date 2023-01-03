import json, create_project, edit_project


def delete_project(user_email):
    print(" Delete Project ".center(48, "*"))
    project_title = input("Project Title:\n")
    del_project = edit_project.get_project(project_title, user_email)
    if del_project:
        try:
            updated_projects = []
            projects = create_project.get_projects()
            with open("./projects.json", "w") as json_file:
                for project in projects:
                    if project["Title"] == project_title and project["User"] == user_email:
                        print(" Project Deleted Successfully ".center(48, "*"))
                    else:
                        updated_projects.append(project)
                json.dump(updated_projects, json_file)
        except Exception as e:
            print(e)
