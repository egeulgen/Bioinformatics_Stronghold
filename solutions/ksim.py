import sys


def inside_band(i, j, k):
    return -k <= i - j <= k


def edit_distance_kband(str1, str2, bandwidth):
    str1 = "-" + str1
    str2 = "-" + str2

    diff = len(str1) - len(str2)

    score_mat = [[1e6 for j in range(len(str2))] for i in range(len(str1))]

    for i in range(bandwidth + 1 + diff):
        score_mat[i][0] = i
    for j in range(1, bandwidth + 1):
        score_mat[0][j] = j

    for i in range(1, len(str1)):
        for h in range(-bandwidth - diff, bandwidth + 1):
            j = i + h
            if 1 <= j < len(str2):
                score_mat[i][j] = score_mat[i - 1][j - 1] + (1 if str1[i] != str2[j] else 0)
                if inside_band(i - 1, j, bandwidth + diff):
                    score_mat[i][j] = min(score_mat[i][j], score_mat[i - 1][j] + 1)
                if inside_band(i, j - 1, bandwidth):
                    score_mat[i][j] = min(score_mat[i][j], score_mat[i][j - 1] + 1)
    return score_mat


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

    len_A = len(stringA)
    len_B = len(stringB)

    edit_dist_dict = {}

    for i in range(len_B - len_A + k + 1):
        last = min(len_B, i + len_A + k)
        length = last - i + 1

        substr = stringB[i:last]

        if substr in edit_dist_dict:
            score_mat = edit_dist_dict[substr]
        else:
            if len(substr) < len_A:
                score_mat = edit_distance_kband(stringA, substr, k)
            else:
                score_mat = edit_distance_kband(substr, stringA, k)
            edit_dist_dict[substr] = score_mat

        if len(score_mat) > len(score_mat[0]):
            for idx in range(len(score_mat)):
                if score_mat[idx][len_A] <= k:
                    print(i + 1, idx)
        else:
            for idx in range(len(score_mat[0])):
                if score_mat[len_A][idx] <= k:
                    print(i + 1, idx)
