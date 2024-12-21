from domain.hospital import Departments
from domain.patient import Patient

def sorting (arr : list[Patient | Departments], key = lambda x: x, relation = lambda a, b: a > b):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if relation(key(arr[i]), key(arr[j])):
                arr[i], arr[j] = arr[j], arr[i]

def filtering (arr : list[Patient | Departments], key = lambda x: x):
    return [x for x in arr if key(x)]

def backtrack(k: int, current_group: list[Patient|Departments], start: int, set_identifier: set, elements: list[Patient|Departments], results, key = lambda x: x):
    if len(current_group) == k:
        results.append(current_group[:])
        return
    for i in range(start, len(elements)):
        element = elements[i]
        if key(element) not in set_identifier:
            current_group.append(element)
            set_identifier.add(key(element))
            backtrack(k, current_group, i + 1, set_identifier, elements, results, key)
            current_group.pop()
            set_identifier.remove(key(element))

def different_diseases(department: Departments):
    diseases = set()
    for patient in department.get_list_of_patients().get_all_patients():
        diseases.add(patient.get_disease())
    return diseases


'''

def backtrack_patients(k: int, current_group: list[Patient], start: int, set_pnc: set, patients: list[Patient], results):
    if len(current_group) == k:
        results.append(current_group)
        return
    for i in range(start, len(current_group)):
        patient = patients[i]
        if patient.get_pnc() not in set_pnc:
            current_group.append(patient)
            set_pnc.add(patient.get_pnc())
            backtrack_patients(k, current_group, i + 1, set_pnc, patients, results)
            current_group.pop()
            set_pnc.remove(patient.get_pnc())
    return results

def backtrack_departments(k: int, current_group: list[Departments], start: int, set_id: set, departments: list[Departments], results):
    if len(current_group) == k:
        results.append(current_group)
        return
    for i in range(start, len(current_group)):
        department = departments[i]
        if department.get_id() not in set_id:
            current_group.append(department)
            set_id.add(department.get_id())
            backtrack_departments(k, current_group, i + 1, set_id, departments, results)
            current_group.pop()
            set_id.remove(department.get_id())
    return results

'''