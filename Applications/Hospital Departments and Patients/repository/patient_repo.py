from domain.patient import Patient

class PatientRepository:
    def __init__(self, patients: list['Patient']|None):
        if patients is None:
            self.__patients = []
        else:
            self.__patients = patients

    def add_patient(self, first_name: str, last_name: str, pnc: int, disease: str):
        if isinstance(first_name, str) and isinstance(last_name, str) and isinstance(pnc,int) and isinstance(disease, str):
            self.__patients.append(Patient(first_name, last_name, pnc, disease))
        else:
            if not isinstance(first_name, str):
                raise TypeError('First Name must be a string')
            elif not isinstance(last_name, str):
                raise TypeError('Last Name must be a string')
            elif not isinstance(pnc,int):
                raise TypeError('Patient Number must be a integer')
            elif not isinstance(disease, str):
                raise TypeError('Disease must be a string')

    def get_patient(self, patient_id: int) -> Patient:
        if isinstance(patient_id, int) and 0 <= patient_id < len(self.__patients):
            return self.__patients[patient_id]

    def update_patient(self, patient_id: int, first_name: str, last_name: str, pnc: int, disease: str):
        if isinstance(patient_id, int) and 0 <= patient_id < len(self.__patients):
            if isinstance(first_name, str) and isinstance(last_name, str) and isinstance(pnc, int) and isinstance(disease, str):
                self.__patients[patient_id].set_first_name(first_name)
                self.__patients[patient_id].set_last_name(last_name)
                self.__patients[patient_id].set_pnc(pnc)
                self.__patients[patient_id].set_disease(disease)
            else:
                if not isinstance(first_name, str):
                    raise TypeError('First Name must be a string')
                elif not isinstance(last_name, str):
                    raise TypeError('Last Name must be a string')
                elif not isinstance(pnc, int):
                    raise TypeError('Patient Number must be a integer')
                elif not isinstance(disease, str):
                    raise TypeError('Disease must be a string')
        else:
            raise TypeError('Invalid patient id')

    def delete_patient(self, patient_id: int):
        if isinstance(patient_id, int) and 0 <= patient_id < len(self.__patients):
            self.__patients.pop(patient_id)
        else:
            raise TypeError('Invalid patient id')
