from domain.hospital import Departments
from domain.patient import Patient

def sorting (arr : list[Patient | Departments], key = lambda x: x, relation = lambda a, b: a > b):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if relation(key(arr[i]), key(arr[j])):
                arr[i], arr[j] = arr[j], arr[i]

def filtering (arr : list[Patient | Departments], key = lambda x: x):
    return [x for x in arr if key(x)]