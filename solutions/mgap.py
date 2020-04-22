import sys
from rosalind_utility import parse_fasta


def max_gap_symbols(str1, str2):
    str1 = "-" + str1
    str2 = "-" + str2

    score_mat = [[0 for i in range(len(str2))] for j in range(len(str1))]

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                score_mat[i][j] = score_mat[i - 1][j - 1] + 1
            else:
                score_mat[i][j] = max(score_mat[i][j -1], score_mat[i - 1][j])

    return len(str1) - 1 + len(str2) - 1 - 2 * score_mat[len(str1) - 1][len(str2) - 1]


if __name__ == "__main__":
    '''
    Given: Two DNA strings s and t in FASTA format (each of length at most 5000 bp).
    Return: The maximum number of gap symbols that can appear in any maximum score alignment of s and t with score 
    parameters satisfying m>0, d<0, and g<0.
    '''
    input_lines = sys.stdin.read().splitlines()
    stringA = list(parse_fasta(input_lines).values())[0]
    stringB = list(parse_fasta(input_lines).values())[1]

    print(max_gap_symbols(stringA, stringB))
