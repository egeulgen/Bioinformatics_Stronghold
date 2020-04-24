import sys
from cunr import count_unrooted_binary_trees


def count_rooted_binary_trees(n):
    return count_unrooted_binary_trees(n) * (2 * n - 3) % 10 ** 6


if __name__ == "__main__":
    '''
    Let B(n) represent the total number of distinct rooted binary trees on n labeled taxa.
    Given: A positive integer n (n≤1000).
    Return: The value of B(n) modulo 1,000,000.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])

    print(count_rooted_binary_trees(n))
