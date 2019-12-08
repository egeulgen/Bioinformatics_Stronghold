import sys
from rosalind_utility import parse_fasta

def subseq_indices(string, query):
    ''' Locate Subsequence
    :param string: main string
    :param query: query string
    :return: indices of symbols of query as a subsequence in string
    '''
    positions = [0 for _ in query]
    i = 0
    j = 0
    while i < len(string):
        if string[i] == query[j]:
            positions[j] = i + 1
            i += 1
            j += 1
            if j == len(query):
                break
        else:
            i += 1
    return positions


if __name__ == "__main__":
    '''
    Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
    Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions 
    exist, you may return any one.
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_strings = list(parse_fasta(input_lines).values())
    if len(DNA_strings[0]) > len(DNA_strings[1]):
        idx_list = subseq_indices(DNA_strings[0], DNA_strings[1])
    else:
        idx_list = subseq_indices(DNA_strings[1], DNA_strings[0])
    print(" ".join(map(str, idx_list)))
