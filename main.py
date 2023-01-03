import os
from registration import register
from login import login


def main_menu():
    while True:
        os.system("clear")
        print(" Crowd Funding ".center(48, "*"))
        print(" Main Menu ".center(48, "*"))
        choice = input("Choose:\n1) For Registration\n2) For Login\n3) To Exit\n")
        if choice.isnumeric():
            choice = int(choice)
        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            exit()


main_menu()
