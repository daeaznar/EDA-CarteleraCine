from sys import exit
import sqlite3
import mask_password
import admin_menu
import client_menu
from classes import User

# Define connection and cursor2
conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()


def main():
    while True:
        print("""
========== Cinema System ==========\n
    Please select an option to continue\n
    1. View Movies and Times
    2. Login as Admin
    0. Exit
        """)
        try:
            opt = int(input("Option: "))
        except:
            print("Invalid Option\n")
        else:
            if opt == 1:
                client_menu.client_menu()
            elif opt == 2:
                login()
            elif opt == 0:
                while True:
                    confirm = input("Are you sure you want to exit? (y/n)>>")
                    if confirm == 'y':
                        print("See you later ;)\n\n"
                              "Exiting System...")
                        exit()
                    elif confirm == 'n':
                        print()
                        break
                    else:
                        print("Invalid Option\n")
            else:
                print("Invalid Option\n")


def login():
    print()
    print("*Login*")
    while True:
        print("Enter your credentials (press 0 to cancel)\n")
        user_name = input("User Name: ")
        if user_name == '0':
            break
        password = mask_password.hide_pass()
        try:
            # region Get User
            query = cursor.execute("SELECT user_id FROM user WHERE user_name = :user_name AND password = :password",
                                   {'user_name': user_name, 'password': password})
            if query:
                user_id = cursor.fetchone()[0]

                cursor.execute("SELECT user_name FROM user WHERE user_id = :user_id", {'user_id': user_id})
                user_name = cursor.fetchone()[0]

                cursor.execute("SELECT password FROM user WHERE user_id = :user_id", {'user_id': user_id})
                password = cursor.fetchone()[0]

                user = User(user_name, password)
                # endregion
            else:
                print('Something went wrong, please try again later')
        except:
            print("Incorrect user_name or password\n")
        else:
            admin_menu.admin_menu()
            break


if __name__ == '__main__':
    main()
    conn.close()
