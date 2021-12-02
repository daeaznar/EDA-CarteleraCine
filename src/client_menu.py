

from listData import ListData
from prettytable import PrettyTable

listsData: ListData = None
city_id = None

def client_menu(lists: ListData):
    global listsData
    listsData = lists

    
    while True:
        print("\n******************************\n")
        state_code = input("State ID:")
        city_code = input("City ID:")
        print("\n******************************\n")

        filteredState = listsData.states.getByFilter('state_code', state_code)
        filteredCities = None

        if (filteredState.list != None):
            filteredCities = listsData.cities.getByFilter('city_code', city_code, 'state_id', filteredState.list.data.state_id)
            
            if (filteredCities.list != None):
                city_id = filteredCities.list.data.city_id

                break
            else:
                print(f"No match was found for State ID {state_code} and City ID {city_code}\n\n")
        else:
            print(f"No match was found for State ID {state_code}\n\n")

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
                searchMovieByFilter('name')
            elif opt == 2:
                searchMovieByFilter('rating')
            elif opt == 3:
                searchMovieByFilter('genre')
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


def searchMovieByFilter(filter):
    textGetFilter = ''
    if (filter == 'name'):
        textGetFilter = 'Name: '
        print("""
            \n******************************\n
                1. Search movies by name
            \n******************************\n
        """)
    if (filter == 'rating'):
        textGetFilter = 'Rating: '
        print("""
            \n******************************\n
                2. Search movies by rating
            \n******************************\n
        """)
    if (filter == 'genre'):
        textGetFilter = 'Genre: '
        print("""
            \n******************************\n
                3. Search movies by genre
            \n******************************\n
        """)

    filterText = input(textGetFilter)
        
    filteredData = listsData.movies.getByFilter(filter, filterText)

    table = PrettyTable(['Name', 'Director', 'Genre', 'Producer', 'Rating', 'Duration'])

    for row in filteredData:
        table.add_row([
            row.name,
            row.director,
            row.genre_id,
            row.producer,
            row.rating,
            f'{str(int(row.length))}min'
        ])
        
    print(table)
