import sys
from rosalind_utility import parse_fasta


def print_matrix(mat):
    for row in mat:
        print(" ".join(map(str, [x if x < 0 else " " + str(x) for x in row])))


def global_alignment_score(str1, str2):
    str1 = "-" + str1
    str2 = "-" + str2

    score_mat = [[0 for j in range(len(str2))] for i in range(len(str1))]
    backtrack_mat = [[None for j in range(len(str2))] for i in range(len(str1))]

    for i in range(len(str2)):
        score_mat[0][i] -= i
        backtrack_mat[0][i] = "l"

    for j in range(len(str1)):
        score_mat[j][0] -= j
        backtrack_mat[j][0] = "u"

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):

            score1 = score_mat[i - 1][j - 1] + (1 if str1[i] == str2[j] else -1)
            score2 = score_mat[i - 1][j] - 1
            score3 = score_mat[i][j - 1] - 1
            score_mat[i][j] = max(score1, score2, score3)
            if score_mat[i][j] == score1:
                backtrack_mat[i][j] = "d"
            elif score_mat[i][j] == score2:
                backtrack_mat[i][j] = "u"
            elif score_mat[i][j] == score3:
                backtrack_mat[i][j] = "l"

    # print_matrix(score_mat)
    j = len(str2) - 1
    i = len(str1) - 1
    return score_mat[i][j], score_mat


if __name__ == "__main__":
    '''
    Given: Two DNA strings s and t in FASTA format, each having length at most 1000 bp.
    Return: The maximum alignment score of a global alignment of s and t, followed by the sum of all elements of the 
    matrix M corresponding to s and t that was defined above. Apply the mismatch score introduced in 
    “Finding a Motif with Modifications”.
    '''
    input_lines = sys.stdin.read().splitlines()
    stringA = list(parse_fasta(input_lines).values())[0]
    stringB = list(parse_fasta(input_lines).values())[1]

    max_score, score_mat = global_alignment_score(stringA, stringB)
    max_score_rev, score_mat_rev = global_alignment_score(stringA[::-1], stringB[::-1])
    print(max_score)

    result = 0
    for j in range(len(stringA)):
        for k in range(len(stringB)):
            left = score_mat[j][k]
            right = score_mat_rev[j][k]
            result += (left + right + (1 if stringA[j] == stringB[k] else -1))

    print(result)