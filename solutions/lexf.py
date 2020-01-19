import sys


def alpha_combs(alphabet, n, acc='', res=[]):
    if n == 0:
        res.append(acc)
    else:
        for c in alphabet:
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res


if __name__ == "__main__":
    '''
    Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
    Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard 
    order of symbols in the English alphabet).
    '''
    symbols = sys.stdin.readline().rstrip().split()
    n = int(sys.stdin.readline())

    sorted_permutations = alpha_combs(symbols, n, )
    for perm in sorted_permutations:
        print(perm)
