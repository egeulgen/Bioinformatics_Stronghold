def parse_fasta(lines):
    ''' Parse FASTA format
    :param lines: list of lines in FASTA format
    :return: dictionary of sequences
    '''
    sequences = {}
    tmp_seq = ""
    for line in lines:
        line = line.rstrip()
        if line.startswith(">"):
            if tmp_seq != "":
                sequences[tmp_name] = tmp_seq
                tmp_seq = ""
            tmp_name = line[1:]
        else:
            tmp_seq += line
    # final seq
    sequences[tmp_name] = tmp_seq
    return sequences


def rev_comp(sequence):
    ''' Create reverse complement of the sequence
    :param sequence: DNA sequence to rev. comp. (string)
    :return: the reverse complement (string)
    '''
    revc_seq = sequence[::-1].translate(str.maketrans("ACGT", "TGCA"))
    return revc_seq


def hamming_dist(seq1, seq2):
    ''' Calculate Hamming Distance
    :param seq1: sequence 1 (string)
    :param seq2: sequence 2 (string)
    :return: the hamming distance bw/ seq1 and seq2 (integer)
    '''
    h_dist = sum([x != y for x, y in zip(seq1, seq2)])
    return h_dist