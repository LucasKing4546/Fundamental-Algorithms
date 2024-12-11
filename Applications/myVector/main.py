from My_Vector import MyVector
from My_Vector import colors
from repo import VectorRepository

def print_menu():
    print("\nMenu")
    print("1: Add vector to the repository")
    print("2: Get all vectors")
    print("3: Get a vector at a given index")
    print("4: Update a vector at a given index")
    print("5: Update a vector by name")
    print("6: Delete a vector by index")
    print("7: Delete a vector by name")
    print("8: Plot all vectors")
    print("9: Get the max of all vectors having the sum greater than a given value")
    print("10:. Delete all vectors for which the product of elements is greater than a given value ")
    print("11:. Update the color on all vectors by a given type")
    print("12: Exit")

def main():
    repo = VectorRepository()
    v1 = MyVector('v1', 'b', 1, [1, 2, 3])
    v2 = MyVector('v2', 'r', 2, [4, 5, 6])
    v3 = MyVector('v3', 'y', 3, [1, -2, 3])
    repo.add_vector(v1)
    repo.add_vector(v2)
    repo.add_vector(v3)
    print_menu()
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter the name of the vector: ")
            color = input("Enter the color of the vector: ")
            type = int(input("Enter the type of vector: "))
            values = [int(x) for x in input("Enter the values of the vector: ").split(" ")]
            print(len(values))
            if isinstance(name, int|str) and color in colors and isinstance(type, int|str) and len(values) == 3:
                repo.add_vector(MyVector(name, color, type, values))
                print("Vector added successfully")
            else:
                print("One of the parameters is not valid")
        elif choice == "2":
            print(repo.get_vectors())
        elif choice == "3":
            index = int(input("Enter the index of the vector: "))
            print(repo.get_vector_by_index(index))
        elif choice == "4":
            name = input("Enter the name of the vector: ")
            color = input("Enter the color of the vector: ")
            type = int(input("Enter the type of vector: "))
            values = [int(x) for x in input("Enter the values of the vector: ").split(" ")]
            index = int(input("Enter the index of the vector: "))
            if isinstance(name, int | str) and color in colors and isinstance(type, int | str) and len(values) == 3 and 0 <= index < len(repo.get_vectors()):
                repo.update_by_index(index, MyVector(name, color, type, values))
                print("Vector updated successfully")
            else:
                print("One of the parameters is not valid")
        elif choice == "5":
            name = input("Enter the name of the vector: ")
            color = input("Enter the color of the vector: ")
            type = int(input("Enter the type of vector: "))
            values = [int(x) for x in input("Enter the values of the vector: ").split(" ")]
            if isinstance(name, int | str) and color in colors and isinstance(type, int | str) and len(values) == 3:
                repo.update_by_name(name, MyVector(name, color, type, values))
                print("Vector updated successfully")
            else:
                print("One of the parameters is not valid")
        elif choice == "6":
            index = int(input("Enter the index of the vector: "))
            if 0 <= index < len(repo.get_vectors()):
                repo.delete_by_index(index)
                print("Vector deleted successfully")
            else:
                print("The index is not valid")
        elif choice == "7":
            name = input("Enter the name of the vector: ")
            if isinstance(name, int|str):
                repo.delete_by_name(name)
                print("Vector deleted successfully")
            else:
                print("The name is not valid")
        elif choice == "8":
            if len(repo.get_vectors()) == 0:
                print("The repository is empty")
            else:
                repo.plot_vectors()
        elif choice == "9":
            value = int(input("Enter the value: "))
            print(repo.max_sum_greater_than_value(value))
        elif choice == "10":
            value = int(input("Enter the value: "))
            print(repo.delete_product_greater_than_value(value))
        elif choice == "11":
            type = int(input("Enter the type of vectors: "))
            color = input("Enter the new color of the vectors: ")
            if isinstance(type, int) and color in colors:
                repo.update_by_type(type, color)
        elif choice == "12":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")



if __name__ == '__main__':
    main()