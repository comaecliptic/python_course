from itertools import product


def generate(max_len):
    """Generates all possible DNA sequences with length up
    to input.

    Parameters
    ----------
    max_len : int

    Yields
    -------
    dna : str
    """
    for n in range(1, max_len + 1):
        for dna in product('ATGC', repeat=n):
            yield ''.join(dna)


if __name__ == '__main__':
    print(list(generate(2)))
