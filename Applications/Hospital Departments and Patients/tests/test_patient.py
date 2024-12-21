from domain.patient import Patient

patient1 = Patient("John", "Doe", 1234567890, "Flu", 30)
patient2 = Patient("Jane", "Smith", 9876543210, "Diabetes", 45)
patient3 = Patient("Alice", "Johnson", 1122334455, "Asthma", 25)

def reset_patients(p1, p2, p3):
    p1.set_first_name("John")
    p1.set_last_name("Doe")
    p1.set_pnc(1234567890)
    p1.set_disease("Flu")
    p1.set_age(30)

    p2.set_first_name("Jane")
    p2.set_last_name("Smith")
    p2.set_pnc(9876543210)
    p2.set_disease("Diabetes")
    p2.set_age(45)

    p3.set_first_name("Alice")
    p3.set_last_name("Johnson")
    p3.set_pnc(1122334455)
    p3.set_disease("Asthma")
    p3.set_age(25)

def test_get_first_name():
    assert patient1.get_first_name() == "John"
    assert patient2.get_first_name() == "Jane"
    assert patient3.get_first_name() == "Alice"

def test_get_last_name():
    assert patient1.get_last_name() == "Doe"
    assert patient2.get_last_name() == "Smith"
    assert patient3.get_last_name() == "Johnson"

def test_get_pnc():
    assert patient1.get_pnc() == 1234567890
    assert patient2.get_pnc() == 9876543210
    assert patient3.get_pnc() == 1122334455

def test_get_disease():
    assert patient1.get_disease() == "Flu"
    assert patient2.get_disease() == "Diabetes"
    assert patient3.get_disease() == "Asthma"

def test_get_age():
    assert patient1.get_age() == 30
    assert patient2.get_age() == 45
    assert patient3.get_age() == 25

def test_set_first_name():
    reset_patients(patient1, patient2, patient3)
    patient1.set_first_name("Lucas")
    assert patient1.get_first_name() == "Lucas"
    patient2.set_first_name("Paul")
    assert patient2.get_first_name() == "Paul"
    patient3.set_first_name("Victor")
    assert patient3.get_first_name() == "Victor"

def test_set_last_name():
    reset_patients(patient1, patient2, patient3)
    patient1.set_last_name("Secara")
    assert patient1.get_last_name() == "Secara"
    patient2.set_last_name("Popescu")
    assert patient2.get_last_name() == "Popescu"
    patient3.set_last_name("Ardelean")
    assert patient3.get_last_name() == "Ardelean"

def test_set_pnc():
    reset_patients(patient1, patient2, patient3)
    patient1.set_pnc(7174171212)
    assert patient1.get_pnc() == 7174171212
    patient2.set_pnc(1274577152)
    assert patient2.get_pnc() == 1274577152
    patient3.set_pnc(9876543210)
    assert patient3.get_pnc() == 9876543210

def test_set_disease():
    reset_patients(patient1, patient2, patient3)
    patient1.set_disease("Diabetes")
    assert patient1.get_disease() == 'Diabetes'
    patient2.set_disease("Asthma")
    assert patient2.get_disease() == 'Asthma'
    patient3.set_disease("Flu")
    assert patient3.get_disease() == 'Flu'

def test_set_age():
    reset_patients(patient1, patient2, patient3)
    patient1.set_age(45)
    assert patient1.get_age() == 45
    patient2.set_age(30)
    assert patient2.get_age() == 30
    patient3.set_age(10)
    assert patient3.get_age() == 10

if __name__ == "__main__":
    test_get_age()
    test_set_age()
    test_get_pnc()
    test_set_pnc()
    test_get_disease()
    test_set_disease()
    test_get_first_name()
    test_set_first_name()
    test_get_last_name()
    test_set_last_name()
    print("All tests passed")


