from feature_1 import *
from feature_2 import *
from feature_3 import *
from feature_4 import *
from feature_5 import *

stack_lists = []
# 10 examples
score_list = [2, 5, 23, 56, 24, 75, 90, 100, 44, 11]

def get_score_list():
    return list(map(int, input("Enter scores separated by space: ").split()))

def get_score_list_from_file():
    global score_list
    try:
        fin = open("input.txt", "r")
        score_list = list(map(int, fin.readline().split()))
        stack_lists.append(score_list.copy())
        fin.close()
        print()
        display_score_list()
    except IOError as e:
        print("IO error:" + str(e))
    except ValueError as ex:
        print("ValueError error:" + str(ex))

def write_score_list_in_file():
    global score_list
    try:
        fout = open("output.txt", "w")
        fout.write("Current score list: " + str(score_list))
        fout.close()
    except IOError as e:
        print("IO error:" + str(e))
    except ValueError as ex:
        print("ValueError error:" + str(ex))

def add_score_list():
    global score_list, stack_lists
    score_list = get_score_list()
    stack_lists.append(score_list.copy())
    print(f"New score list added: {score_list}")

def display_score_list():
    if score_list:
        print(f"Current score list: {score_list}")
    else:
        print("No score list available.")

def add_value():
    global score_list
    if not score_list:
        print("No score list available.")
        return
    value = int(input("Enter the value to add: "))
    if (isinstance(value, int)) and value > 0:
        score_list = add(score_list, value)
        stack_lists.append(score_list.copy())
        print(f"Added {value}: {score_list}")
    else:
        print('Value must be a positive integer.')


def insert_value():
    global score_list
    if not score_list:
        print("No score list available.")
        return
    index = int(input("Enter the index to insert at: "))
    value = int(input("Enter the value to insert: "))
    if (isinstance(index, int)) and 0 <= index < len(score_list):
        if (isinstance(value, int)) and value > 0:
            score_list = insert(score_list, index, value)
            stack_lists.append(score_list.copy())
            print(f"Inserted {value} at index {index}: {score_list}")
        else:
            print('Value must be a positive integer.')
    else:
        print('Index must be in the range of the set.')



def remove_value():
    global score_list
    if not score_list:
        print("No score list available.")
        return
    index = int(input("Enter the index to remove: "))
    if isinstance(index, int) and len(score_list) > index >= 0:
        score_list = remove(score_list, index)
        stack_lists.append(score_list.copy())
        print(f"Removed element at index {index}: {score_list}")
    else:
        print('The given index is not valid.')



def remove_range():
    global score_list
    if not score_list:
        print("No score list available.")
        return
    from_index = int(input("Enter the starting index: "))
    to_index = int(input("Enter the ending index: "))
    if isinstance(from_index, int) and isinstance(to_index, int) and 0 <= from_index < to_index < len(score_list):
        score_list = remove_multiple(score_list, from_index, to_index)
        stack_lists.append(score_list.copy())
        print(f"Removed elements from index {from_index} to {to_index}: {score_list}")
    else:
        print('The given index is not valid.')


def replace_value():
    global score_list
    if not score_list:
        print("No score list available.")
        return
    new_value = int(input("Enter the value to insert: "))
    index = int(input("Enter the index to remove: "))
    if (isinstance(index, int)) and 0 <= index < len(score_list):
        if (isinstance(new_value, int)) and new_value > 0:
            score_list = replace(score_list, index, new_value)
            stack_lists.append(score_list.copy())
            print(f"Removed element at index {index}: {score_list}")
        else:
            print('Value must be a positive integer.')
    else:
        print('Index must be in the range of the set.')


def filter_multiples():
    global score_list
    if not score_list:
        print("No score list available.")
        return
    value = int(input("Enter the value to filter multiples of: "))
    if (isinstance(value, int)) and value > 0:
        score_list = filter_mul(score_list, value)
        stack_lists.append(score_list.copy())
        print(f"Filtered multiples of {value}: {score_list}")
    else:
        print('Value must be a positive integer.')


def filter_greater_than():
    global score_list
    if not score_list:
        print("No score list available.")
        return
    value = int(input("Enter the value to filter elements greater than: "))
    if (isinstance(value, int)) and value > 0:
        score_list = filter_greater(score_list, value)
        stack_lists.append(score_list.copy())
        print(f"Filtered greater than {value}: {score_list}")
    else:
        print('Value must be a positive integer.')

def calculate_average():
    if not score_list:
        print("No score list available.")
        return
    from_index = int(input("Enter the starting index: "))
    to_index = int(input("Enter the ending index: "))
    if isinstance(from_index, int) and isinstance(to_index, int) and 0 <= from_index < to_index < len(score_list):
        avg_value = avg(score_list, from_index, to_index)
        print(f"Average from index {from_index} to {to_index}: {avg_value}")
    else:
        print('The given index is not valid.')


def find_minimum():
    if not score_list:
        print("No score list available.")
        return
    from_index = int(input("Enter the starting index: "))
    to_index = int(input("Enter the ending index: "))
    if isinstance(from_index, int) and isinstance(to_index, int) and 0 <= from_index < to_index < len(score_list):
        min_value = min(score_list, from_index, to_index)
        print(f"Minimum value from index {from_index} to {to_index}: {min_value}")
    else:
        print('The given index is not valid.')


def multiple():
    if not score_list:
        print("No score list available.")
        return
    value = int(input("Enter the value for which multiples will be found: "))
    from_index = int(input("Enter the starting index: "))
    to_index = int(input("Enter the ending index: "))
    if isinstance(from_index, int) and isinstance(to_index, int) and 0 <= from_index < to_index < len(score_list) and isinstance(value, int):
        multiples = mul(score_list, value, from_index, to_index)
        print(f"Multiple values of {value} from index {from_index} to {to_index}: {multiples}")
    else:
        print('The given index is not valid.')

def sort_list():
    global score_list
    if not score_list:
        print("No score list available.")
        return
    score_list = sorted(score_list)
    stack_lists.append(score_list.copy())
    print(f"Sorted list: {score_list}")


def sort_by_higher():
    if not score_list:
        print("No score list available.")
        return
    value = int(input("Enter the value to filter scores higher than: "))
    if isinstance(value, int):
        sorted_higher = sorted_by_higher_value(score_list, value)
        print(f"Scores higher than {value} (sorted): {sorted_higher}")
    else:
        print('Value must be a positive integer.')


def filter_less_than():
    if not score_list:
        print("No score list available.")
        return
    value = int(input("Enter the value to filter scores less than: "))
    if isinstance(value, int):
        less_than_list = less(score_list, value)
        print(f"Scores less than {value}: {less_than_list}")
    else:
        print('Value must be a positive integer.')

# Feature 6
def undo():
    """
       Removes the most recent list (last entry) from the stack of lists.
       Assumes that 'stack_lists' is a global variable or object imported from the 'main' module.
       Parameters: None
       Returns: The updated stack of lists after removing the last entry.
    """
    global score_list
    if len(stack_lists) > 1:
        stack_lists.pop()
        score_list = stack_lists[-1]
        print("Last action undone.")
    else:
        print("No actions to undo.")