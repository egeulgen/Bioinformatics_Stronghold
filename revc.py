import sys


def rev_comp(sequence):
    ''' Create reverse complement of the sequence
    :param sequence: DNA sequence to rev. comp. (string)
    :return: the reverse complement (string)
    '''
    revc_seq = sequence[::-1].translate(str.maketrans("ACGT", "TGCA"))
    return revc_seq


if __name__ == "__main__":
    '''
    Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement sc of s.
    '''
    DNA_seq = sys.stdin.read().splitlines()[0]
    print(rev_comp(DNA_seq))
