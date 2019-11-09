def reverse(list_to_reverse):
    """Get list and return it in reverse order.

    Parameters
    ----------
    list_to_reverse : list
        List.
    Returns
    -------
    reversed_list : list
        List, but in reversed order.
    """
    return list_to_reverse[::-1]


if __name__ == '__main__':
    print(reverse([100, 2, 3, 45, -2, 4]))
