from domain.hospital import Departments
from domain.patient import Patient

class DepartmentsRepository:
    def __init__(self, departments: list['Departments']|None):
        if departments is None:
            self.__departments = []
        else:
            self.__departments = departments

    def add_department(self, id: int, name: str, beds: int, patients: list['Patient']):
        if isinstance(id, int) and isinstance(name, str) and isinstance(beds, int) and isinstance(patients, list):
            self.__departments.append(Departments(id, name, beds, patients))
        else:
            if not isinstance(id, int):
                raise TypeError('id must be an integer')
            elif not isinstance(name, str):
                raise TypeError('name must be an string')
            elif not isinstance(beds, int):
                raise TypeError('beds must be an integer')
            elif not isinstance(patients, list):
                raise TypeError('patients must be an list')

    def get_department(self, department_id: int):
        if isinstance(department_id, int) and 0 <= department_id < len(self.__departments):
            return self.__departments[department_id]
        else:
            raise TypeError('department_id must be an integer')

    def update_department(self, department_id: int, name: str, beds: int, patients: list['Patient']):
        if isinstance(department_id, int) and 0 <= department_id < len(self.__departments):
            if isinstance(name, str) and isinstance(beds, int) and isinstance(patients, list):
                self.__departments[department_id].set_name(name)
                self.__departments[department_id].set_number_of_beds(beds)
                self.__departments[department_id].set_list_of_patients(patients)
            else:
                if not isinstance(name, str):
                    raise TypeError('name must be an string')
                elif not isinstance(beds, int):
                    raise TypeError('beds must be an integer')
                elif not isinstance(patients, list):
                    raise TypeError('patients must be an list')
        else:
                raise TypeError('Invalid department id')

    def delete_department(self, department_id: int):
        if isinstance(department_id, int) and 0 <= department_id < len(self.__departments):
            self.__departments.pop(department_id)
        else:
            raise TypeError('Invalid department id')

    def get_all_departments(self):
        return self.__departments

    def sorting_departments(self, condition):
        if condition == "patient":
            self.__departments.sort(key=lambda x: len(x.get_list_of_patients()))
        elif condition == "id":
            self.__departments.sort(key=lambda x: x.get_id())
        elif condition == "name":
            self.__departments.sort(self.__departments,key=lambda x: x.get_name())
        elif condition == "beds":
            self.__departments.sort(self.__departments,key=lambda x: x.get_number_of_beds())
        else:
            raise ValueError("Invalid condition")
