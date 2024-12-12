from domain.hospital import Departments
from domain.patient import Patient
from repository.hospital_repo import DepartmentsRepository

def test_add_department():
    repo = DepartmentsRepository([])
    repo.add_department(1, "Cardiology", 10, [
        Patient("John", "Doe", 1234567890, "Heart Issue", 55)])
    repo.add_department(2, "Neurology", 8, [
        Patient("Jane", "Smith", 9876543210, "Migraine", 45)])
    repo.add_department(3, "Pediatrics", 15, [
        Patient("Alice", "Johnson", 1122334455, "Asthma", 12)])

    assert repo.get_department(0).get_name() == "Cardiology"
    assert repo.get_department(1).get_name() == "Neurology"
    assert repo.get_department(2).get_number_of_beds() == 15

def test_get_department():
    repo = DepartmentsRepository([
        Departments(1, "Cardiology", 10, [
            Patient("John", "Doe", 1234567890, "Heart Issue", 55)]),
        Departments(2, "Neurology", 8, [
            Patient("Jane", "Smith", 9876543210, "Migraine", 45)]),
        Departments(3, "Pediatrics", 15, [
            Patient("Alice", "Johnson", 1122334455, "Asthma", 12)])
    ])

    dep1 = repo.get_department(0)
    dep2 = repo.get_department(1)
    dep3 = repo.get_department(2)

    assert dep1.get_name() == "Cardiology"
    assert dep2.get_number_of_beds() == 8
    assert dep3.get_list_of_patients()[0].get_first_name() == "Alice"

def test_update_department():
    repo = DepartmentsRepository([
        Departments(1, "Cardiology", 10, [
            Patient("John", "Doe", 1234567890, "Heart Issue", 55)]),
        Departments(2, "Neurology", 8, [
            Patient("Jane", "Smith", 9876543210, "Migraine", 45)]),
        Departments(3, "Pediatrics", 15, [
            Patient("Alice", "Johnson", 1122334455, "Asthma", 12)])
    ])

    repo.update_department(0, "Updated Cardiology", 12, [
        Patient("Mark", "Taylor", 5555555555, "Arrhythmia", 60)])
    repo.update_department(1, "Updated Neurology", 9, [
        Patient("Sophia", "Brown", 4444444444, "Seizures", 40)])
    repo.update_department(2, "Updated Pediatrics", 20, [
        Patient("Ethan", "Clark", 3333333333, "Bronchitis", 8)])

    assert repo.get_department(0).get_name() == "Updated Cardiology"
    assert repo.get_department(1).get_list_of_patients()[0].get_disease() == "Seizures"
    assert repo.get_department(2).get_number_of_beds() == 20

def test_delete_department():
    repo = DepartmentsRepository([
        Departments(1, "Cardiology", 10, [
            Patient("John", "Doe", 1234567890, "Heart Issue", 55)]),
        Departments(2, "Neurology", 8, [
            Patient("Jane", "Smith", 9876543210, "Migraine", 45)]),
        Departments(3, "Pediatrics", 15, [
            Patient("Alice", "Johnson", 1122334455, "Asthma", 12)])
    ])

    repo.delete_department(1)
    assert repo.get_department(0).get_name() == "Cardiology"

    repo.delete_department(1)
    assert repo.get_department(0).get_name() == "Cardiology"

    repo.delete_department(0)
    assert len(repo.get_all_departments()) == 0

def test_sorting_departments():
    repo = DepartmentsRepository([
        Departments(1, "Cardiology", 10, [
            Patient("John", "Doe", 1234567890, "Heart Issue", 55)]),
        Departments(2, "Neurology", 8, [
            Patient("Jane", "Smith", 9876543210, "Migraine", 45),
            Patient("Alice", "Johnson", 1122334455, "Asthma", 12)]),
        Departments(3, "Pediatrics", 15, [
            Patient("Ethan", "Clark", 3333333333, "Bronchitis", 8)])
    ])

    repo.sorting_departments("patient")

    assert repo.get_department(0).get_name() == "Cardiology"
    assert repo.get_department(2).get_name() == "Neurology"

    repo.sorting_departments("id")
    assert repo.get_department(2).get_id() == 3

test_add_department()
test_get_department()
test_update_department()
test_delete_department()
test_sorting_departments()
