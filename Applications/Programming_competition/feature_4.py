def avg(score_list: list, from_index: int, to_index: int) -> float:
    """
    Calculates the average of elements in the list between two indices (inclusive).
    Parameters:
    - score_list: The list of scores to be averaged.
    - from_index: The starting index for the range.
    - to_index: The ending index for the range.
    Returns: The average of the elements in the specified range as a float.
    """
    suma = 0
    if isinstance(from_index, int) and isinstance(to_index, int) and 0 <= from_index < to_index < len(score_list):
        for i in range(from_index, to_index + 1):
            suma += score_list[i]
        suma /= (to_index - from_index + 1)
    else:
        print('The given index is not valid.')
    return suma

def min(score_list: list, from_index: int, to_index: int) -> int:
    """
    Finds the minimum value in the list between two indices (inclusive).
    Parameters:
    - score_list: The list of scores to be checked.
    - from_index: The starting index for the range.
    - to_index: The ending index for the range.
    Returns: The minimum value found within the specified range as an integer.
    """

    minim = 101
    if isinstance(from_index, int) and isinstance(to_index, int) and 0 <= from_index < to_index < len(score_list):
        for i in range(from_index, to_index + 1):
            if score_list[i] < minim:
                minim = score_list[i]
    else:
        print('The given index is not valid.')
    return minim

def mul(score_list: list, value: int, from_index: int, to_index: int) -> list:
    """
    Finds all multiples of a given value in the list between two indices (inclusive).
    Parameters:
    - score_list: The list of scores to be checked.
    - value: The integer value for which multiples will be found.
    - from_index: The starting index for the range.
    - to_index: The ending index for the range.
    Returns: A list of elements from score_list that are multiples of the specified value within the given range.
    """
    multiples = []
    if isinstance(from_index, int) and isinstance(to_index, int) and 0 <= from_index < to_index < len(score_list) and isinstance(value, int):
        for i in range(from_index, to_index + 1):
            if score_list[i] % value == 0:
                multiples.append(score_list[i])
    else:
        print('The given index is not valid.')
    return multiples