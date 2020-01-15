import numpy as np
import matplotlib.pyplot as plt


def random_walk(start_point):
    """Walks 1 step into random direction.

    Parameters
    ----------
    start_point : np.array of int
        x and y coordinates of starting point.

    Returns
    -------
    new_point : np.array of int
        x and y coordinates of new point.
    """
    directions = {
        1: np.array((0, 1)),    # up
        2: np.array((0, -1)),   # down
        3: np.array((-1, 0)),   # left
        4: np.array((1, 0))     # right
    }
    step = np.random.choice(list(directions.keys()))
    new_point = start_point + directions[step]
    return new_point


if __name__ == '__main__':
    start_point = np.array((0, 0))
    step_number = int(input('Enter number of steps: '))
    all_points = [start_point]
    for _ in range(step_number):
        start_point = random_walk(start_point)
        all_points.append(tuple(start_point))
    x_points, y_points = zip(*all_points)
    plt.plot(x_points, y_points)
    plt.show()
