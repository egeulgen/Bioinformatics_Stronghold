import sys
from rosalind_utility import parse_fasta
from rosalind_utility import hamming_dist


def distance_matrix(strings):
    """ Calculate the Distance matrix
    :param strings: the input strings
    :return: distance matrix (list of list)
    """
    str_len = len(strings[0])
    dist_mat = []
    for str1 in strings:
        current_row = []
        for str2 in strings:
            current_row.append(hamming_dist(str1, str2) / str_len)
        dist_mat.append(current_row)
    return dist_mat


if __name__ == "__main__":
    '''
    Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA format.
    Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is allowed an absolute error of 0.001.
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_strings = list(parse_fasta(input_lines).values())
    distance_mat = distance_matrix(DNA_strings)

    for row in distance_mat:
        print(' '.join(["%.3f" % x for x in row]))
