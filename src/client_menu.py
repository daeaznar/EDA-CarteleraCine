

def client_menu():
    print()
    while True:
        print("""
                Please select an option to continue\n
                1. Search movies by name
                2. Search movies by rating
                3. Search movies by genre
                4. View full cinema Schedule (Sorted)
                5. View specific movie info.
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
            elif opt == 0:
                while True:
                    confirm = input("Are you sure you want to exit? (y/n)>>")
                    if confirm == 'y':
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
