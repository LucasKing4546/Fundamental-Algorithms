from domain.hospital import Departments
from domain.patient import Patient

class DepartmentsRepository:
    def __init__(self, departments: list['Departments']|None):
        '''
        Initializes the DepartmentsRepository with an optional list of departments.

        Parameters:
        departments (list[Departments] | None): List of Department objects or None.

        Result:
        Initializes the __departments attribute.
        '''
        if departments is None:
            self.__departments = []
        else:
            self.__departments = departments

    def add_department(self, id: int, name: str, beds: int, patients: list['Patient']):
        '''
        Adds a new department to the repository.

        Parameters:
        id (int): Department ID.
        name (str): Department name.
        beds (int): Number of beds in the department.
        patients (list[Patient]): List of Patient objects associated with the department.

        Result:
        Appends a new Departments instance to the __departments list.
        '''
        self.__departments.append(Departments(id, name, beds, patients))

    def get_department(self, department_id: int):
        '''
        Retrieves a department by its ID.

        Parameters:
        department_id (int): The ID of the department to retrieve.

        Result:
        Returns the Departments object corresponding to the given ID.
        '''
        return self.__departments[department_id]

    def update_department(self, department_id: int, name: str, beds: int, patients: list['Patient']):
        '''
        Updates an existing department's information.

        Parameters:
        department_id (int): The ID of the department to update.
        name (str): New name for the department.
        beds (int): New number of beds.
        patients (list[Patient]): New list of patients.

        Result:
        Updates the specified department's details.
        '''
        self.__departments[department_id].set_name(name)
        self.__departments[department_id].set_number_of_beds(beds)
        self.__departments[department_id].set_list_of_patients(patients)

    def delete_department(self, department_id: int):
        '''
        Deletes a department by its ID.

        Parameters:
        department_id (int): The ID of the department to delete.

        Result:
        Removes the department from the __departments list.
        '''
        self.__departments.pop(department_id)

    def get_all_departments(self):
        '''
        Retrieves all departments.

        Parameters:
        None.

        Result:
        Returns the list of all Departments objects.
        '''
        return self.__departments

