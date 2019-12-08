import sys


def rev_comp(string):
    ''' Create reverse complement of the string
    :param string: DNA string to rev. comp. (string)
    :return: the reverse complement (string)
    '''
    revc_seq = string[::-1].translate(str.maketrans("ACGT", "TGCA"))
    return revc_seq


if __name__ == "__main__":
    '''
    Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement sc of s.
    '''
    DNA_string = sys.stdin.read().splitlines()[0]
    print(rev_comp(DNA_string))
