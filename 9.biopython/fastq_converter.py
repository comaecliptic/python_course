from Bio import SeqIO


def fastq_to_fasta(fastq_input, fasta_output, min_len=50):
    """Convert .fastq file to .fasta keeping only
    sequences with length > min_len.

    Parameters
    ----------
    fastq_input : str
        Path to .fastq file.
    fasta_output : str
        Path to .fasta file.
    min_len : int
        Minimal length to keep sequence.
    """
    fasta_list = []
    for record in SeqIO.parse(fastq_input, 'fastq'):
        if len(record.seq) > min_len:
            fasta_list.append(record)
    SeqIO.write(fasta_list, fasta_output, 'fasta')


if __name__ == '__main__':
    test_input = 'test_input.fastq'
    test_output = 'test_output.fasta'
    fastq_to_fasta(test_input, test_output)
