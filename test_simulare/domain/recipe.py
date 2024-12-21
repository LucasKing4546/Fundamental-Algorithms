cuisine=['Italian', 'Mexican', 'Indian']
class Recipe:
    def __init__(self, id, name, type, difficulty, time):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__difficulty = difficulty
        self.__time = time

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_difficulty(self):
        return self.__difficulty

    def get_time(self):
        return self.__time

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_type(self, type):
        self.__type = type

    def set_difficulty(self, difficulty):
        self.__difficulty = difficulty

    def set_time(self, time):
        self.__time = time

    def __repr__(self):
        print(f"Recipe id: {self.__id}, name: {self.__name}, cuisine type: {self.__type}, difficulty rating: {self.__difficulty}, preparation time: {self.__time}")

