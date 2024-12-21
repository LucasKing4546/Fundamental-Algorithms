from repository.recipe_repo import *

repo = RecipeRepository()

def print_menu():
    print('Menu:\n')
    print('1: Add recipe')
    print('2: Update recipe')
    print('3: Delete all recipes with a preparation time under 10 minutes')
    print('4: Sort recipe')

def main(choice: int):
    choice = int(input('Enter your choice: '))
    while True:
        if choice == 1:
            id = int(input('Enter the id of the recipe'))
            name = input('Enter the name of the recipe')
            type = input('Enter the type of recipe')
            difficulty = input('Enter the difficulty of the recipe(0 - 5)')
            time = int(input('Enter the time of the recipe'))
            repo.add(id, name, type, difficulty, time)
            print("Recipe added")
        elif choice == 2:
            id = int(input('Enter the id of the recipe'))
            name = input('Enter the name of the recipe')
            type = input('Enter the type of recipe')
            difficulty = input('Enter the difficulty of the recipe(0 - 5)')
            time = int(input('Enter the time of the recipe'))
            repo.update(id, name, type, difficulty, time)
            print("Recipe updated")
        elif choice == 3:
            repo.delete()
            print("Recipes deleted")
        elif choice == 4:





if __name__ == '__main__':
    print_menu()
    while
