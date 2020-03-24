from Bio import SeqIO
from Bio.SeqUtils import GC
from collections import Counter
import matplotlib.pyplot as plt


class FastaStats:
    """Class for extracting different statistics from
    .fasta file.

    Parameters
    ----------
    filepath : str
        Path to a .fasta file
    """
    def __init__(self, filepath):
        self.path = filepath

    def seq_count(self):
        """Gets number of sequences in file

        Returns
        -------
        count : int
        """
        if getattr(self, 'count', None) is not None:
            return self.count
        else:
            self.count = 0
            for record in SeqIO.parse(self.path, 'fasta'):
                self.count += 1
            return self.count

    def length_distribution(self):
        """Plots histogram of sequences lengths in file.
        """
        if getattr(self, 'lengths', None) is None:
            self.lengths = []
            for record in SeqIO.parse(self.path, 'fasta'):
                self.lengths.append(len(record.seq))
        plt.hist(self.lengths)
        plt.xlabel('Sequences lengths')
        plt.ylabel('Frequency')
        plt.title('Histogram of sequences lengths')
        plt.show()

    def calculate_gc(self):
        """Computes average GC percentage among all sequences.

        Returns
        -------
        gc_content : float
        """
        if getattr(self, 'gc_content', None) is None:
            self.gc_content = 0
            for record in SeqIO.parse(self.path, 'fasta'):
                self.gc_content += GC(record.seq)
            self.gc_content /= self.seq_count()
        return self.gc_content

    def kmer_distribution(self, k=4):
        """Plots histogram of k-mer distribution in all
        sequences.

        Parameters
        ----------
        k : int
            k-mer size. Default is 4.
        """
        kmer_numbers = Counter()
        for record in SeqIO.parse(self.path, 'fasta'):
            for k in range(len(record.seq) - 4):
                kmer = record.seq[k:k+4]
                kmer_numbers[kmer] += 1
        plt.hist(kmer_numbers.values())
        plt.xlabel('k-mer counts')
        plt.ylabel('Frequency')
        plt.title('K-mer distribution')
        plt.show()

    def __str__(self):
        return self.path


if __name__ == '__main__':
    stats = FastaStats('..\\12.functional_programming\\salmon_gill_poxvirus.fasta')
    print(f'File path: {stats}')
    print(f'Sequence count: {stats.seq_count()}')
    print(f'Average GC content: {stats.calculate_gc()}')
    stats.length_distribution()
    stats.kmer_distribution()
