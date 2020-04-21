import sys
from rosalind_utility import rev_comp


def deBruijn(dna_strings):
    long_mers = set()
    for string in dna_strings:
        long_mers.add(string)
        long_mers.add(rev_comp(string))
    result = []
    for mer in long_mers:
        result.append((mer[:len(mer) - 1], mer[1:]))
    return result


if __name__ == "__main__":
    '''
    Given: A collection of up to 1000 (possibly repeating) DNA strings of equal length (not exceeding 50 bp) 
    corresponding to a set S of (k+1)-mers.
    Return: The adjacency list corresponding to the de Bruijn graph corresponding to S∪Src.
    '''
    input_lines = sys.stdin.read().splitlines()

    result = deBruijn(input_lines)

    for r in result:
        print("(" + r[0] + ", " + r[1] + ")")