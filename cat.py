import sys
from rosalind_utility import parse_fasta

memo = {}


def catalan(seq):
    if len(seq) == 0 or len(seq) == 1:
        return 1

    total = 0
    if seq in memo:
        return memo[seq]

    for i in range(1, len(seq), 2):
        if ((seq[0] == 'A' and seq[i] == 'U') or
                (seq[0] == 'U' and seq[i] == 'A') or
                (seq[0] == 'C' and seq[i] == 'G') or
                (seq[0] == 'G' and seq[i] == 'C')):
            total += catalan(seq[1:i]) * catalan(seq[i + 1:])

    memo[seq] = total % 10 ** 6
    return memo[seq]


if __name__ == "__main__":
    '''
    Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C'
    as 'G'. The length of the string is at most 300 bp.
    Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, 
    modulo 1,000,000.
    '''
    input_lines = sys.stdin.read().splitlines()
    RNA_string = list(parse_fasta(input_lines).values())[0]
    print(catalan(RNA_string))
