import sqlite3
import mask_password
from listData import *
from classes import User
from binaryTree import TreeNode
import models.movies

listData = ListData()
listData.getDatabaseData()

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
                addMovie()
            elif opt == 2:
                pass
            elif opt == 3:
                deleteMovie()
            elif opt == 4:
                pass
            elif opt == 5:
                pass
            elif opt == 6:
                pass
            elif opt == 7:
                viewCinema()
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


def addMovie():
    name = input("Enter the name of the movie to ADD: ")
    
    
    movieNode = TreeNode()
    tempList = listData.movies.list

    while True:
        movieNode.insert('name', tempList.data)
        if tempList.next is None:
            break
        else:
            tempList = tempList.next

    # orderedMoviesASC = movieNode.inorder([])

    # print('\n\n********** Lista orden ASC **********')
    # for row in orderedMoviesASC:
    #     print(f'{row.movie_id} - {row.name}')

    # orderedMoviesDESC = movieNode.inorder([], False)

    # print('\n\n********** Lista orden DESC **********')
    # for row in orderedMoviesDESC:
    #     print(f'{row.movie_id} - {row.name}')


def deleteMovie():
    name = input("Enter the name of the movie to DELETE: ")

    movieNode = TreeNode()
    tempList = listData.movies.list
    while True:
            movieNode.insert('name', tempList.data)
            if tempList.next is None:
                break
            else:
                tempList = tempList.next


def viewCinema():
    movieNode = TreeNode()
    tempList = listData.movies.list

    while True:
        movieNode.insert('name', tempList.data)
        if tempList.next is None:
            break
        else:
            tempList = tempList.next

    while True:
        print("""
            Please select an option to continue\n
            1. Sort Ascendant
            2. Sort Descendant
            0. Go Back
            """)
        try:
            opt = int(input("Option: "))
        except:
            print("Invalid Option\n")
        else:
            if opt == 1:
                orderedMoviesASC = movieNode.inorder([])
                print('\n\n********** Lista orden ASC **********')
                for row in orderedMoviesASC:
                    print(f'{row.movie_id} - {row.name}')
            elif opt == 2:
                orderedMoviesDESC = movieNode.inorder([], False)
                print('\n\n********** Lista orden DESC **********')
                for row in orderedMoviesDESC:
                    print(f'{row.movie_id} - {row.name}')
            elif opt == 0:
                break
            else:
                print("Invalid Option\n")