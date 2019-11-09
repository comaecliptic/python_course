def fibo(n):
    """Return nth Fibonacci number.

    Parameters
    ----------
    n : int
        A number of Fibonacci number in the sequence.

    Returns
    -------
    f_n : int
        nth Fibonacci number.
    """
    f_n = 0
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            f_n = 1
        else:
            f_n = fibo(i - 1) + fibo(n - 2)
    return f_n


if __name__ == '__main__':
    while True:
        number = input(
            """Enter a number of place in Fibonacci sequence to get it's value. Type 'exit' to escape.\n""")
        if number == 'exit':
            break
        else:
            print(fibo(int(number)))
