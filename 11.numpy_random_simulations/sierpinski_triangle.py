import numpy as np
import matplotlib.pyplot as plt


def add_new_point(start_points, last_point):
    """Adds new point.

    Parameters
    ----------
    start_points : list of np.arrays
        Coordinates of three start point.
    last_point : np.array
        Coordinates of the last added point.

    Returns
    -------
    new_point : np.array
        Coordinates of a new point.
    """
    direction = np.random.choice([0, 1, 2])
    randomly_chosen_point = start_points[direction]
    last_point = np.array(last_point)
    new_point = (randomly_chosen_point + last_point) / 2
    return new_point


if __name__ == '__main__':
    number_of_iterations = int(input('Enter number of iterations: '))
    all_points = [np.random.randint(-100, 101, size=2) for _ in range(3)]
    new_point = np.random.randint(-100, 101, size=2)
    all_points.append(new_point)
    for i in range(number_of_iterations):
        new_point = add_new_point(all_points[:3], new_point)
        all_points.append(new_point)

    graph_points = [tuple(i) for i in all_points]
    x_points, y_points = zip(*graph_points)
    plt.scatter(x_points, y_points)
    plt.show()
