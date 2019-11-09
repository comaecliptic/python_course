def flatten(initial_list):
    """Get list with internal lists and return flattened list
    with all elements at the same level.

    Parameters
    ----------
    initial_list : list
        A list to flatten.

    Returns
    -------
    flattened_list : list
        Flattened list.
    """
    result_list = []
    for element in initial_list:
        if isinstance(element, list):
            result_list.extend(flatten(element))
        else:
            result_list.append(element)
    return result_list


if __name__ == '__main__':
    complicated_list = [1, [1, 2], 3, [[4, 5, [6]]]]
    print(flatten(complicated_list))
