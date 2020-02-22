from Bio.Data import CodonTable


class RNAHandler:
    """A class to work with RNA sequences. Supports translation
    and reverse transcription. Initial sequence supposed to be
    5'-3'-directed.
    """

    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.length = len(self.sequence)
        self.translation_table = CodonTable.unambiguous_rna_by_name["Standard"]
        self.reverse_transcription_table = str.maketrans('AUGC', 'TACG')

    def translate(self):
        """Translates RNA sequence in all reading frames.

        Returns
        -------
        proteins : list of str
            List of all proteins that can be obtained from this sequence.
        """
        i = 0
        genes = []
        while i < self.length:
            if self.sequence[i:i + 3] in self.translation_table.start_codons:
                for j in range(i, self.length, 3):
                    if self.sequence[j:j + 3] in self.translation_table.stop_codons:
                        genes.append(self.sequence[i:j])
                        break
            i += 1
        proteins = []
        for gene in genes:
            codon_list = [gene[i:i+3] for i in range(0, len(gene), 3)]
            aminoacid_list = [self.translation_table.forward_table[codon] for codon in codon_list]
            protein = ''.join(aminoacid_list)
            proteins.append(protein)
        return proteins

    def reverse_transcribe(self):
        """Returns a complement DNA copy of RNA.
        """
        return self.sequence.translate(self.reverse_transcription_table)


if __name__ == '__main__':
    test_rna = RNAHandler(
        'auggagggccaugucaagcgccccaugaaugcauuuaugguguggucccguggagagagg'
        'cgcaaguuggcucaacagaaucccagcaugcagaauucagagaucagcaagcaucuggga'
        'uaucaguggaaaagccuuacagaagccgaaaaaaggcccuuuuuccaggaggcgcagaga'
        'cugaagacccuacacagagagaaauauccaaacuauaaauaucagccucaucgaaggguu'
        'aaagugccacagaggaguuauacuuugcagcgugaaguugccucaacaaaacuguacaac'
        'cugcugcaaugggacaacaaccuacacacuaucauauacggacaggacugggcuagagcu'
        'gcacaccaguccuccaagaaccagaaaagcauuuauuuacagccuguggacauccccacu'
        'ggauacccacuacagcagaaacagcagcaccagcagcagcagcacgugcaccugcagcag'
        'cagcagcagcagcagcaccaguuccacuag'
    )
    print(test_rna.translate())
    print(test_rna.reverse_transcribe())
