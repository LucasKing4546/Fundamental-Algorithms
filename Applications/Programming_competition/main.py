from console import *


def display_menu():
    print("\nMenu:")
    print("1. Display current score list")
    print("2. Add a new score to the list")
    print("3. Insert a value into the score list")
    print("4. Remove a value from the score list by index")
    print("5. Remove a range of values")
    print("6. Replace a value from the score list by index")
    print("7. Filter multiples of a value")
    print("8. Filter elements greater than a value")
    print("9. Get average of a range")
    print("10. Get minimum value in a range")
    print("11. Sort score list")
    print("12. Get scores higher than a value (sorted)")
    print("13. Get elements less than a value")
    print("14. Get all multiples of a given value in a range")
    print("15. Undo last action")
    print("16. Replace the current score list with the list from a file")
    print("17. Write in the output file the current score list")
    print("18. Exit")


def main():
    if score_list is None:
        add_score_list()
    stack_lists.append(score_list.copy())
    print(f"New score list added: {score_list}")

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        print()
        if choice == '1':
            display_score_list()
        elif choice == '2':
            add_value()
        elif choice == '3':
            insert_value()
        elif choice == '4':
            remove_value()
        elif choice == '5':
            remove_range()
        elif choice == '6':
            replace_value()
        elif choice == '7':
            filter_multiples()
        elif choice == '8':
            filter_greater_than()
        elif choice == '9':
            calculate_average()
        elif choice == '10':
            find_minimum()
        elif choice == '11':
            sort_list()
        elif choice == '12':
            sort_by_higher()
        elif choice == '13':
            filter_less_than()
        elif choice == '14':
            multiple()
        elif choice == '15':
            undo()
        elif choice == '16':
            get_score_list_from_file()
        elif choice == '17':
            write_score_list_in_file()
        elif choice == '18':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
