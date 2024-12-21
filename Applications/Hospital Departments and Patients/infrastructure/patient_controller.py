from repository.patient_repo import PatientRepository


class PatientController:
    def __init__(self, repo: PatientRepository):
        self.__patient_repo = repo

    def add_patient_controller(self, first_name: str, last_name: str, pnc: int, disease: str, age: int):
        if isinstance(first_name, str) and isinstance(last_name, str) and isinstance(pnc, int) and isinstance(disease,str) and isinstance(age, int):
            self.__patient_repo.add_patient(first_name, last_name, pnc, disease, age)
        else:
            if not isinstance(first_name, str):
                raise TypeError('First Name must be a string')
            elif not isinstance(last_name, str):
                raise TypeError('Last Name must be a string')
            elif not isinstance(pnc, int):
                raise TypeError('Patient Number must be an integer')
            elif not isinstance(disease, str):
                raise TypeError('Disease must be a string')
            elif not isinstance(age, int):
                raise TypeError('Age must be an integer')

    def get_patient_controller(self, patient_id: int):
        if isinstance(patient_id, int):
            return self.__patient_repo.get_patient(patient_id)
        else:
            raise TypeError('Invalid patient id')

    def update_patient_controller(self, patient_id: int, first_name: str, last_name: str, pnc: int, disease: str, age: int):
        if isinstance(first_name, str) and isinstance(last_name, str) and isinstance(pnc, int) and isinstance(disease,str) and isinstance(age, int):
            self.__patient_repo.update_patient(patient_id, first_name, last_name, pnc, disease, age)
        else:
            # Raise specific errors for invalid input types.
            if not isinstance(first_name, str):
                raise TypeError('First Name must be a string')
            elif not isinstance(last_name, str):
                raise TypeError('Last Name must be a string')
            elif not isinstance(pnc, int):
                raise TypeError('Patient Number must be an integer')
            elif not isinstance(disease, str):
                raise TypeError('Disease must be a string')
            elif not isinstance(age, int):
                raise TypeError('Age must be an integer')
            else:
                raise TypeError('Invalid patient id')

    def delete_patient_controller(self, patient_id: int):
        if isinstance(patient_id, int):
            self.__patient_repo.delete_patient(patient_id)
        else:
            raise TypeError('Invalid patient id')
