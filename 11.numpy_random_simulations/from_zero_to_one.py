import numpy as np
import random
import timeit
import matplotlib.pyplot as plt


amount_of_numbers = 1
max_amount = int(input('Enter amount of numbers: '))
random_time_list = []
numpy_time_list = []
while amount_of_numbers <= max_amount:
    random_time = timeit.timeit(
        stmt='[random.random() for _ in range(amount_of_numbers)]',
        setup='import random',
        globals=globals(),
        number=100000,
    )
    numpy_time = timeit.timeit(
        stmt='np.random.random(amount_of_numbers).tolist()',
        setup='import numpy as np',
        globals=globals(),
        number=100000,
    )
    random_time_list.append(random_time)
    numpy_time_list.append(numpy_time)
    amount_of_numbers += 1

all_amounts = [x for x in range(1, amount_of_numbers)]
plt.plot(all_amounts, random_time_list, label='random module')
plt.plot(all_amounts, numpy_time_list, label='numpy module')
plt.title('Modules performance in calculating random numbers from [0.0, 1.0)')
plt.xlabel('Amount of numbers')
plt.ylabel('Time to calculate')
plt.legend()
plt.show()
