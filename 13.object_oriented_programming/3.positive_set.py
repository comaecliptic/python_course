class PositiveSet(set):
    """Set modification that can contain only positive numbers.
    """
    def __init__(self, args):
        args = [x for x in args if (isinstance(x, int) or isinstance(x, float)) and x > 0]
        super().__init__(args)

    def add(self, new_elem):
        if (isinstance(new_elem, int) or isinstance(new_elem, float)) and new_elem > 0:
            super().add(new_elem)

    #def __str__(self):
    #    print(self.__dict__)
    #    return '{' + ', '.join(self) + '}'


if __name__ == '__main__':
    a = PositiveSet((1, 2, 3.3, -4, 16, 0, 'adf'))
    print(f'Initial set: {a}')
    a.add(56)
    a.add(-6)
    a.add('dsddg')
    print(f'With new elements: {a}')
