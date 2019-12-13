from Bio import SeqIO


def align_global(filepath, match, mismatch, gap):
    """Performs global alignment on a pair of sequences in
    .fasta file.

    Parameters
    ----------
    filepath : str
        Path to .fasta file.
    match : int
        Score for match.
    mismatch : int
        Score for mismatch.
    gap : int
        Score for gap.

    Returns
    -------
    alignment : tuple of (int, str)
        Alignment score and string. 
    """
    record1, record2 = SeqIO.parse(filepath, 'fasta')
    seq1 = str(record1.seq)
    seq2 = str(record2.seq)
    length1 = len(seq1) + 1
    length2 = len(seq2) + 1
    sim_matrix = [[0 for _ in range(length2)] for _ in range(length1)]

    # fill the alignment matrix with scores
    for i in range(length1):
        for j in range(length2):
            if (i == 0) or (j == 0):
                sim_matrix[i][j] = (i + j) * gap
            if (i != 0) and (j != 0):
                pair = (sim_matrix[i - 1][j - 1] + match if seq1[i - 1] == seq2[j - 1]
                            else sim_matrix[i - 1][j - 1] + mismatch)
                delete = sim_matrix[i - 1][j] + gap
                insert = sim_matrix[i][j - 1] + gap
                sim_matrix[i][j] = max((pair, delete, insert))

    align_score = sim_matrix[i][j]
    print(sim_matrix)

    # backtrack through matrix
    alignment1, alignment2 = '', ''
    i = len(seq1)
    j = len(seq2)
    while (i > 0) and (j > 0):
        local_score = match if seq1[i - 1] == seq2[j - 1] else mismatch
        if sim_matrix[i][j] == sim_matrix[i - 1][j - 1] + local_score:
            alignment1 += seq1[i - 1]
            alignment2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif sim_matrix[i][j] == sim_matrix[i - 1][j] + gap:
            alignment1 += seq1[i - 1]
            alignment2 += '-'
            i -= 1
        else:
            alignment1 += '-'
            alignment2 += seq2[j - 1]
            j -= 1

    align_string = alignment1[::-1] + '\n' + alignment2[::-1]
    return align_score, align_string


if __name__ == '__main__':
    print(align_global(
        filepath='test_align.fasta',
        match=1,
        mismatch=-1,
        gap=-1,
    ))
    