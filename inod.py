import sys

if __name__ == "__main__":
    '''
    Given: A positive integer n (3≤n≤10000).
    Return: The number of internal nodes of any unrooted binary tree having n leaves.
    '''
    n = int(sys.stdin.readline().rstrip())

    # An unrooted tree with n leaves and m internal nodes should have n + 3m total degrees.
    # (n + 3m) / 2 = n + m - 1
    # m = n - 2
    print(n - 2)
