import sys
from rosalind_utility import parse_fasta


def semiglobal_alignment(str1, str2):
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
            elif score_mat[i][j] == score2:
                backtrack_mat[i][j] = "u"
            else:
                backtrack_mat[i][j] = "l"

    last_row_index = max(range(len(str2)), key=lambda x: score_mat[len(str1) - 1][x])
    last_column_index = max(range(len(str1)), key=lambda x: score_mat[x][len(str2) - 1])
    if score_mat[len(str1) - 1][last_row_index] >= score_mat[last_column_index][len(str2) - 1]:
        i = len(str1) - 1
        j = last_row_index
    else:
        i = last_column_index
        j = len(str2) - 1
    max_score = score_mat[i][j]

    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Initialize the aligned strings as the input strings.
    aligned_1, aligned_2 = str1[1:], str2[1:]

    for _ in range(len(str1) - 1 - i):
        aligned_2 += '-'
    for _ in range(len(str2) - 1 - j):
        aligned_1 += '-'

    while i * j != 0:
        if backtrack_mat[i][j] == "u":
            i -= 1
            aligned_2 = insert_indel(aligned_2, j)
        elif backtrack_mat[i][j] == "l":
            j -= 1
            aligned_1 = insert_indel(aligned_1, i)
        else:
            i -= 1
            j -= 1

    for _ in range(i):
        aligned_2 = insert_indel(aligned_2, 0)
    for _ in range(j):
        aligned_1 = insert_indel(aligned_1, 0)

    return max_score, aligned_1, aligned_2


if __name__ == "__main__":
    '''
    Given: Two protein strings s and t in FASTA format (each having length at most 1000 aa).
    Return: A maximum alignment score along with substrings r and u of s and t, respectively, which produce this maximum
    alignment score (multiple solutions may exist, in which case you may output any one). Use:
        The PAM250 scoring matrix.
        Linear gap penalty equal to 5.
    '''
    input_lines = sys.stdin.read().splitlines()
    stringA = list(parse_fasta(input_lines).values())[0]
    stringB = list(parse_fasta(input_lines).values())[1]

    score, aligned_strA, aligned_strB = semiglobal_alignment(stringA, stringB)

    print(score)
    print(aligned_strA)
    print(aligned_strB)
