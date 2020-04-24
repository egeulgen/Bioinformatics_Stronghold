import sys
from rosalind_utility import parse_fasta


def print_matrix(mat):
    for row in mat:
        print(" ".join(map(str, [x if x < 0 else " " + str(x) for x in row])))


def overlap_alignment(str1, str2):
    str1 = "-" + str1
    str2 = "-" + str2

    score_mat = [[0 for j in range(len(str2))] for i in range(len(str1))]
    backtrace_mat = [[None for j in range(len(str2))] for i in range(len(str1))]

    for j in range(1, len(str2)):
        score_mat[0][j] = score_mat[0][j - 1] - 2
        backtrace_mat[0][j] = "l"

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):

            score1 = score_mat[i - 1][j - 1] + (1 if str1[i] == str2[j] else -2)
            score2 = score_mat[i - 1][j] - 2
            score3 = score_mat[i][j - 1] - 2
            score_mat[i][j] = max(score1, score2, score3)
            if score_mat[i][j] == score1:
                backtrace_mat[i][j] = "d"
            if score_mat[i][j] == score2:
                backtrace_mat[i][j] = "u"
            if score_mat[i][j] == score3:
                backtrace_mat[i][j] = "l"

    i = len(str1) - 1
    j = max(range(len(str2)), key=lambda x: score_mat[i][x])
    max_score = score_mat[i][j]

    aligned_1 = aligned_2 = ""
    while backtrace_mat[i][j] is not None:
        direction = backtrace_mat[i][j]
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
    Given: Two DNA strings s and t in FASTA format, each having length at most 10 kbp.
    Return: The score of an optimal overlap alignment of s and t, followed by an alignment of a suffix s′ of s and a 
    prefix t′ of t achieving this optimal score. Use an alignment score in which matching symbols count +1, 
    substitutions count -2, and there is a linear gap penalty of 2. If multiple optimal alignments exist, then you may 
    return any one.
    '''
    input_lines = sys.stdin.read().splitlines()
    stringA = list(parse_fasta(input_lines).values())[0]
    stringB = list(parse_fasta(input_lines).values())[1]

    score, aligned_strA, aligned_strB = overlap_alignment(stringA, stringB)

    print(score)
    print(aligned_strA)
    print(aligned_strB)
