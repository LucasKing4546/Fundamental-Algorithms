from heapq import merge

from domain.recipe import *

class RecipeRepository:
    def __init__(self, repo: list['Recipe']|None):
        if repo is None:
            self.__repo = []
        else:
            self.__repo = repo


    def add(self, id, name, type, difficulty, time):
        if isinstance(id, int) and id not in [x.get_id() for x in self.__repo] and isinstance(name, str) and len(name) >= 1 and type in cuisine and isinstance(difficulty, int) and isinstance(time, int) and time >= 1:
            self.__repo.append(Recipe(id, name, type, difficulty, time))
        else:
            if not(isinstance(id, int) and id not in [x.get_id() for x in self.__repo]):
                raise TypeError("Recipe ID is not valid")
            elif not isinstance(name, str):
                raise TypeError("Recipe name is not valid")
            elif type not in cuisine:
                raise TypeError("Recipe type is not valid")
            elif not isinstance(difficulty, int):
                raise TypeError("Recipe difficulty is not valid")
            elif not isinstance(time, int) or time < 1:
                raise TypeError("Recipe time is not valid")

    def update(self, id, name, type, difficulty, time):
        for x in self.__repo:
            if x.get_id() == id:
                if time >= 1:
                    x.set_name(name)
                    x.set_type(type)
                    x.set_difficulty(difficulty)
                    x.set_time(time)
                else:
                    raise TypeError("Recipe preparation time is not valid")

    def delete(self):
        for i in reversed(range(len(self.__repo))):
            if self.__repo[i].get_time() < 10:
                self.__repo.pop(i)

    def merge(self, left: int, mid: int, right: int, key = lambda x: x, relation = lambda a, b: a > b):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = key(self.__repo[left + i])

        for j in range(n2):
            R[j] = key(self.__repo[mid + j])

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if relation(R[j], L[i]):
                self.__repo[k] = L[i]
                i += 1
            else :
                self.__repo[k] = R[j]
                j += 1
            k+=1

        while i < n1:
            self.__repo[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            self.__repo[k] = R[j]
            j += 1
            k += 1

    def sorting(self, left, right, key = lambda x: x, relation = lambda a, b: a > b):
        if left < right:
            mid = (left + right) // 2
            self.sorting(left, right, key, relation)
            self.sorting(left, mid, right, key, relation)
            merge(left, mid, right, key, relation)




