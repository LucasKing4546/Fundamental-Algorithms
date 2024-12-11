class Departments:
    def __init__(self, id: int, name: str, number_of_beds: int, list_of_patients: list):
        if isinstance(id, int) and isinstance(name, str) and isinstance(number_of_beds, int) and isinstance(list_of_patients, list):
            self.__id = id
            self.__name = name
            self.__number_of_beds = number_of_beds
            self.__list_of_patients = list_of_patients
        else:
            raise ValueError("Invalid inputs")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_number_of_beds(self):
        return self.__number_of_beds

    def get_list_of_patients(self):
        return self.__list_of_patients

    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("Id must be an integer")

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("Name must be an string")

    def set_number_of_beds(self, number_of_beds):
        if isinstance(number_of_beds, int) and number_of_beds >= 0:
            self.__number_of_beds = number_of_beds
        else:
            raise ValueError("Number of beds must be a positive integer")

    def set_list_of_patients(self, list_of_patients):
        if isinstance(list_of_patients, list):
            self.__list_of_patients = list_of_patients
        else:
            raise ValueError("List of_patients must be a list")


