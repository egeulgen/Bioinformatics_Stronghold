import sys


if __name__ == "__main__":
    '''
    Given: A positive integer n (4≤n≤5000), followed by an unrooted binary tree T in Newick format on n taxa.
    Return: The value of q(T) modulo 1,000,000
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])

    result = 0
    for k in range(n - 2):
        result += (k + 1) * (n - k - 3) * (n - k - 2) / 2
    result = int(result) % 1000000

    print(result)