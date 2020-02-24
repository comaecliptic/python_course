import numpy as np
from math import log


some_collection = np.random.random_integers(1000, size=100)
print(some_collection)
print(list(map(log, some_collection)))
print(list(map(lambda x: x ** 2, some_collection)))
print(list(map(lambda x: x > 100, some_collection)))
print(list(filter(lambda x: x > 100, some_collection)))
print(list(filter(lambda x: log(x) > 6, some_collection)))
print(list(filter(lambda x: x % 2 == 0, some_collection)))
