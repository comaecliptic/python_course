complement_table = str.maketrans('atgc', 'TACG')


def reverse_complement(seq):
    """Return reverse complement of DNA sequence in a fancy way.
    Do not raise exception if the sequence has nonDNA characters.
    """
    return seq[::-1].lower().translate(complement_table)


def gene_search(dna_seq):
    """Search DNA sequence for protein-coding
    open reading frames. ORF has following properties:
    - has start codon and stop codon
    - length more than 4 codons
    - the number of nucleotides in ORF is a multiple of three

    Parameters
    ----------
    dna_seq : str
        Input DNA sequence.

    Returns
    -------
    genes : list of str
        List with all ORFs.
    """
    def gene_search_core(dna_seq, length, genes):
        """Core part of gene search. Walk through
        sequence, parse for genes, append to list.

        Parameters
        ----------
        dna_seq : str
            Input DNA sequence.
        length : int
            Length of DNA sequence.
        genes : list of str
            List with genes found.
        """
        i = 0
        while i < length:
            if dna_seq[i:i + 3] == 'ATG':
                for j in range(i, length, 3):
                    if dna_seq[j:j + 3] in {'TAA', 'TAG', 'TGA'}:
                        if len(dna_seq[i:j + 3]) > 12:
                            genes.append(dna_seq[i:j + 3])
                        else:
                            break
            i += 1

    dna_seq = dna_seq.upper()
    genes = []
    length = len(dna_seq)
    reverse_seq = reverse_complement(dna_seq)
    for seq in {dna_seq, reverse_seq}:
        gene_search_core(seq, length, genes)
    return genes


dna = 'atggtaatgtaacaacaacaaccgccgcactgatgtatgggaggagcaactgaatagctg'
assert gene_search(dna) == ['ATGTATGGGAGGAGCAACTGA', 'ATGGGAGGAGCAACTGAATAG']
reverse_dna = reverse_complement(dna)
assert gene_search(dna) == gene_search(reverse_dna)
