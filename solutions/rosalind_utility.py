def parse_fasta(lines):
    ''' Parse FASTA format
    :param lines: list of lines in FASTA format
    :return: dictionary of sequences
    '''
    sequences = {}
    tmp_seq = ""
    tmp_name = ""
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


def rev_comp(string):
    ''' Create reverse complement of the string
    :param string: DNA sequence to rev. comp. (string)
    :return: the reverse complement (string)
    '''
    revc_seq = string[::-1].translate(str.maketrans("ACGT", "TGCA"))
    return revc_seq


def hamming_dist(string1, string2):
    ''' Calculate Hamming Distance between strings
    :param string1: string 1 (string)
    :param string2: string 2 (string)
    :return: the hamming distance bw/ string1 and string2 (integer)
    '''
    return sum([x != y for x, y in zip(string1, string2)])
