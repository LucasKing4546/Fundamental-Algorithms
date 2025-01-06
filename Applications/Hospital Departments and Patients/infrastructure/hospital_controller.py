from repository.hospital_repo import DepartmentsRepository
from repository.patient_repo import PatientRepository
from utilities.utility import *

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
        patient_repo = self.__department_repo.get_department(index).get_list_of_patients()
        patient_list = patient_repo.get_all_patients()
        sorting(patient_list, key=lambda patient: patient.get_pnc(), relation=lambda a, b: a > b)
        patient_repo = PatientRepository(patient_list)
        self.__department_repo.get_department(index).set_list_of_patients(patient_repo)

    def sort_by_number_of_patients_and_patients_alphabetically(self) -> None:
        '''
        Definition:
        Sorts departments by the number of patients, and then sorts the patients in each department alphabetically by their first name.

        Parameters:
        None.

        Result:
        Departments in the repository are sorted by the number of patients, and each department's patient list is sorted alphabetically by first name.
        '''
        sorting(self.__department_repo.get_all_departments(),
                key=lambda x: len(x.get_list_of_patients().get_all_patients()),
                relation=lambda a, b: a > b)
        for department in self.__department_repo.get_all_departments():
            sorting(department.get_list_of_patients().get_all_patients(),
                    key = lambda x: x.get_first_name(),
                    relation = lambda a, b: a > b)

    def sort_by_number_of_patients(self):
        '''
        Sorts the departments in the repository by the number of patients in each department.

        Parameters:
        None.

        Result:
        Updates the __department_repo with departments sorted by the number of patients.
        '''
        sorting(self.__department_repo.get_all_departments(),
                key=lambda x: len(x.get_list_of_patients().get_all_patients()),
                relation=lambda a, b: a > b)

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
            department.set_list_of_patients(PatientRepository(filtering(department.get_list_of_patients().get_all_patients(),
                                                      key = lambda patient: patient.get_age() > age)))

        sorting(self.__department_repo.get_all_departments(),
                key=lambda x: len(x.get_list_of_patients().get_all_patients()),
                relation=lambda a, b: a > b
                )

        for dep in self.__department_repo.get_all_departments():
            i = dep.get_id()
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
        return filtering(self.__department_repo.get_all_departments(),
                         key=lambda x: len(
                             [y for y in x.get_list_of_patients().get_all_patients()
                             if y.get_age() < age]
                         ) > 0)

    def get_departments_patient_first_name(self, first_name: str):
        '''
        Retrieves departments that have patients with a specified first name.

        Parameters:
        first_name (str): The first name to filter patients.

        Result:
        Returns a list of departments with patients having the specified first name.
        '''
        return filtering(self.__department_repo.get_all_departments(),
                         key=lambda x: len(
                             [y for y in x.get_list_of_patients().get_all_patients()
                              if y.get_first_name() == first_name]
                         ) > 0)

    def get_patients_first_or_last_name(self, index: int, string: str):
        '''
        Retrieves patients from a department whose first or last name contains a specified string.

        Parameters:
        index (int): The index of the department in the repository.
        string (str): The string to search in first or last names.

        Result:
        Returns a list of patients whose first or last name contains the specified string.
        '''
        return filtering(self.__department_repo.get_department(index).get_list_of_patients().get_all_patients(),
                         key=lambda x: string in x.get_first_name() or string in x.get_last_name(),
                         )

    def form_group_of_patients(self, k: int):
        '''
        Definition:
        Forms groups of 𝒌𝒌 patients from the same department and the same disease.

        Parameters:
        k (int): The size of the groups to form.

        Result:
        Returns a list of grouped patients, where each group has exactly `k` patients with the same disease.
        '''
        result_list = []
        for department in self.__department_repo.get_all_departments():
            diseases = different_diseases(department)
            for disease in diseases:
                patients = [x for x in department.get_list_of_patients().get_all_patients() if x.get_disease() == disease]
                results = []
                backtrack(k, [], 0, set(), patients, results, key=lambda x: x.get_pnc())
                if len(results) > 0:\
                    result_list.append(results)
        return result_list

    def form_group_of_departments(self, k: int, p: int):
        '''
        Definition:
        Forms groups of 𝒌𝒌 departments having at most 𝒑𝒑 patients suffering from the same disease.

        Parameters:
        k (int): The size of the groups to form.
        p (int): The maximum allowed number of patients with a single disease in a department.

        Result:
        Returns a list of grouped departments that meet the condition.
        '''
        departments = []
        results = []
        for department in self.__department_repo.get_all_departments():
            diseases = different_diseases(department)
            ok = 0
            for disease in diseases:
                patients = [x for x in department.get_list_of_patients().get_all_patients() if x.get_disease() == disease]
                if len(patients) > p:
                    ok = 1
                    break
            if ok == 0:
                departments.append(department)
        backtrack(k, [], 0, set(), departments, results, key=lambda x: x.get_id())
        return results

    #CRUD operations

    def add_department_controller(self, id: int, name: str, beds: int, patients: PatientRepository):
        if isinstance(id, int) and id not in [x.get_id() for x in self.__department_repo.get_all_departments()] and isinstance(name, str) and isinstance(beds, int) and isinstance(patients, PatientRepository):
            self.__department_repo.add_department(id, name, beds, patients)
        else:
            if not isinstance(id, int):
                raise TypeError('id must be an integer')
            elif not isinstance(name, str):
                raise TypeError('name must be a string')
            elif not isinstance(beds, int):
                raise TypeError('beds must be an integer')
            elif not isinstance(patients, list):
                raise TypeError('patients must be a PatientRepository')

    def get_department_controller(self, department_id: int):
        if isinstance(department_id, int):
            return self.__department_repo.get_department(department_id)
        else:
            raise TypeError('department_id must be an integer')

    def update_department_controller(self, department_id: int, name: str, beds: int, patients: PatientRepository):
        if isinstance(department_id, int):
            if isinstance(name, str) and isinstance(beds, int) and isinstance(patients, PatientRepository):
                self.__department_repo.update_department(department_id, name, beds, patients)
            else:
                if not isinstance(name, str):
                    raise TypeError('name must be a string')
                elif not isinstance(beds, int):
                    raise TypeError('beds must be an integer')
                elif not isinstance(patients, list):
                    raise TypeError('patients must be a PatientRepository')
        else:
            raise TypeError('Invalid department id')

    def delete_department_controller(self, department_id: int):
        if isinstance(department_id, int):
            self.__department_repo.delete_department(department_id)
        else:
            raise TypeError('Invalid department id')

    def get_all_departments_controller(self):
        return self.__department_repo.get_all_departments()