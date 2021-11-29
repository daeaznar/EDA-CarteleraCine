
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