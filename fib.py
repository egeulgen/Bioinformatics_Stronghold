import sys


def modified_fibonacci(n, k):
    ''' Modified Fibonacci Sequence
    :param n: number of generations (integer)
    :param k: number of pairs a reproduction age pair of rabbits produces (integer)
    :return: the nth element in the sequence (integer)
    '''
    result = {1: 1, 2: 1}
    if n in result:
        return result[n]
    result[n] = modified_fibonacci(n - 1, k) + k * modified_fibonacci(n - 2, k)
    return result[n]


if __name__ == "__main__":
    '''
    Given: Positive integers n≤40 and k≤5.
    Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each 
    generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
    '''
    n, k = [int(x) for x in sys.stdin.read().splitlines()[0].split(" ")]
    print(modified_fibonacci(n, k))