import sys
from edit_distance_kband import edit_distance_kband

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

    for i in range(len_B - len_A + k + 1):
        print(i)
        last = min(len_B, i + len_A + k + 1)

        substr = stringB[i:last]
        len_substr = len(substr)

        if len(substr) < len_A:
            score_mat = edit_distance_kband(stringA, substr, k)
            for idx in range(len_substr + 1):
                if score_mat[-1, idx] <= k:
                    print(i + 1, idx)
        else:
            score_mat = edit_distance_kband(substr, stringA, k)
            for idx in range(len_substr + 1):
                if score_mat[idx, -1] <= k:
                    print(i + 1, idx)