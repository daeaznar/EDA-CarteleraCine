import sqlite3

class ScreenMovie:
    def __init__(
        self,
        screen_id=None,
        screen_number=None,
        movie_id=None,
        city_id=None,
        movie_time=None,
        is_active=1
    ):
        self.screen_id = screen_id
        self.screen_number = screen_number
        self.movie_id = movie_id
        self.city_id = city_id
        self.movie_time = movie_time
        self.is_active = is_active

    def __getitem__(self, key):
        return getattr(self, key)

class NodeScreenMovie:
    def __init__(self, data = None, prev = None, next = None):
        self.data: ScreenMovie = data
        self.prev: NodeScreenMovie = prev
        self.next: NodeScreenMovie = next

class ListScreenMovie:
    def __init__(self):
        self.list: NodeScreenMovie = None

    def getList(self):
        return self.list

    def getByFilter(self, key: str, value: any):
        filteredData = ListScreenMovie()

        tempList = self.list

        while(True):
            if (tempList.data[key] == value):
                filteredData.insert(tempList.data)

            if (tempList == None or tempList.next is None):
                break
            else:
                tempList = tempList.next

        return filteredData

    def insert(self, data: ScreenMovie):
        def insertValue(tempList: NodeScreenMovie):
            if (tempList is None):
                newList = NodeScreenMovie(data)
                return newList
            if (tempList.next is None):
                newList = NodeScreenMovie(data, tempList)
                tempList.next = newList
                return tempList
            else:
                tempList.next = insertValue(tempList.next)
                return tempList

        self.list = insertValue(self.list)

    def update(self, pos: int, data: ScreenMovie):
        def updateValue(tempList: NodeScreenMovie, tempPos: int):
            if (tempList is None):
                return tempList
            else:
                if (tempPos == pos):
                    tempList.data = data
                    return tempList
                else:
                    tempList.next = updateValue(tempList.next, tempPos + 1)
                    return tempList

    def delete(self, pos: int):
        def deleteValue(tempList: NodeScreenMovie, tempPos: int):
            if (tempList is None):
                return tempList
            else:
                if (tempPos == pos):
                    if (tempList.prev == None):
                        newList = tempList.next
                        newList.prev = None

                        return newList
                    else:
                        newList = tempList.next
                        newList.prev = tempList.prev
                        
                        return newList
                elif (tempPos + 1 == pos and tempList.next.next == None):
                    tempList.next = None

                    return tempList
                else:
                    tempList.next = deleteValue(tempList.next, tempPos + 1)
                    return tempList

        self.list = deleteValue(self.list, 0)

class ScreenMoviesModel:
    def __init__(self):
        self.table = 'screen_movie'
        self.database = 'cinema.db'

    def getAll(self):
        # create DB connection
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        try:
            result = cursor.execute(f'SELECT * FROM ' + self.table).fetchall()

            if (result):
                conn.close()
                data = []

                for i, row in enumerate(result):
                    data.insert(i, ScreenMovie(row[0], row[1], row[2], row[3], row[4], row[5]))

                return data
            else:
                conn.close()
                return []
        except:
            conn.close()
            return []

    def create(self, user: ScreenMovie):
        # create DB connection
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        try:
            result = cursor.execute('INSERT INTO ' + self.table + ' (' + ('screen_id, ' if user.screen_id != None else '') + 'screen_number, movie_id, city_id, movie_time, is_active) VALUES (' + (':screen_id, ' if user.screen_id != None else '') + ':screen_number, :movie_id, :city_id, :movie_time, :is_active)',  {'screen_id': user.screen_id, 'screen_number': user.screen_number, 'movie_id': user.movie_id, 'city_id': user.city_id, 'movie_time': user.movie_time, 'is_active': user.is_active})
            conn.commit()
            
            if (result):
                return True
            else:
                conn.close()
                return None
        except:
            conn.close()
            return None
    
    def deleteAll(self):
        # create DB connection
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        try:
            result = cursor.execute('DELETE FROM ' + self.table + ' WHERE 1 = 1')
            conn.commit()
            
            if (result):
                return True
            else:
                conn.close()
                return None
        except:
            conn.close()
            return None