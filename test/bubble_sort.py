def bubble_sort(lst):
    """Perform bubble sort on list of numbers.
    Return list in ascending order. Sorting is performed inplace.

    Parameters
    ----------
    lst : list of int or float
        Numbers to sort.

    Returns
    -------
    lst : list of int or float
        Numbers in ascending order.
    """
    swapped = False
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            swapped = True
    if swapped:
        bubble_sort(lst)
    return lst


assert bubble_sort([12, 3, 5, 4, 1, 2, ]) == [1, 2, 3, 4, 5, 12, ]
assert bubble_sort([0.99, 0.98, 0.45, 0.3, 0.5, 0.49, ]) == [0.3, 0.45, 0.49, 0.5, 0.98, 0.99, ]
test_inplace = [12, 3, 5, 4, 1, 2, ]
bubble_sort(test_inplace)
assert test_inplace == [1, 2, 3, 4, 5, 12, ]
