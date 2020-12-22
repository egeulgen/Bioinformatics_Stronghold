import numpy as np
cimport numpy as cnp

cdef bint inside_band(int i, int j, int k):
    return -k <= i - j <= k

cpdef cnp.ndarray edit_distance_kband(str str1, str str2, int bandwidth):

    cdef int m = len(str1) + 1
    cdef int n = len(str2) + 1

    cdef int diff = len(str1) - len(str2)

    cdef cnp.ndarray[cnp.int_t, ndim = 2] score_mat
    score_mat = np.full((m, n), 1e6, dtype=int)

    for i in range(bandwidth + 1 + diff):
        score_mat[i, 0] = i
    for j in range(1, bandwidth + 1):
        score_mat[0, j] = j

    for i in range(1, m):
        for h in range(-bandwidth - diff, bandwidth + 1):
            j = i + h
            if 1 <= j < n:
                score_mat[i, j] = score_mat[i - 1, j - 1] + (1 if str1[i - 1] != str2[j - 1] else 0)
                if inside_band(i - 1, j, bandwidth + diff):
                    score_mat[i, j] = min(score_mat[i, j], score_mat[i - 1, j] + 1)
                if inside_band(i, j - 1, bandwidth):
                    score_mat[i, j] = min(score_mat[i, j], score_mat[i, j - 1] + 1)
    return score_mat