import sqlite3
import mask_password
from classes import User


def admin_menu():
    print()
    while True:
        print("""
            Please select an option to continue\n
            1. Add Movie
            2. Add Movie time
            3. Delete Movie
            4. Delete Movie time
            5. Modify Movie
            6. View Movie
            7. Full cinema schedule
            8. Create admin account
            0. Log Out
            """)
        try:
            opt = int(input("Option: "))
        except:
            print("Invalid Option\n")
        else:
            if opt == 1:
                pass
            elif opt == 2:
                pass
            elif opt == 3:
                pass
            elif opt == 4:
                pass
            elif opt == 5:
                pass
            elif opt == 6:
                pass
            elif opt == 7:
                pass
            elif opt == 8:
                register()
            elif opt == 0:
                while True:
                    confirm = input("Are you sure you want to log out? (y/n)>>")
                    if confirm == 'y':
                        print(f"See you soon\n"
                              "Logging out...")
                        break
                    elif confirm == 'n':
                        print()
                        break
                    else:
                        print("Invalid Option\n")
                if confirm == 'y':
                    break
            else:
                print("Invalid Option\n")


# Add new user account to DB
def register():
    conn = sqlite3.connect('cinema.db')
    cursor = conn.cursor()
    print()
    print("*Register*")

    while True:
        print("Enter your information (press 0 to cancel)\n")
        user_name = input("User Name: ")
        if user_name == '0':
            break

        cursor.execute("SELECT user_name FROM user WHERE user_name = :user_name", {'user_name': user_name})
        check_user = cursor.fetchall()

        if len(check_user) != 0:
            print("user_name is already taken\n")
        else:
            print()
            while True:
                temp_password = mask_password.hide_pass()  # Prevent password from showing input
                password = mask_password.hide_pass(prompt='Confirm Password: ')
                if password == temp_password:
                    break
                else:
                    print("Error. Password doesn't match")
            while True:
                confirm = input("Is your information correct? (y/n)>>")
                if confirm == 'y':
                    user = User(user_name, password)

                    with conn:
                        cursor.execute("INSERT INTO user (user_name, password)"
                                       "VALUES(:user_name, :password)",
                                       {'user_name': user.user_name,
                                        'password': user.password})
                    break
                elif confirm == 'n':
                    print()
                    break
                else:
                    print("Invalid Option\n")
            if confirm == 'y':
                conn.close()
                break
        break
