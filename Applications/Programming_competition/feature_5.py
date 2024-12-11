from feature_4 import mul

def filter_mul(score_list: list, value: int) -> list:
    """
    Filters the score list to include only multiples of a given value.
    This function uses the 'mul' function from the imported module to get all multiples of the specified value.
    Parameters:
    - score_list: The list of scores to be filtered.
    - value: The integer value for which multiples will be found.
    Returns: A filtered list containing only the multiples of the specified value.
    """
    if (isinstance(value, int)) and value > 0:
        score_list = mul(score_list, value, 0, len(score_list)-1)
    else:
        print('Value must be a positive integer.')
    return score_list


def filter_greater(score_list: list, value: int) -> list:
    """
    Removes all elements greater than the specified value from the score list.
    Parameters:
    - score_list: The list of scores to be filtered.
    - value: The threshold value for comparison.
    Returns: The updated list with all elements greater than the specified value removed.
    """
    if (isinstance(value, int)) and value >=0:
        temp = []
        for element in score_list:
            if int(element) > value:
                temp.append(element)
        score_list = temp
    else:
        print('Value must be a positive integer.')
    return score_list
