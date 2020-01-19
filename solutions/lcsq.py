import sys
from rosalind_utility import parse_fasta


def longest_common_subsequence(v, w):
    """ Find the longest subsequence
    """
    v = '-' + v
    w = '-' + w
    score_mat = [[0 for i in range(len(w))] for j in range(len(v))]
    Backtrack = [[0 for i in range(len(w))] for j in range(len(v))]
    for i in range(1, len(score_mat)):
        score_mat[i][0] = score_mat[i - 1][0]
        Backtrack[i][0] = 1
    for j in range(1, len(score_mat[0])):
        score_mat[0][j] = score_mat[0][j - 1]
        Backtrack[0][j] = 2
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            diag = score_mat[i - 1][j - 1] + (1 if v[i] == w[j] else 0)
            down = score_mat[i - 1][j]
            right = score_mat[i][j - 1]
            score_mat[i][j] = max([0, down, right, diag])
            if score_mat[i][j] == 0:
                Backtrack[i][j] = 0
            elif score_mat[i][j] == down:
                Backtrack[i][j] = 1
            elif score_mat[i][j] == right:
                Backtrack[i][j] = 2
            else:
                Backtrack[i][j] = 4

    max_score = -1e3
    idx = (-1, -1)
    for i, row in enumerate(score_mat):
        for j, val in enumerate(row):
            if val > max_score:
                max_score = val
                idx = (i, j)

    v = v[1:]
    i, j = idx
    lcsq_str = ''
    while Backtrack[i][j] != 0:
        if Backtrack[i][j] == 4:
            lcsq_str = v[i - 1] + lcsq_str
            i -= 1
            j -= 1
        elif Backtrack[i][j] == 2:
            j -= 1
        else:
            i -= 1
    return lcsq_str


if __name__ == "__main__":
    '''
    Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.
    Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    v, w = list(parse_fasta(input_lines).values())
    print(longest_common_subsequence(v, w))
