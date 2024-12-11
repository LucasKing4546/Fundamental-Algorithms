def less(score_list: list, value: int) -> list:
    """
    Returns a list of scores that are less than a given value.
    Parameters:
    - score_list: The list of scores to be compared.
    - value: The threshold value for comparison.
    Returns: A list containing the elements of score_list that are less than the specified value.
    """
    less_list = []
    if isinstance(value, int):
        for elem in score_list:
            if int(elem) < value:
                less_list.append(elem)
    else:
        print('Value must be a positive integer.')
    return less_list


def sorted(score_list: list) -> list:
    """
    Sorts the list of scores in ascending order.
    Parameters:
    - score_list: The list of scores to be sorted.
    Returns: A new list containing the sorted elements from score_list.
    """
    score_list.sort(key=lambda x: int(x))
    return score_list


def sorted_by_higher_value(score_list: list, value: int) -> list:
    """
    Returns a list of scores greater than a given value, sorted in ascending order.
    Parameters:
    - score_list: The list of scores to be compared.
    - value: The threshold value for comparison.
    Returns: A sorted list containing the elements of score_list that are greater than the specified value.
    """
    higher_list = []
    if isinstance(value, int):
        for elem in score_list:
            if int(elem) > value:
                higher_list.append(elem)
    else:
        print('Value must be a positive integer.')
    return sorted(higher_list)