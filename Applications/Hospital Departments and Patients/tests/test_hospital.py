from domain.hospital import Departments
from domain.patient import Patient
from repository.patient_repo import PatientRepository

def test_get_id():
    department1 = Departments(1, "Cardiology", 20, PatientRepository([
        Patient("John", "Doe", 1234567890, "Heart Issue", 55),
        Patient("Jane", "Smith", 9876543210, "Migraine", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 12)
    ]))
    department2 = Departments(2, "Neurology", 15, PatientRepository([
        Patient("Bob", "Brown", 9988776655, "Seizures", 40),
        Patient("Eve", "White", 8877665544, "Headache", 35),
        Patient("Charlie", "Davis", 7766554433, "Stroke", 50)
    ]))
    department3 = Departments(3, "Oncology", 10, PatientRepository([
        Patient("Dave", "Smith", 6655443322, "Cancer", 60),
        Patient("Clara", "Jones", 5544332211, "Leukemia", 70),
        Patient("Emily", "Clark", 4433221100, "Lymphoma", 65)
    ]))

    assert department1.get_id() == 1
    assert department2.get_id() == 2
    assert department3.get_id() == 3

def test_get_name():
    department1 = Departments(1, "Cardiology", 20, PatientRepository([
        Patient("John", "Doe", 1234567890, "Heart Issue", 55),
        Patient("Jane", "Smith", 9876543210, "Migraine", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 12)
    ]))
    department2 = Departments(2, "Neurology", 15, PatientRepository([
        Patient("Bob", "Brown", 9988776655, "Seizures", 40),
        Patient("Eve", "White", 8877665544, "Headache", 35),
        Patient("Charlie", "Davis", 7766554433, "Stroke", 50)
    ]))
    department3 = Departments(3, "Oncology", 10, PatientRepository([
        Patient("Dave", "Smith", 6655443322, "Cancer", 60),
        Patient("Clara", "Jones", 5544332211, "Leukemia", 70),
        Patient("Emily", "Clark", 4433221100, "Lymphoma", 65)
    ]))

    assert department1.get_name() == "Cardiology"
    assert department2.get_name() == "Neurology"
    assert department3.get_name() == "Oncology"

def test_get_number_of_beds():
    department1 = Departments(1, "Cardiology", 20, PatientRepository([
        Patient("John", "Doe", 1234567890, "Heart Issue", 55),
        Patient("Jane", "Smith", 9876543210, "Migraine", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 12)
    ]))
    department2 = Departments(2, "Neurology", 15, PatientRepository([
        Patient("Bob", "Brown", 9988776655, "Seizures", 40),
        Patient("Eve", "White", 8877665544, "Headache", 35),
        Patient("Charlie", "Davis", 7766554433, "Stroke", 50)
    ]))
    department3 = Departments(3, "Oncology", 10, PatientRepository([
        Patient("Dave", "Smith", 6655443322, "Cancer", 60),
        Patient("Clara", "Jones", 5544332211, "Leukemia", 70),
        Patient("Emily", "Clark", 4433221100, "Lymphoma", 65)
    ]))

    assert department1.get_number_of_beds() == 20
    assert department2.get_number_of_beds() == 15
    assert department3.get_number_of_beds() == 10

def test_get_list_of_patients():
    department1 = Departments(1, "Cardiology", 20, PatientRepository([
        Patient("John", "Doe", 1234567890, "Heart Issue", 55),
        Patient("Jane", "Smith", 9876543210, "Migraine", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 12)
    ]))
    department2 = Departments(2, "Neurology", 15, PatientRepository([
        Patient("Bob", "Brown", 9988776655, "Seizures", 40),
        Patient("Eve", "White", 8877665544, "Headache", 35),
        Patient("Charlie", "Davis", 7766554433, "Stroke", 50)
    ]))
    department3 = Departments(3, "Oncology", 10, PatientRepository([
        Patient("Dave", "Smith", 6655443322, "Cancer", 60),
        Patient("Clara", "Jones", 5544332211, "Leukemia", 70),
        Patient("Emily", "Clark", 4433221100, "Lymphoma", 65)
    ]))
    assert department1.get_list_of_patients().get_all_patients() == [
        Patient("John", "Doe", 1234567890, "Heart Issue", 55),
        Patient("Jane", "Smith", 9876543210, "Migraine", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 12)
    ]

    assert department2.get_list_of_patients().get_all_patients() == [
        Patient("Bob", "Brown", 9988776655, "Seizures", 40),
        Patient("Eve", "White", 8877665544, "Headache", 35),
        Patient("Charlie", "Davis", 7766554433, "Stroke", 50)
    ]
    assert department3.get_list_of_patients().get_all_patients() == [
        Patient("Dave", "Smith", 6655443322, "Cancer", 60),
        Patient("Clara", "Jones", 5544332211, "Leukemia", 70),
        Patient("Emily", "Clark", 4433221100, "Lymphoma", 65)
    ]

