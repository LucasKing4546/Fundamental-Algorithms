from repository.hospital_repo import DepartmentsRepository

class HospitalController:
    def __init__(self, department_repo: 'DepartmentsRepository'):
        self.__department_repo = department_repo

    def sort_patients_by_pnc(self, index) -> None:
        patient_list = self.__department_repo.get_department(index).get_list_of_patients()
        patient_list.sort(key=lambda patient: patient.get_pnc())
        self.__department_repo.get_department(index).set_list_of_patients(patient_list)

    def sort_by_number_of_patients(self):
        self.__department_repo = DepartmentsRepository(
            self.__department_repo.sorting_departments("patient")
        )

    def sort_by_number_of_patient_over_an_age(self, age: int):
        # Copy of original repository to maintain the list of patients
        department_repo_copy = self.__department_repo

        for department in self.__department_repo.get_all_departments():
            department.set_list_of_patients([department.get_list_of_patients()
                                             for patient in department.get_list_of_patients()
                                             if patient.get_age() > age])

        self.__department_repo.sorting_departments("patient")

        for i in range(len(self.__department_repo.get_all_departments())):
            department = department_repo_copy.get_department(i)
            self.__department_repo.get_department(i).set_list_of_patients(department.get_list_of_patients())

    def get_departments_patients_under_an_age(self, age):
        departments = []
        for department in self.__department_repo.get_all_departments():
            if len([department.get_list_of_patients()
                    for patient in department.get_list_of_patients()
                    if patient.get_age() < age]) != 0:
                departments.append(department)
        return departments

    def get_departments_patient_first_name(self, first_name):
        departments = []
        for department in self.__department_repo.get_all_departments():
            if len([department.get_list_of_patients()
                    for patient in department.get_list_of_patients()
                    if patient.get_first_name() == first_name]) != 0:
                departments.append(department)
        return departments

    def get_patients_first_or_last_name(self, index: int, string: str):
        department = self.__department_repo.get_department(index)
        patients = [patient
                    for patient in department.get_list_of_patients()
                    if string in patient.get_last_name() or
                    string in patient.get_first_name()
                    ]
        return patients