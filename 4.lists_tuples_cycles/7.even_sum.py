import numpy as np


interesting_numbers = (3, 2, 5, 7, 14, 26, 32, 31, 37)
interesting_array = np.array(interesting_numbers)
print(interesting_array[interesting_array % 2 == 0].sum())