def test_set_id():
    department1 = Departments(1, "Cardiology", 20, PatientRepository([
        Patient("John", "Doe", 1234567890, "Heart Issue", 55),
        Patient("Jane", "Smith", 9876543210, "Migraine", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 12)
    ]))
    department2 = Departments(2, "Neurology", 15, PatientRepository([
        Patient("Bob", "Brown", 9988776655, "Seizures", 40),
        Patient("Eve", "White", 8877665544, "Headache", 35),
        Patient("Charlie", "Davis", 7766554433, "Stroke", 50)
    ]))
    department3 = Departments(3, "Oncology", 10, PatientRepository([
        Patient("Dave", "Smith", 6655443322, "Cancer", 60),
        Patient("Clara", "Jones", 5544332211, "Leukemia", 70),
        Patient("Emily", "Clark", 4433221100, "Lymphoma", 65)
    ]))

    department1.set_id(4)
    department2.set_id(5)
    department3.set_id(6)

    assert department1.get_id() == 4
    assert department2.get_id() == 5
    assert department3.get_id() == 6

def test_set_name():
    department1 = Departments(1, "Cardiology", 20, PatientRepository([
        Patient("John", "Doe", 1234567890, "Heart Issue", 55),
        Patient("Jane", "Smith", 9876543210, "Migraine", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 12)
    ]))
    department2 = Departments(2, "Neurology", 15, PatientRepository([
        Patient("Bob", "Brown", 9988776655, "Seizures", 40),
        Patient("Eve", "White", 8877665544, "Headache", 35),
        Patient("Charlie", "Davis", 7766554433, "Stroke", 50)
    ]))
    department3 = Departments(3, "Oncology", 10, PatientRepository([
        Patient("Dave", "Smith", 6655443322, "Cancer", 60),
        Patient("Clara", "Jones", 5544332211, "Leukemia", 70),
        Patient("Emily", "Clark", 4433221100, "Lymphoma", 65)
    ]))

    department1.set_name("Dermatology")
    department2.set_name("Pediatrics")
    department3.set_name("Radiology")

    assert department1.get_name() == "Dermatology"
    assert department2.get_name() == "Pediatrics"
    assert department3.get_name() == "Radiology"

def test_set_number_of_beds():
    department1 = Departments(1, "Cardiology", 20, PatientRepository([
        Patient("John", "Doe", 1234567890, "Heart Issue", 55),
        Patient("Jane", "Smith", 9876543210, "Migraine", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 12)
    ]))
    department2 = Departments(2, "Neurology", 15, PatientRepository([
        Patient("Bob", "Brown", 9988776655, "Seizures", 40),
        Patient("Eve", "White", 8877665544, "Headache", 35),
        Patient("Charlie", "Davis", 7766554433, "Stroke", 50)
    ]))
    department3 = Departments(3, "Oncology", 10, PatientRepository([
        Patient("Dave", "Smith", 6655443322, "Cancer", 60),
        Patient("Clara", "Jones", 5544332211, "Leukemia", 70),
        Patient("Emily", "Clark", 4433221100, "Lymphoma", 65)
    ]))

    department1.set_number_of_beds(30)
    department2.set_number_of_beds(25)
    department3.set_number_of_beds(12)

    assert department1.get_number_of_beds() == 30
    assert department2.get_number_of_beds() == 25
    assert department3.get_number_of_beds() == 12

def test_set_list_of_patients():
    department1 = Departments(1, "Cardiology", 20, PatientRepository([
        Patient("John", "Doe", 1234567890, "Heart Issue", 55),
        Patient("Jane", "Smith", 9876543210, "Migraine", 45),
        Patient("Alice", "Johnson", 1122334455, "Asthma", 12)
    ]))
    department2 = Departments(2, "Neurology", 15, PatientRepository([
        Patient("Bob", "Brown", 9988776655, "Seizures", 40),
        Patient("Eve", "White", 8877665544, "Headache", 35),
        Patient("Charlie", "Davis", 7766554433, "Stroke", 50)
    ]))
    department3 = Departments(3, "Oncology", 10, PatientRepository([
        Patient("Dave", "Smith", 6655443322, "Cancer", 60),
        Patient("Clara", "Jones", 5544332211, "Leukemia", 70),
        Patient("Emily", "Clark", 4433221100, "Lymphoma", 65)
    ]))

    department1.set_list_of_patients(PatientRepository([
        Patient("Mike", "Taylor", 2233445566, "Arrhythmia", 50),
        Patient("Anna", "Wilson", 3344556677, "Flu", 30)
    ]))
    department2.set_list_of_patients(PatientRepository([
        Patient("Sara", "Thomas", 4455667788, "Allergy", 20),
        Patient("Tom", "Brown", 5566778899, "Infection", 25)
    ]))
    department3.set_list_of_patients(PatientRepository([
        Patient("Chris", "Green", 6677889900, "Diabetes", 45),
        Patient("Laura", "White", 7788990011, "Hypertension", 55)
    ]))

    assert department1.get_list_of_patients().get_all_patients() == [
        Patient("Mike", "Taylor", 2233445566, "Arrhythmia", 50),
        Patient("Anna", "Wilson", 3344556677, "Flu", 30)
    ]
    assert department2.get_list_of_patients().get_all_patients() == [
        Patient("Sara", "Thomas", 4455667788, "Allergy", 20),
        Patient("Tom", "Brown", 5566778899, "Infection", 25)
    ]
    assert department3.get_list_of_patients().get_all_patients() == [
        Patient("Chris", "Green", 6677889900, "Diabetes", 45),
        Patient("Laura", "White", 7788990011, "Hypertension", 55)
    ]
if __name__ == '__main__':
    test_get_id()
    test_get_name()
    test_get_number_of_beds()
    test_get_list_of_patients()
    test_set_id()
    test_set_name()
    test_set_number_of_beds()
    test_set_list_of_patients()
    print("All tests passed")