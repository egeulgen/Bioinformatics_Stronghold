import sys
from edit_distance_kband import ksim_solver


if __name__ == "__main__":
    '''
    Given: A positive integer k (k≤50), a DNA string s of length at most 5 kbp representing a motif, and a DNA string t 
    of length at most 50 kbp representing a genome.
    Return: All substrings t′ of t such that the edit distance dE(s,t′) is less than or equal to k. Each substring 
    should be encoded by a pair containing its location in t followed by its length.
    '''
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])
    stringA = input_lines[1]
    stringB = input_lines[2]

    ksim_solver(stringA, stringB, k)