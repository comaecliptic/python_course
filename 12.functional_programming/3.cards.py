from itertools import product


print(list(product(
    list(range(2, 11)) + ['J', 'Q', 'K', 'A'],
    ('H', 'C', 'S', 'D')
)))
