import matplotlib.pyplot as plt


x = [i for i in range(100)]
y = [i ** 2 for i in range(100)]

plt.plot(x, y)
plt.title('Square function')
plt.xlabel('$x$')
plt.ylabel('$x^2$')
plt.show()