import numpy as np
import matplotlib.pyplot as plt
import timeit


def is_sorted(list_of_numbers):
    """Checks if the list of numbers is sorted
    in ascending order.

    Parameters
    ----------
    list_of_numbers : list of int or float

    Returns
    -------
    bool
    """
    for i in range(len(list_of_numbers) - 1):
        if list_of_numbers[i] > list_of_numbers[i + 1]:
            return False
    return True


def monkey_sort(list_of_numbers):
    """Performs random shuffling of elements of numbers list
    until it is ordered.

    Parameters
    ----------
    list_of_numbers : list of int or float
    """
    while not is_sorted(list_of_numbers):
        np.random.shuffle(list_of_numbers)


if __name__ == '__main__':
    list_size = 2
    mean_time_of_sort = []
    std_of_sort = []
    number_of_runs = int(input('Enter number of runs: '))
    while list_size <= 10:
        runs = []
        for i in range(number_of_runs):
            time_of_run = timeit.timeit(
                stmt='monkey_sort(test_list)',
                setup='import numpy as np; test_list = list(np.random.randint(0, 10, list_size))',
                globals=globals(),
                number=1,
            )
            runs.append(time_of_run)
        mean_time_of_sort.append(np.mean(runs))
        std_of_sort.append(np.std(runs))
        list_size += 1

    all_sizes = [_ for _ in range(2, 11)]
    plt.errorbar(all_sizes, mean_time_of_sort, std_of_sort)
    plt.title('Performance of monkey sort by list size')
    plt.xlabel('Length of the list')
    plt.ylabel(f'Time needed mean of {number_of_runs} runs')
    plt.show()
