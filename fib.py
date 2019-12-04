import sys


def fibonacci(n, k):
    result = {1: 1, 2: 1}
    if n in result:
        return result[n]
    result[n] = fibonacci(n - 1, k) + k * fibonacci(n - 2, k)
    return result[n]


if __name__ == "__main__":
    '''
    Given: Positive integers n≤40 and k≤5.
    Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each 
    generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
    '''
    n, k = [int(x) for x in sys.stdin.read().splitlines()[0].split(" ")]
    print(fibonacci(n, k))