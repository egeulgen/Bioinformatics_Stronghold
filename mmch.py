import sys
from rosalind_utility import parse_fasta
from math import factorial


def permutation(n, k):
    return factorial(n) // factorial(n-k)


def num_max_matching(string):
    n_A = string.count("A")
    n_U = string.count("U")
    n_C = string.count("C")
    n_G = string.count("G")
    return permutation(max(n_A, n_U), min(n_A, n_U)) * permutation(max(n_C, n_G), min(n_C, n_G))


if __name__ == "__main__":
    '''
    Given: An RNA string s of length at most 100.
    Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.
    '''
    input_lines = sys.stdin.read().splitlines()
    RNA_string = list(parse_fasta(input_lines).values())[0]

    print(num_max_matching(RNA_string))
