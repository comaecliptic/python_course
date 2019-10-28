complement_table = str.maketrans('atgc', 'TACG')
complement_dict = {
    'a': 'T',
    't': 'A',
    'g': 'C',
    'c': 'G',
}


def short_method(seq):
    """Return reverse complement of DNA sequence in a fancy way.
    Do not raise exception if the sequence has nonDNA characters.
    """
    return seq[::-1].translate(complement_table)


def long_method(seq):
    """Return reverse complement of DNA sequence, but with more code.
    Raise exception if the sequence has nonDNA characters.
    """
    reverse_complement = ''
    for i in seq[::-1]:
        if i == 'a':
            reverse_complement += 'T'
        elif i == 't':
            reverse_complement += 'A'
        elif i == 'c':
            reverse_complement += 'G'
        elif i == 'g':
            reverse_complement += 'C'
        else:
            raise ValueError('Not a DNA sequence!')
    return reverse_complement


def dict_method(seq):
    reverse_complement = ''
    for i in seq[::-1]:
        if i in complement_dict:
            reverse_complement += complement_dict[i]
        else:
            raise ValueError('Not a DNA sequence!')
    return reverse_complement


while True:
    dna = input('Enter DNA sequence to get its reverse complement or "exit" to escape.\n').lower()
    if dna != 'exit':
        method = input('Select method: "1", "2" or "3":\n')
        if method == '1':
            reverse_complement = short_method(dna)
            print(f'First method: {reverse_complement}', end='\n\n')
        elif method == '2':
            reverse_complement = long_method(dna)
            print(f'Second method: {reverse_complement}', end='\n\n')
        elif method == '3':
            reverse_complement = dict_method(dna)
            print(f'Third method: {reverse_complement}', end='\n\n')
        else:
            print('Wrong method key.')
    else:
        print('Bye!')
        break
