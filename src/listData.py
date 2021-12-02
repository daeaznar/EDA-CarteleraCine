import time

from models.users import *
from models.states import *
from models.cities import *
from models.genres import *
from models.movies import *

class ListData():
    def __init__(self):
        self.userModel = UsersModel()
        self.users = ListUser()
        self.stateModel = StatesModel()
        self.states = ListState()
        self.cityModel = CitiesModel()
        self.cities = ListCity()
        self.genreModel = GenresModel()
        self.genres = ListGenre()
        self.movieModel = MoviesModel()
        self.movies = ListMovie()

    def getDatabaseData(self):
        # get Users data and put into a list
        users = self.userModel.getAll()
        state = self.stateModel.getAll()
        city = self.cityModel.getAll()
        genre = self.genreModel.getAll()
        movie = self.movieModel.getAll()

        for row in users:
            self.users.insert(row)
        for row in state:
            self.states.insert(row)
        for row in city:
            self.cities.insert(row)
        for row in genre:
            self.genres.insert(row)
        for row in movie:
            self.movies.insert(row)
    
    def backUpData(self):
        # get Users list and backup into database
        self.userModel.deleteAll()
        usersList = self.users.list

        if (usersList != None): 
            while(1 == 1):
                self.userModel.create(usersList.data)

                if (usersList.next is None):
                    break
                else:
                    usersList = usersList.next

        # get Movies list and backup into database
        self.movieModel.deleteAll()
        moviesList = self.movies.list

        if (moviesList != None): 
            while(1 == 1):
                self.movieModel.create(moviesList.data)

                if (moviesList.next is None):
                    break
                else:
                    moviesList = moviesList.next

# listData = ListData()
# listData.getDatabaseData()

# # filteredData = listData.users.getByFilter('user_name', 'john.doe')

# # time.sleep(5)

# tempList = listData.genres.list

# while(True):
#     print(str(tempList.data.genre_id) + '- Name: ' + tempList.data.name)

#     if (tempList.next is None):
#         break
#     else:
#         tempList = tempList.next

# # listData.backUpData()
    