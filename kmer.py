import sys
from rosalind_utility import parse_fasta
from lexf import alpha_combs


def kmer_comp(string, k = 4):
    all_kmers = alpha_combs(["A", "C", "G", "T"], k, )
    result = {}
    for kmer in all_kmers:
        result[kmer] = 0
    for i in range(len(string) - k + 1):
        kmer = string[i:i + k]
        result[kmer] += 1
    return result


if __name__ == "__main__":
    '''
    Given: A DNA string s in FASTA format (having length at most 100 kbp).
    Return: The 4-mer composition of s.
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_string = list(parse_fasta(input_lines).values())[0]
    
    composition = list(kmer_comp(DNA_string).values())
    print(' '.join(map(str, composition)))
