from collections import Counter
from maximum import maximum


def moda(number_list):
    """Return the most common number or numbers in list.

    Parameters
    ----------
    number_list : list of int or float
        Well, list.
    Returns
    -------
    mode_value : int, float or tuple of int or float
        The most common number/numbers.
    """
    values_counter = Counter(number_list)
    mode_value = []
    count = 0
    max_value = maximum(values_counter.values())
    for key, value in values_counter.items():
        if value == max_value:
            mode_value.append(key)
            count += 1
    if count > 1:
        return tuple(mode_value)
    return mode_value[0]


if __name__ == '__main__':
    print(moda([100, 3, 100, 2, 45, 45, 45, 3, 45, 3, 3, -2, 4]))
