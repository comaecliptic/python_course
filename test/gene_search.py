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
    dna_seq = dna_seq.upper()
    i = 0
    genes = []
    length = len(dna_seq)
    while i < length:
        if dna_seq[i:i + 3] == 'ATG':
            for j in range(i, length, 3):
                if dna_seq[j:j + 3] in {'TAA', 'TAG', 'TGA'}:
                    if len(dna_seq[i:j+3]) > 12:
                        genes.append(dna_seq[i:j+3])
                    else:
                        break
        i += 1
    return genes


dna = 'atggtaatgtaacaacaacaaccgccgcactgatgtatgggaggagcaactgaatagctg'
assert gene_search(dna) == ['ATGTATGGGAGGAGCAACTGA', 'ATGGGAGGAGCAACTGAATAG']
