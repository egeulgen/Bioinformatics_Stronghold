import sys


def substr_locs(seq, subseq):
    ''' Locate all occurrences of substring in string
    :param seq: sequence to search within (string)
    :param subseq: subsequence to search for (string)
    :return: the locations of substring occurrences in string (list of integers, 1-based)
    '''
    match_idx = []
    k = len(subseq)
    for i in range(len(seq) - k + 1):
        if seq[i:i+k] == subseq:
            match_idx.append(i + 1)
    return match_idx


if __name__ == "__main__":
    '''
    Given: Two DNA strings s and t (each of length at most 1 kbp).
    Return: All locations of t as a substring of s.
    '''
    input_lines = sys.stdin.read().splitlines()
    s = input_lines[0]
    t = input_lines[1]
    result = (substr_locs(s, t))
    print(' '.join([str(idx) for idx in result]))
