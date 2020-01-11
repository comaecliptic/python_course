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
    direction = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7])
    randomly_chosen_point = start_points[direction]
    last_point = np.array(last_point)
    new_point = (2 * randomly_chosen_point + last_point) / 3
    return new_point


if __name__ == '__main__':
    number_of_iterations = int(input('Enter number of iterations: '))
    all_points = []

    first_point = np.random.randint(-100, 101, size=2)
    side_length = np.random.randint(1, 101)
    second_point = np.array([first_point[0] + side_length, first_point[1]])
    third_point = np.array([second_point[0], second_point[1] + side_length])
    forth_point = np.array([third_point[0] - side_length, third_point[1]])
    all_points.extend([first_point, second_point, third_point, forth_point])

    middle_points = []
    for i in range(-3, 1):
        middle_points.append((all_points[i - 1] + all_points[i]) / 2)
    all_points.extend(middle_points)

    new_point = np.random.randint(-100, 101, size=2)
    all_points.append(new_point)
    for i in range(number_of_iterations):
        new_point = add_new_point(all_points[:8], new_point)
        all_points.append(new_point)

    graph_points = [tuple(i) for i in all_points]
    x_points, y_points = zip(*graph_points)
    plt.scatter(x_points, y_points)
    plt.gca().set_aspect('equal')
    plt.show()
