import sys
from rosalind_utility import parse_fasta

memo = {}


def modified_motzkin(seq):
    if len(seq) in [0, 1]:
        return 1

    if seq in memo:
        return memo[seq]

    memo[seq] = modified_motzkin(seq[1:])
    for i in range(1, len(seq)):
        if ((seq[0] == "A" and seq[i] == "U") or
                (seq[0] == "U" and seq[i] == "A") or
                (seq[0] == "C" and seq[i] == "G") or
                (seq[0] == "G" and seq[i] == "C")):
            memo[seq] += modified_motzkin(seq[1:i]) * modified_motzkin(seq[i+1:])
    memo[seq] %= int(1e6)
    return memo[seq]


if __name__ == "__main__":
    '''
    Given: An RNA string s of length at most 300 bp.
    Return: The total number of noncrossing matchings of basepair edges in the bonding graph of s, modulo 1,000,000.
    '''
    input_lines = sys.stdin.read().splitlines()
    rna_seq = list(parse_fasta(input_lines).values())[0]
    print(modified_motzkin(rna_seq))
