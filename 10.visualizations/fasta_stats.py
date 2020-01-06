from Bio import SeqIO
import matplotlib.pyplot as plt
from collections import Counter


def get_seqs_lengths(fasta_input):
    """Return the length distribution of 
    sequences in .fasta file.

    Parameters
    ----------
    fasta_input : str
        Path to a .fasta file.
    """
    length_list = []
    for record in SeqIO.parse(fasta_input, 'fasta'):
        length_list.append(len(record.seq))
    # length_count = Counter(length_list)
    plt.hist(length_list)
    plt.title('Lengths distribution')
    plt.xlabel('Sequence length')
    plt.ylabel('Sequence count')
    plt.show()


if __name__ == '__main__':
    get_seqs_lengths('test.fasta')