import sys
from rosalind_utility import hamming_dist

if __name__ == "__main__":
    '''
    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
    Return: The Hamming distance dH(s,t).
    '''
    input_lines = sys.stdin.read().splitlines()
    s1 = input_lines[0]
    s2 = input_lines[1]
    print(hamming_dist(s1, s2))
