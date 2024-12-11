
def remove(score_list : list, index : int):
   """
   Removes an element from the list at a specific index
    Parameters:
    - score_list: The list from which the value will be removed
    - index: The position of the element to remove
    Returns: The updated score list
    """
   if isinstance(index, int) and len(score_list) > index >= 0:
       score_list.remove(score_list[index])
   else:
       print('The given index is not valid.')
   return score_list

def remove_multiple(score_list : list, from_index : int, to_index : int):
    """
    Removes a range of elements from the list, between two indices
    Parameters:
    - score_list: The list from which the range of elements will be removed
    - from_index: The starting position of the range to remove
    - to_index: The ending position of the range to remove
    Returns: The updated score list
    """
    if isinstance(from_index, int) and isinstance(to_index, int) and 0 <= from_index < to_index < len(score_list):
        score_list = score_list[:from_index] + score_list[to_index + 1:]
    else:
        print('The given index is not valid.')
    return score_list


def replace(score_list : list, index : int, new_value : int):
    """
    Replaces the value at a specific index with a new value
    Parameters:
    - score_list: The list where the value will be replaced
    - index: The position of the element to replace
    - new_value: The new integer value to replace the old one
    Returns: The updated score list
    """
    if (isinstance(index, int)) and 0 <= index < len(score_list):
        if (isinstance(new_value, int)) and new_value > 0:
            score_list[index] = new_value
        else:
            print('Value must be a positive integer.')
    else:
        print('Index must be in the range of the set.')
    return score_list



