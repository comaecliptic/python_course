def binary_search(number, sorted_list):
    """Perform binary search on pre-sorted list  of numbers
    for given element and return its index of None
    if element is absent.

    Parameters
    ----------
    number : int, float
        Desired number.
    sorted_list : list of int or list of float
        Pre-sorted number list.

    Returns
    -------
    int or None
        Index of desired element in list.
    """
    length = len(sorted_list)
    middle_idx = int(length / 2)
    if sorted_list[middle_idx] == number:
        return middle_idx
    elif length == 1:
        return None
    elif sorted_list[middle_idx] > number:
        return binary_search(number, sorted_list[:middle_idx])
    else:
        result = binary_search(number, sorted_list[middle_idx:])
        if result:
            return middle_idx + result
        return result


assert binary_search(42, [12, 13, 15, 20, 34, 42, 56, 70]) == 5
assert binary_search(42, [12, 13, 15, 20, 34, 41, 56, 70]) is None
