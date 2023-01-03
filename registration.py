import json
from utils import Validator


def register():
    print(" Register ".center(48, "*"))
    first_name = Validator.validate_name("First Name")
    last_name = Validator.validate_name("Last Name")
    email = Validator.validate_email()
    password = Validator.validate_password()
    mobile_phone = Validator.validate_phone()
    new_user = {
        "First_Name": first_name,
        "Last_Name": last_name,
        "Email": email,
        "Password": password,
        "Mobile_Phone": mobile_phone,
    }
    if new_user:
        add_user(new_user)
        print(" Registration Successful ".center(48, "*"))
    else:
        print(" Registration Failed ".center(48, "*"))


def add_user(user):
    try:
        users = get_users()
        with open("./users.json", "w") as json_file:
            users.append(user)
            json.dump(users, json_file)
    except Exception as e:
        print(e)


def get_users():
    try:
        with open("./users.json", "r") as json_file:
            users = json.load(json_file)
            return users
    except Exception as e:
        return []
