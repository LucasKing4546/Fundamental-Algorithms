from repository.hospital_repo import DepartmentsRepository

class HospitalController:
    def __init__(self, department_repo: 'DepartmentsRepository'):
        '''
        Initializes the HospitalController with a department repository.

        Parameters:
        department_repo (DepartmentsRepository): Repository for managing hospital departments.

        Result:
        Sets the __department_repo attribute to the provided repository.
        '''
        self.__department_repo = department_repo

    def sort_patients_by_pnc(self, index: int) -> None:
        '''
        Sorts the list of patients in a department by their personal numeric code (PNC).

        Parameters:
        index (int): The index of the department in the repository.

        Result:
        Updates the list of patients in the specified department, sorted by PNC.
        '''
        patient_list = self.__department_repo.get_department(index).get_list_of_patients()
        patient_list.sort(key=lambda patient: patient.get_pnc())
        self.__department_repo.get_department(index).set_list_of_patients(patient_list)

    def sort_by_number_of_patients(self):
        '''
        Sorts the departments in the repository by the number of patients in each department.

        Parameters:
        None.

        Result:
        Updates the __department_repo with departments sorted by the number of patients.
        '''
        self.__department_repo = DepartmentsRepository(
            self.__department_repo.sorting_departments("patient")
        )

    def sort_by_number_of_patient_over_an_age(self, age: int):
        '''
        Sorts departments by the number of patients over a specified age.

        Parameters:
        age (int): The age threshold to filter patients.

        Result:
        Updates the departments in the repository sorted by the number of patients over the specified age.
        '''
        # Copy of original repository to maintain the list of patients
        department_repo_copy = self.__department_repo

        for department in self.__department_repo.get_all_departments():
            department.set_list_of_patients([patient
                                             for patient in department.get_list_of_patients()
                                             if patient.get_age() > age])

        self.__department_repo.sorting_departments("patient")

        for i in range(len(self.__department_repo.get_all_departments())):
            department = department_repo_copy.get_department(i)
            self.__department_repo.get_department(i).set_list_of_patients(department.get_list_of_patients())

    def get_departments_patients_under_an_age(self, age: int):
        '''
        Retrieves departments that have patients under a specified age.

        Parameters:
        age (int): The age threshold to filter patients.

        Result:
        Returns a list of departments that have patients under the specified age.
        '''
        departments = []
        for department in self.__department_repo.get_all_departments():
            if len([patient
                    for patient in department.get_list_of_patients()
                    if patient.get_age() < age]) != 0:
                departments.append(department)
        return departments

    def get_departments_patient_first_name(self, first_name: str):
        '''
        Retrieves departments that have patients with a specified first name.

        Parameters:
        first_name (str): The first name to filter patients.

        Result:
        Returns a list of departments with patients having the specified first name.
        '''
        departments = []
        for department in self.__department_repo.get_all_departments():
            if len([patient
                    for patient in department.get_list_of_patients()
                    if patient.get_first_name() == first_name]) != 0:
                departments.append(department)
        return departments

    def get_patients_first_or_last_name(self, index: int, string: str):
        '''
        Retrieves patients from a department whose first or last name contains a specified string.

        Parameters:
        index (int): The index of the department in the repository.
        string (str): The string to search in first or last names.

        Result:
        Returns a list of patients whose first or last name contains the specified string.
        '''
        department = self.__department_repo.get_department(index)
        patients = [patient
                    for patient in department.get_list_of_patients()
                    if string in patient.get_last_name() or
                    string in patient.get_first_name()
                    ]
        return patients
