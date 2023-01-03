import json
from view_projects import view_all_projects, view_user_projects
from create_project import create_project
from edit_project import edit_project
from delete_project import delete_project


def login():
    print(" Log In ".center(48, "*"))
    email = input("Email:\n")
    password = input("Password:\n")
    user = get_user(email, password)
    if user:
        print(" Login Successful ".center(48, "*"))
        while True:
            print(" Logged In ".center(48, "*"))
            choice = input(
                "Choose:\n1) To View All Projects\n2) To View Your Projects\n3) To Create a New Project\n4) To Edit a Project\n5) To Delete a Project\n6) To Exit\n"
            )
            if choice.isnumeric():
                choice = int(choice)
            if choice == 1:
                view_all_projects()
            elif choice == 2:
                view_user_projects(email)
            elif choice == 3:
                create_project(email)
            elif choice == 4:
                edit_project(email)
            elif choice == 5:
                delete_project(email)
            elif choice == 6:
                exit()
    else:
        print(" Login Failed ".center(48, "*"))


def get_user(email, password):
    try:
        with open("./users.json", "r") as json_file:
            users = json.load(json_file)
            for user in users:
                if user["Email"] == email and user["Password"] == password:
                    return user
    except Exception as e:
        print(e)
