from domain.patient import Patient
from repository.patient_repo import PatientRepository


def test_add_patient():
    repo = PatientRepository([])
    repo.add_patient("Mark", "Taylor", 5555555555, "Cold", 35)
    repo.add_patient("Sophia", "Brown", 4444444444, "Fever", 28)
    repo.add_patient("Ethan", "Clark", 3333333333, "Allergy", 22)

    assert repo.get_patient(0).get_first_name() == "Mark"
    assert repo.get_patient(1).get_pnc() == 4444444444
    assert repo.get_patient(2).get_disease() == "Allergy"

def test_get_patient():
    repo = PatientRepository([
        Patient("John", "Doe", 1234567890, "Flu", 30),
        Patient("Jane", "Smith", 9876543210, "Diabetes", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 25)
    ])

    patient1 = repo.get_patient(0)
    patient2 = repo.get_patient(1)
    patient3 = repo.get_patient(2)

    assert patient1.get_first_name() == "John"
    assert patient2.get_last_name() == "Smith"
    assert patient3.get_age() == 25

def test_update_patient():
    repo = PatientRepository([
        Patient("John", "Doe", 1234567890, "Flu", 30),
        Patient("Jane", "Smith", 9876543210, "Diabetes", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 25)
    ])

    repo.update_patient(0, "Jack", "Davis", 1111111111, "Cold", 32)
    repo.update_patient(1, "Emily", "White", 2222222222, "Migraine", 40)
    repo.update_patient(2, "Liam", "Green", 3333333333, "Flu", 20)

    assert repo.get_patient(0).get_first_name() == "Jack"
    assert repo.get_patient(1).get_disease() == "Migraine"
    assert repo.get_patient(2).get_age() == 20

def test_delete_patient():
    repo = PatientRepository([
        Patient("John", "Doe", 1234567890, "Flu", 30),
        Patient("Jane", "Smith", 9876543210, "Diabetes", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 25)
    ])

    assert repo.get_patient(0).get_first_name() == "John"
    repo.delete_patient(1)
    assert repo.get_patient(1).get_first_name() == "Alice"
    repo.delete_patient(0)
    assert repo.get_patient(0).get_first_name() == "Alice"

if __name__ == "__main__":
    test_add_patient()
    test_get_patient()
    test_update_patient()
    test_delete_patient()
    print("All tests passed")
