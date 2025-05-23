
from domain.patient import Patient

class PatientRepository:
    def __init__(self, patients: list['Patient']|None):
        '''
        Initializes the PatientRepository with an optional list of patients.

        Parameters:
        patients (list[Patient] | None): List of Patient objects or None.

        Result:
        Initializes the __patients attribute.
        '''
        if patients is None:
            self.__patients = []
        else:
            self.__patients = patients

    def add_patient(self, first_name: str, last_name: str, pnc: int, disease: str, age: int):
        '''
        Adds a new patient to the repository.

        Parameters:
        first_name (str): Patient's first name.
        last_name (str): Patient's last name.
        pnc (int): Patient's unique personal numeric code.
        disease (str): Patient's diagnosed disease.
        age (int): Patient's age.

        Result:
        Appends a new Patient instance to the __patients list.
        '''
        self.__patients.append(Patient(first_name, last_name, pnc, disease, age))

    def get_patient(self, patient_id: int) -> Patient:
        '''
        Retrieves a patient by their ID.

        Parameters:
        patient_id (int): The ID of the patient to retrieve.

        Result:
        Returns the Patient object corresponding to the given ID.
        '''
        return self.__patients[patient_id]

    def update_patient(self, patient_id: int, first_name: str, last_name: str, pnc: int, disease: str, age: int):
        '''
        Updates an existing patient's information.

        Parameters:
        patient_id (int): The ID of the patient to update.
        first_name (str): New first name for the patient.
        last_name (str): New last name for the patient.
        pnc (int): New personal numeric code.
        disease (str): New diagnosed disease.
        age (int): New age of the patient.

        Result:
        Updates the specified patient's details.
        '''
        if isinstance(patient_id, int) and 0 <= patient_id < len(self.__patients):
            self.__patients[patient_id].set_first_name(first_name)
            self.__patients[patient_id].set_last_name(last_name)
            self.__patients[patient_id].set_pnc(pnc)
            self.__patients[patient_id].set_disease(disease)
            self.__patients[patient_id].set_age(age)

    def delete_patient(self, patient_id: int):
        '''
        Deletes a patient by their ID.

        Parameters:
        patient_id (int): The ID of the patient to delete.

        Result:
        Removes the patient from the __patients list.
        '''
        self.__patients.pop(patient_id)

    def get_all_patients(self):
        return self.__patients

    def __repr__(self):
        return f"{self.__patients}\n"
