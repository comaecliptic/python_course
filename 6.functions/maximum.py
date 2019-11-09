def maximum(numbers_list):
    """Return the biggest number in the list.

    Parameters
    ----------
    numbers_list : list of int or float
        List with digits.
    Returns
    -------
    m : int or float
        Maximum value in list.
    """
    m = None
    for i in numbers_list:
        if m is None or i > m:
            m = i
    return m


if __name__ == '__main__':
    print(maximum([100, 2, 3, 45, -2, 4]))
