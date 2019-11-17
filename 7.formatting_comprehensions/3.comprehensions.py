squares = [i ** 2 for i in range(11)]
print(squares)

sums = [a + b for a, b in zip(range(4), range(5, 9))]
print(sums)

nucleotide_dict = {
    'A': ['C', 'T', 'G']
}
nucleotide_conversions = [
    f'{n}->{m}' for n in ('A', 'T', 'G', 'C') for m in ('A', 'T', 'G', 'C') if n != m
]
print(nucleotide_conversions)

matrix = [[x for x in range(y, y + 3)] for y in range(0, 9, 3)]
print(matrix)
