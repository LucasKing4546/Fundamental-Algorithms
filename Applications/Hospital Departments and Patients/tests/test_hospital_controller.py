from domain.hospital import Departments
from domain.patient import Patient
from repository.hospital_repo import DepartmentsRepository
from infrastructure.hospital_controller import HospitalController


def test_sort_patients_by_pnc():
    repo = DepartmentsRepository([
        Departments(1, "Cardiology", 10, [
            Patient("John", "Doe", 1234567890, "Heart Issue", 55),
            Patient("Alice", "Johnson", 1122334455, "Asthma", 12)]),
        Departments(2, "Neurology", 8, [
            Patient("Jane", "Smith", 9876543210, "Migraine", 45),
            Patient("Zane", "Taylor", 6677889900, "Headache", 35)]),
        Departments(3, "Pediatrics", 15, [
            Patient("Ethan", "Clark", 3333333333, "Bronchitis", 8),
            Patient("Grace", "Lee", 5566778899, "Flu", 10)])
    ])
    controller = HospitalController(repo)
    controller.sort_patients_by_pnc(0)
    controller.sort_patients_by_pnc(1)
    controller.sort_patients_by_pnc(2)

    assert repo.get_department(0).get_list_of_patients()[0].get_first_name() == "Alice"
    assert repo.get_department(1).get_list_of_patients()[0].get_first_name() == "Zane"
    assert repo.get_department(2).get_list_of_patients()[0].get_first_name() == "Ethan"


def test_sort_by_number_of_patients():
    repo = DepartmentsRepository([
        Departments(1, "Cardiology", 10, [
            Patient("John", "Doe", 1234567890, "Heart Issue", 55)]),
        Departments(2, "Neurology", 8, [
            Patient("Jane", "Smith", 9876543210, "Migraine", 45),
            Patient("Zane", "Taylor", 6677889900, "Headache", 35)]),
        Departments(3, "Pediatrics", 15, [
            Patient("Ethan", "Clark", 3333333333, "Bronchitis", 8)])
    ])
    controller = HospitalController(repo)
    controller.sort_by_number_of_patients()

    # Asserts based on the 3 departments
    assert repo.get_department(0).get_name() == "Cardiology"
    assert repo.get_department(1).get_name() == "Pediatrics"
    assert repo.get_department(2).get_name() == "Neurology"


def test_sort_by_number_of_patient_over_an_age():
    repo = DepartmentsRepository([
        Departments(1, "Cardiology", 10, [
            Patient("John", "Doe", 1234567890, "Heart Issue", 55)]),
        Departments(2, "Neurology", 8, [
            Patient("Jane", "Smith", 9876543210, "Migraine", 45),
            Patient("Zane", "Taylor", 6677889900, "Headache", 35)]),
        Departments(3, "Pediatrics", 15, [
            Patient("Ethan", "Clark", 3333333333, "Bronchitis", 8),
            Patient("Grace", "Lee", 5566778899, "Flu", 10)])
    ])
    controller = HospitalController(repo)
    controller.sort_by_number_of_patient_over_an_age(30)

    # Asserts based on the 3 departments
    assert len(repo.get_department(0).get_list_of_patients()) == 0
    assert len(repo.get_department(1).get_list_of_patients()) == 1
    assert len(repo.get_department(2).get_list_of_patients()) == 2


def test_get_departments_patients_under_an_age():
    repo = DepartmentsRepository([
        Departments(1, "Cardiology", 10, [
            Patient("John", "Doe", 1234567890, "Heart Issue", 55)]),
        Departments(2, "Neurology", 8, [
            Patient("Jane", "Smith", 9876543210, "Migraine", 45),
            Patient("Zane", "Taylor", 6677889900, "Headache", 35)]),
        Departments(3, "Pediatrics", 15, [
            Patient("Ethan", "Clark", 3333333333, "Bronchitis", 8),
            Patient("Grace", "Lee", 5566778899, "Flu", 10)])
    ])
    controller = HospitalController(repo)
    departments = controller.get_departments_patients_under_an_age(40)

    # Asserts based on the 3 departments
    assert departments[0].get_name() == "Neurology"
    assert departments[1].get_name() == "Pediatrics"
    assert len(departments[1].get_list_of_patients()) == 2


def test_get_departments_patient_first_name():
    repo = DepartmentsRepository([
        Departments(1, "Cardiology", 10, [
            Patient("John", "Doe", 1234567890, "Heart Issue", 55)]),
        Departments(2, "Neurology", 8, [
            Patient("Jane", "Smith", 9876543210, "Migraine", 45),
            Patient("Zane", "Taylor", 6677889900, "Headache", 35)]),
        Departments(3, "Pediatrics", 15, [
            Patient("Ethan", "Clark", 3333333333, "Bronchitis", 8),
            Patient("Grace", "Lee", 5566778899, "Flu", 10)])
    ])
    controller = HospitalController(repo)
    departments = controller.get_departments_patient_first_name("Grace")

    assert len(departments) == 1
    assert departments[0].get_name() == "Pediatrics"
    assert departments[0].get_list_of_patients()[1].get_first_name() == "Grace"


def test_get_patients_first_or_last_name():
    repo = DepartmentsRepository([
        Departments(1, "Cardiology", 10, [
            Patient("John", "Doe", 1234567890, "Heart Issue", 55)]),
        Departments(2, "Neurology", 8, [
            Patient("Jane", "Smith", 9876543210, "Migraine", 45),
            Patient("Zane", "Taylor", 6677889900, "Headache", 35)]),
        Departments(3, "Pediatrics", 15, [
            Patient("Ethan", "Clark", 3333333333, "Bronchitis", 8),
            Patient("Grace", "Lee", 5566778899, "Flu", 10)])
    ])
    controller = HospitalController(repo)
    patients = controller.get_patients_first_or_last_name(1, "ane")

    assert len(patients) == 2
    assert patients[0].get_first_name() == "Jane"
    assert patients[1].get_last_name() == "Taylor"


test_sort_patients_by_pnc()
test_sort_by_number_of_patients()
test_sort_by_number_of_patient_over_an_age()
test_get_departments_patients_under_an_age()
test_get_departments_patient_first_name()
test_get_patients_first_or_last_name()
