import numpy as np


array_1 = np.array([1, 2, 3, 4, 56, 789])
array_2 = np.full(15, 42)
array_3 = np.zeros(21)

for array in (array_1, array_2, array_3):
    print(array)
