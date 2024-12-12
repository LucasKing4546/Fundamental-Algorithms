from domain.hospital import Departments

def test_get_id():
    department1 = Departments(1, "Cardiology", 20, ["John", "Jane", "Alice"])
    department2 = Departments(2, "Neurology", 15, ["Bob", "Eve", "Charlie"])
    department3 = Departments(3, "Oncology", 10, ["Dave", "Clara", "Emily"])

    assert department1.get_id() == 1
    assert department2.get_id() == 2
    assert department3.get_id() == 3

def test_get_name():
    department1 = Departments(1, "Cardiology", 20, ["John", "Jane", "Alice"])
    department2 = Departments(2, "Neurology", 15, ["Bob", "Eve", "Charlie"])
    department3 = Departments(3, "Oncology", 10, ["Dave", "Clara", "Emily"])

    assert department1.get_name() == "Cardiology"
    assert department2.get_name() == "Neurology"
    assert department3.get_name() == "Oncology"

def test_get_number_of_beds():
    department1 = Departments(1, "Cardiology", 20, ["John", "Jane", "Alice"])
    department2 = Departments(2, "Neurology", 15, ["Bob", "Eve", "Charlie"])
    department3 = Departments(3, "Oncology", 10, ["Dave", "Clara", "Emily"])

    assert department1.get_number_of_beds() == 20
    assert department2.get_number_of_beds() == 15
    assert department3.get_number_of_beds() == 10

def test_get_list_of_patients():
    department1 = Departments(1, "Cardiology", 20, ["John", "Jane", "Alice"])
    department2 = Departments(2, "Neurology", 15, ["Bob", "Eve", "Charlie"])
    department3 = Departments(3, "Oncology", 10, ["Dave", "Clara", "Emily"])

    assert department1.get_list_of_patients() == ["John", "Jane", "Alice"]
    assert department2.get_list_of_patients() == ["Bob", "Eve", "Charlie"]
    assert department3.get_list_of_patients() == ["Dave", "Clara", "Emily"]

def test_set_id():
    department1 = Departments(1, "Cardiology", 20, ["John", "Jane", "Alice"])
    department2 = Departments(2, "Neurology", 15, ["Bob", "Eve", "Charlie"])
    department3 = Departments(3, "Oncology", 10, ["Dave", "Clara", "Emily"])

    department1.set_id(4)
    department2.set_id(5)
    department3.set_id(6)

    assert department1.get_id() == 4
    assert department2.get_id() == 5
    assert department3.get_id() == 6

def test_set_name():
    department1 = Departments(1, "Cardiology", 20, ["John", "Jane", "Alice"])
    department2 = Departments(2, "Neurology", 15, ["Bob", "Eve", "Charlie"])
    department3 = Departments(3, "Oncology", 10, ["Dave", "Clara", "Emily"])

    department1.set_name("Dermatology")
    department2.set_name("Pediatrics")
    department3.set_name("Radiology")

    assert department1.get_name() == "Dermatology"
    assert department2.get_name() == "Pediatrics"
    assert department3.get_name() == "Radiology"

def test_set_number_of_beds():
    department1 = Departments(1, "Cardiology", 20, ["John", "Jane", "Alice"])
    department2 = Departments(2, "Neurology", 15, ["Bob", "Eve", "Charlie"])
    department3 = Departments(3, "Oncology", 10, ["Dave", "Clara", "Emily"])

    department1.set_number_of_beds(30)
    department2.set_number_of_beds(25)
    department3.set_number_of_beds(12)

    assert department1.get_number_of_beds() == 30
    assert department2.get_number_of_beds() == 25
    assert department3.get_number_of_beds() == 12

def test_set_list_of_patients():
    department1 = Departments(1, "Cardiology", 20, ["John", "Jane", "Alice"])
    department2 = Departments(2, "Neurology", 15, ["Bob", "Eve", "Charlie"])
    department3 = Departments(3, "Oncology", 10, ["Dave", "Clara", "Emily"])

    department1.set_list_of_patients(["Mike", "Anna"])
    department2.set_list_of_patients(["Sara", "Tom"])
    department3.set_list_of_patients(["Chris", "Laura"])

    assert department1.get_list_of_patients() == ["Mike", "Anna"]
    assert department2.get_list_of_patients() == ["Sara", "Tom"]
    assert department3.get_list_of_patients() == ["Chris", "Laura"]

test_get_id()
test_get_name()
test_get_number_of_beds()
test_get_list_of_patients()
test_set_id()
test_set_name()
test_set_number_of_beds()
test_set_list_of_patients()
