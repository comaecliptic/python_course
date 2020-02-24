from Bio import SeqIO
from Bio.Data import CodonTable


standard_codon_table = CodonTable.unambiguous_dna_by_name["Standard"]


def translate_fasta(path, codon_table=standard_codon_table):
    """Generator to translate sequences in .fasta-file.

    Parameters
    ----------
    path : str
        Path to .fasta-file
    codon_table : dict or dict-like
        Mapping from codons to aminoacids.

    Yields
    -------
    protein : str
        Protein sequence
    """
    for record in SeqIO.parse(path, 'fasta'):
        protein = translate(record.seq, codon_table)
        yield protein


def translate(dna_seq, codon_table):
    """Translates DNA sequence to protein.

    Parameters
    ----------
    dna_seq : str
        DNA sequence.
    codon_table : dict or dict-like
        Mapping from codons to aminoacids.

    Returns
    -------
    protein : str
        Protein sequence.
    """
    i = 0
    dna_len = len(dna_seq)
    while i < dna_len:
        if dna_seq[i:i + 3] in codon_table.start_codons:
            for j in range(i, dna_len, 3):
                if dna_seq[j:j + 3] in codon_table.stop_codons:
                    gene = dna_seq[i:j]
                    codon_list = [gene[i:i + 3] for i in range(0, len(gene), 3)]
                    aminoacid_list = [codon_table.forward_table[codon] for codon in codon_list]
                    protein = ''.join(aminoacid_list)
                    return protein
        i += 1
    return 'No protein encoded in this sequence.'


if __name__ == '__main__':
    salmon_gill_poxvirus_proteins = translate_fasta('salmon_gill_poxvirus.fasta')
    for protein in salmon_gill_poxvirus_proteins:
        print(protein)
