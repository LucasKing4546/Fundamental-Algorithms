import sys
from domain.patient import Patient
from domain.hospital import Departments
from infrastructure.hospital_controller import HospitalController
from infrastructure.patient_controller import PatientController
from repository.hospital_repo import DepartmentsRepository
from repository.patient_repo import PatientRepository


def display_menu():
    print("\n=== Hospital Management System ===")
    print("1. Add Department")
    print("2. View Department")
    print("3. Update Department")
    print("4. Delete Department")
    print("5. Add Patient")
    print("6. View Patient")
    print("7. Update Patient")
    print("8. Delete Patient")
    print("9. Sort Patients by PNC in a Department")
    print("10. Sort Departments by Patient Count")
    print("11. Sort Patients Alphabetically in Departments")
    print("12. Get Departments with Patients Below Age")
    print("13. Get Departments with Patient by First Name")
    print("14. Get Patients by First or Last Name in Department")
    print("15. Form Groups of Patients by Disease")
    print("16. Form Groups of Departments by Patient Limit")
    print("17, View all Patients from a Department")
    print("18. View all Departments")
    print("19. Exit")

def main():
    department_repo = DepartmentsRepository([
        Departments(1, "Cardiology", 10, PatientRepository([
            Patient("John", "Doe", 1234567890, "Heart Issue", 55),
            Patient("Lucas", "Secara", 1243653753, "Heart Issue", 19),
            Patient("Andrei", "Schiop", 2131344224, "Heart Issue", 19)
        ])),
        Departments(2, "Neurology", 8, PatientRepository([
            Patient("Jane", "Smith", 9876543210, "Migraine", 45),
            Patient("Zane", "Taylor", 6677889900, "Headache", 35)
        ])),
        Departments(3, "Pediatrics", 15, PatientRepository([
            Patient("Ethan", "Clark", 3333333333, "Bronchitis", 8),
            Patient("Grace", "Lee", 5566778899, "Flu", 10)
        ]))
    ])
    hospital_controller = HospitalController(department_repo)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                id = int(input("Enter Department ID: "))
                name = input("Enter Department Name: ")
                beds = int(input("Enter Number of Beds: "))
                hospital_controller.add_department_controller(id, name, beds, PatientRepository(None))
                print("Department added successfully!")

            elif choice == "2":
                department_id = int(input("Enter Department ID: "))
                department = hospital_controller.get_department_controller(department_id)
                print(department)

            elif choice == "3":
                department_id = int(input("Enter Department ID to Update: "))
                name = input("Enter New Name: ")
                beds = int(input("Enter New Number of Beds: "))
                hospital_controller.update_department_controller(department_id, name, beds, PatientRepository(None))
                print("Department updated successfully!")

            elif choice == "4":
                department_id = int(input("Enter Department ID to Delete: "))
                hospital_controller.delete_department_controller(department_id)
                print("Department deleted successfully!")

            elif choice == "5":
                department_id = int(input("Enter Department ID: "))
                first_name = input("Enter Patient First Name: ")
                last_name = input("Enter Patient Last Name: ")
                pnc = int(input("Enter Personal Numeric Code (PNC): "))
                disease = input("Enter Disease: ")
                age = int(input("Enter Age: "))
                department_patients = hospital_controller.get_department_controller(department_id).get_list_of_patients().get_all_patients()

                patient_repo = PatientRepository(department_patients)

                patient_controller = PatientController(patient_repo)

                patient_controller.add_patient_controller(first_name, last_name, pnc, disease, age)
                print("Patient added successfully!")

            elif choice == "6":
                department_id = int(input("Enter Department ID: "))
                patient_id = int(input("Enter Patient ID: "))
                department_patients = hospital_controller.get_department_controller(department_id).get_list_of_patients().get_all_patients()
                patient_repo = PatientRepository(department_patients)
                patient_controller = PatientController(patient_repo)
                patient = patient_controller.get_patient_controller(patient_id)
                print(patient)

            elif choice == "7":
                department_id = int(input("Enter Department ID: "))
                patient_id = int(input("Enter Patient ID to Update: "))
                first_name = input("Enter New First Name: ")
                last_name = input("Enter New Last Name: ")
                pnc = int(input("Enter New Personal Numeric Code (PNC): "))
                disease = input("Enter New Disease: ")
                age = int(input("Enter New Age: "))
                department_patients = hospital_controller.get_department_controller(
                    department_id).get_list_of_patients().get_all_patients()
                patient_repo = PatientRepository(department_patients)
                patient_controller = PatientController(patient_repo)
                patient_controller.update_patient_controller(patient_id, first_name, last_name, pnc, disease, age)
                print("Patient updated successfully!")

            elif choice == "8":
                department_id = int(input("Enter Department ID: "))
                patient_id = int(input("Enter Patient ID to Delete: "))
                department_patients = hospital_controller.get_department_controller(
                    department_id).get_list_of_patients().get_all_patients()
                patient_repo = PatientRepository(department_patients)
                patient_controller = PatientController(patient_repo)
                patient_controller.delete_patient_controller(patient_id)
                print("Patient deleted successfully!")

            elif choice == "9":
                department_id = int(input("Enter Department ID to Sort Patients by PNC: "))
                hospital_controller.sort_patients_by_pnc(department_id)
                print("Patients sorted by PNC in the department!")

            elif choice == "10":
                hospital_controller.sort_by_number_of_patients()
                print("Departments sorted by the number of patients!")

            elif choice == "11":
                hospital_controller.sort_by_number_of_patients_and_patients_alphabetically()
                print("Departments and their patients sorted alphabetically!")

            elif choice == "12":
                age = int(input("Enter Age Threshold: "))
                departments = hospital_controller.get_departments_patients_under_an_age(age)
                print("Departments with patients below age", age, ":", departments)

            elif choice == "13":
                first_name = input("Enter First Name: ")
                departments = hospital_controller.get_departments_patient_first_name(first_name)
                print("Departments with patients having the first name", first_name, ":", departments)

            elif choice == "14":
                department_id = int(input("Enter Department ID: "))
                search_string = input("Enter Search String for First or Last Name: ")
                patients = hospital_controller.get_patients_first_or_last_name(department_id, search_string)
                print("Patients with the name containing", search_string, ":", patients)

            elif choice == "15":
                group_size = int(input("Enter Group Size: "))
                groups = hospital_controller.form_group_of_patients(group_size)
                print("Formed groups of patients:", groups)

            elif choice == "16":
                group_size = int(input("Enter Group Size: "))
                max_patients = int(input("Enter Maximum Number of Patients per Disease: "))
                groups = hospital_controller.form_group_of_departments(group_size, max_patients)
                print("Formed groups of departments:", groups)
            elif choice == "17":
                department_id = int(input("Enter Department ID: "))
                department_patients = hospital_controller.get_department_controller(department_id).get_list_of_patients().get_all_patients()
                print(department_patients)

            elif choice == "18":
                print(hospital_controller.get_all_departments_controller())

            elif choice == "19":
                print("Exiting... Goodbye!")
                sys.exit()

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
