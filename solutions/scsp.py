import sys
from lcsq import longest_common_subsequence


def shortest_common_supersequence(v, w):
    lcsq_string = longest_common_subsequence(v, w)

    scs_string = ""
    i = 0
    j = 0
    for char in lcsq_string:
        if i < len(v):
            while v[i] != char:
                scs_string += v[i]
                i += 1
            i += 1
        if j < len(w):
            while w[j] != char:
                scs_string += w[j]
                j += 1
            j += 1
        scs_string += char

    if i < len(v):
        scs_string += v[i:]
    if j < len(w):
        scs_string += w[j:]

    return scs_string


if __name__ == "__main__":
    '''
    Given: Two DNA strings s and t.
    Return: A shortest common supersequence of s and t. If multiple solutions exist, you may output any one.
    '''
    v, w = sys.stdin.read().splitlines()
    print(shortest_common_supersequence(v, w))
