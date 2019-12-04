import sys


def hamming_dist(seq1, seq2):
    ''' Calculate Hamming Distance
    :param seq1: sequence 1 (string)
    :param seq2: sequence 2 (string)
    :return: the hamming distance bw/ seq1 and seq2 (integer)
    '''
    h_dist = sum([x != y for x, y in zip(seq1, seq2)])
    return h_dist


if __name__ == "__main__":
    '''
    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
    Return: The Hamming distance dH(s,t).
    '''
    input_list = sys.stdin.read().splitlines()
    s1 = input_lines[0]
    s2 = input_lines[1]
    print(hamming_dist(s1, s2))
