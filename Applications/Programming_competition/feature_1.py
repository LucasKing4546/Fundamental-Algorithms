
def add(score_list : list, value : int):
    """
    Adds a value to the end of the score list
    Parameters:
    - score_list: The list where the value will be added
    - value: The integer value to add
    Returns: The updated score list
    """
    if (isinstance(value, int)) and value > 0:
        score_list.append(value)
    else:
        print('Value must be a positive integer.')
    return score_list


def insert(score_list : list, index : int, value : int):
    """
    Inserts a value at a specific index
    Parameters:
    - score_list: The list where the value will be inserted
    - index: The position where the value will be inserted
    - value: The integer value to insert
    Returns: The updated score list
    """
    if (isinstance(index, int)) and 0 <= index < len(score_list):
        if (isinstance(value, int)) and value > 0:
            score_list = score_list[:index] + [value] + score_list[index:]
        else:
            print('Value must be a positive integer.')
    else:
        print('Index must be in the range of the set.')
    return score_list
