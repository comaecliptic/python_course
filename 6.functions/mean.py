def mean(number_list):
    """Return mean value of the list.

    Parameters
    ----------
    number_list : list of int or float
        List with numbers.
    Returns
    -------
    mean_value : float
        Mean value.
    """
    mean_value = 0
    length = 0
    for i in number_list:
        mean_value += i
        length += 1
    mean_value /= length
    return mean_value


if __name__ == '__main__':
    print(mean([100, 2, 3, 45, -2, 4]))
