import sys


def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * double_factorial(n - 2)


if __name__ == "__main__":
    '''
    Let b(n) denote the total number of distinct unrooted binary trees having n labeled leaves.
    Given: A positive integer n (n≤1000).
    Return: The value of b(n) modulo 1,000,000.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])

    # The total number is just the double factorial: (2n - 5)!!
    print(double_factorial(2 * n - 5) % int(1e6))