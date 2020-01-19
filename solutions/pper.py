import sys


if __name__ == "__main__":
    '''
    Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.
    Return: The total number of partial permutations P(n,k), modulo 1,000,000.
    '''
    n, k = map(int, sys.stdin.readline().rstrip().split(" "))
    num_pper = 1
    for i in range(k):
        num_pper *= n - i
        num_pper %= 1e6
    print(int(num_pper))
