import sys
from rosalind_utility import parse_fasta


def print_matrix(mat):
    for row in mat:
        print(" ".join(map(str, [x if x < 0 else " " + str(x) for x in row])))


def fitting_alignment(str1, str2):
    str1 = "-" + str1
    str2 = "-" + str2

    score_mat = [[0 for j in range(len(str2))] for i in range(len(str1))]
    backtrack_mat = [[None for j in range(len(str2))] for i in range(len(str1))]

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):

            score1 = score_mat[i - 1][j - 1] + (1 if str1[i] == str2[j] else -1)
            score2 = score_mat[i - 1][j] - 1
            score3 = score_mat[i][j - 1] - 1
            score_mat[i][j] = max(score1, score2, score3)
            if score_mat[i][j] == score1:
                backtrack_mat[i][j] = "d"
            if score_mat[i][j] == score2:
                backtrack_mat[i][j] = "u"
            if score_mat[i][j] == score3:
                backtrack_mat[i][j] = "l"

    j = len(str2) - 1
    i = max(enumerate([score_mat[row][j] for row in range(len(str2) - 1, len(str1) - 1)]), key=lambda x: x[1])[0] + len(str2) - 1
    max_score = score_mat[i][j]

    # print_matrix(score_mat)

    aligned_1 = aligned_2 = ""
    while backtrack_mat[i][j] is not None:
        direction = backtrack_mat[i][j]
        if direction == "d":
            aligned_1 = str1[i] + aligned_1
            aligned_2 = str2[j] + aligned_2
            i -= 1
            j -= 1
        elif direction == "u":
            aligned_1 = str1[i] + aligned_1
            aligned_2 = "-" + aligned_2
            i -= 1
        else:
            aligned_1 = "-" + aligned_1
            aligned_2 = str2[j] + aligned_2
            j -= 1

    return max_score, aligned_1, aligned_2


if __name__ == "__main__":
    '''
    Given: Two DNA strings s and t, where s has length at most 10 kbp and t represents a motif of length at most 1 kbp.
    Return: An optimal fitting alignment score with respect to the mismatch score defined above, followed by an optimal
    fitting alignment of a substring of s against t. If multiple such alignments exist, then you may output any one.
    '''
    input_lines = sys.stdin.read().splitlines()
    stringA = list(parse_fasta(input_lines).values())[0]
    stringB = list(parse_fasta(input_lines).values())[1]

    score, aligned_strA, aligned_strB = fitting_alignment(stringA, stringB)

    print(score)
    print(aligned_strA)
    print(aligned_strB)
