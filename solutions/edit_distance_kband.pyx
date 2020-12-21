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