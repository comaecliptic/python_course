import matplotlib.pyplot as plt
import numpy as np


trials = [np.random.randint(0, 100, 1000) for _ in range(5)]
plt.boxplot(trials, widths=0.5)
plt.title('Boxplot on random data from uniform distribution')
plt.xlabel('Trials')
plt.ylabel('Random numbers from [0, 100)')
plt.show()
