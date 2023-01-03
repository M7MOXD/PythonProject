import re
from datetime import datetime


class Validator:
    @staticmethod
    def validate_name(msg):
        while True:
            name = input(f"{msg}:\n")
            name = name.replace(" ", "")
            if name.isalpha():
                return name
            else:
                print(f"Invalid {msg}")

    @staticmethod
    def validate_number(msg):
        while True:
            number = input(f"{msg}:\n")
            if number.replace(".", "", 1).isdigit():
                return float(number)
            else:
                print("Invalid Number")

    @staticmethod
    def validate_email():
        while True:
            email = input("Email:\n")
            if re.fullmatch(r"^[\w\.]+@([\w]+\.)+[\w]{2,4}$", email):
                return email
            else:
                print("Invalid Email")

    @staticmethod
    def validate_password():
        while True:
            special_symbols = ["$", "@", "#", "%", "!"]
            password = input(
                "Password:\nPassword Must Be:\nAt Least 6 Characters Long\nContaining: One Spcial Character, One Digit, One Lowercase Character, One Uppercase Character\n"
            )
            if len(password) < 6:
                print("Invalid Password: Password Should Be at Least 6 Characters Long")
                continue
            if not any(char.isdigit() for char in password):
                print("Invalid Password: Password Should Contain at Least One Digit")
                continue
            if not any(char.isupper() for char in password):
                print("Invalid Password: Password Should Contain at Least One Uppercase Character")
                continue
            if not any(char.islower() for char in password):
                print("Invalid Password: Password Should Contain at Least One Lowercase Character")
                continue
            if not any(char in special_symbols for char in password):
                print("Invalid Password: Password Should Contain at Least One Special Character")
                continue
            if Validator.confirm_password(password):
                return password
            else:
                print("Passwords Do Not Match")

    @staticmethod
    def confirm_password(current_password):
        confirmed_password = input("Confirm Password:\n")
        if confirmed_password == current_password:
            return True
        return False

    @staticmethod
    def validate_phone():
        while True:
            mobile_phone = input("Mobile Phone:\n")
            if re.fullmatch(r"^01[0-2,5]\d{8}$", mobile_phone):
                return mobile_phone
            else:
                print("Invalid Phone Number")

    @staticmethod
    def validate_time(msg, delta=datetime.strptime(datetime.today().strftime("%d/%m/%Y"), "%d/%m/%Y")):
        while True:
            date_str = input(f"{msg}:\n")
            try:
                time = datetime.strptime(date_str, "%d/%m/%Y")
                if time >= delta:
                    return time
            except Exception as e:
                print(e)
