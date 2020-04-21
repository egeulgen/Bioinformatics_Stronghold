import sys
from rosalind_utility import parse_fasta


def edit_distance_alignment_num(str1, str2):
    modulus = 2 ** 27 - 1

    str1 = "-" + str1
    str2 = "-" + str2

    score_mat = [[0 for i in range(len(str2))] for j in range(len(str1))]
    count_mat = [[0 for i in range(len(str2))] for j in range(len(str1))]

    for i in range(len(str2)):
        score_mat[0][i] = i
        count_mat[0][i] = 1

    for j in range(len(str1)):
        score_mat[j][0] = j
        count_mat[j][0] = 1

    for i in range(1, len(str2)):
        for j in range(1, len(str1)):
            score1 = score_mat[j - 1][i - 1] + (0 if str1[j] == str2[i] else 1)
            score2 = score_mat[j - 1][i] + 1
            score3 = score_mat[j][i - 1] + 1
            score_mat[j][i] = min(score1, score2, score3)
            if score_mat[j][i] == score1:
                count_mat[j][i] += count_mat[j - 1][i - 1]
            if score_mat[j][i] == score2:
                count_mat[j][i] += count_mat[j - 1][i]
            if score_mat[j][i] == score3:
                count_mat[j][i] += count_mat[j][i - 1]
            count_mat[j][i] = count_mat[j][i] % modulus

    return count_mat[len(str1) - 1][len(str2) - 1]


if __name__ == "__main__":
    '''
    Given: Two protein strings s and t in FASTA format, each of length at most 1000 aa.
    Return: The total number of optimal alignments of s and t with respect to edit alignment score, 
    modulo 134,217,727 (227-1).
    '''
    input_lines = sys.stdin.read().splitlines()
    stringA = list(parse_fasta(input_lines).values())[0]
    stringB = list(parse_fasta(input_lines).values())[1]

    print(edit_distance_alignment_num(stringA, stringB))