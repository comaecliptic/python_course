def my_or(p, q):
    return p or q


def my_and(p, q):
    return p and q


def xor(p, q):
    return p != q


def nor(p, q):
    return not (p or q)


def nand(p, q):
    return not (p and q)


def make_unary_table():
    print('P | not P\n1 |   0\n0 |   1')


def make_binary_table(operation, operator):
    print(f'P | Q | P {operator} Q')
    for p in [True, False]:
        for q in [True, False]:
            print(f'{int(p)} | {int(q)} |    {int(operation(p, q))}')


c = None
while c != 'exit':
    print("Type operation to get its' truth table. Type 'exit' to escape.")
    c = input().lower()
    if c == 'not':
        make_unary_table()
    elif c == 'or':
        make_binary_table(my_or, c)
    elif c == 'and':
        make_binary_table(my_and, c)
    elif c == 'xor':
        make_binary_table(xor, c)
    elif c == 'nor':
        make_binary_table(nor, c)
    elif c == 'nand':
        make_binary_table(nand, c)
    elif c == 'exit':
        print('Exiting...')
    else:
        print('Wrong command.')