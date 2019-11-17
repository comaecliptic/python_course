def linear_search(element, list_of_elements):
    """Search list for element and returns its index
    or None if element is absent.

    Parameters
    ----------
    element : anything
        Desired element.
    list_of_elements : list
        List to perform search.
    Returns
    -------
    int or None
        Index of desired element in list.
    """
    for i, elem in enumerate(list_of_elements):
        if elem == element:
            return i
    return None


assert linear_search(42, [12, 425, 657, 42, 254, 54, 3]) == 3
assert linear_search(42, [12, 425, 657, 83472, 254, 54, 3]) is None
