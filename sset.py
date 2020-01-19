import sys

if __name__ == "__main__":
    '''
    Given: A positive integer n (n≤1000).
    Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
    '''
    n = int(sys.stdin.readline().rstrip())

    print(2 ** n % 1e6)

