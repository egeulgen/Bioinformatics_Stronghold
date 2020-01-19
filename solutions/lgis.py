import sys


def calculate_lis(sequence):
    ''' Calculate a longest increasing subsequence
    :param sequence: sequence to search the lis in
    :return: a lis
    '''
    L = [[sequence[0]]]
    for i in range(1, len(sequence)):
        L.append([])
        for j in range(i):
            if (sequence[j] < sequence[i]) and (len(L[i]) < len(L[j]) + 1):
                L[i] = L[j][:]
        L[i].append(sequence[i])
    lis = []
    max_len = 0
    for l in L:
        if len(l) > max_len:
            max_len = len(l)
            lis = l
    return lis


if __name__ == "__main__":
    '''
    Given: A positive integer n≤10000 followed by a permutation π of length n.
    Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
    '''
    n = int(sys.stdin.readline())
    permutation = list(map(int, sys.stdin.readline().rstrip().split()))

    LIS = calculate_lis(permutation)
    LDS = calculate_lis(permutation[::-1])[::-1]

    print(" ".join(map(str, LIS)))
    print(" ".join(map(str, LDS)))
