import sys
from rosalind_utility import parse_fasta


def edit_distance(str1, str2):
    str1 = "-" + str1
    str2 = "-" + str2

    score_mat = [[0 for i in range(len(str2))] for j in range(len(str1))]

    for i in range(len(str2)):
        score_mat[0][i] = i

    for j in range(len(str1)):
        score_mat[j][0] = j

    for i in range(1, len(str2)):
        for j in range(1, len(str1)):
            if str1[j - 1] == str2[i - 1]:
                score1 = score_mat[j - 1][i - 1]
            else:
                score1 = score_mat[j - 1][i - 1] + 1
            score2 = score_mat[j - 1][i] + 1
            score3 = score_mat[j][i - 1] + 1
            score_mat[j][i] = min(score1, score2, score3)

    return score_mat[len(str1) - 1][len(str2) - 1]


if __name__ == "__main__":
    '''
    Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).
    Return: The edit distance dE(s,t).
    '''
    input_lines = sys.stdin.read().splitlines()
    stringA = list(parse_fasta(input_lines).values())[0]
    stringB = list(parse_fasta(input_lines).values())[1]

    print(edit_distance(stringA, stringB))