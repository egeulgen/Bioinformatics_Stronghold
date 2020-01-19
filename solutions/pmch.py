import sys
from rosalind_utility import parse_fasta
from math import factorial


if __name__ == "__main__":
    '''
    Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
    Return: A longest common substring of the collection. (If multiple solutions exist, you may return any 
    single solution.)
    '''
    input_lines = sys.stdin.read().splitlines()
    strings_dict = parse_fasta(input_lines)
    RNA = list(strings_dict.values())[0]
    print(factorial(RNA.count("A")) * factorial(RNA.count("C")))
