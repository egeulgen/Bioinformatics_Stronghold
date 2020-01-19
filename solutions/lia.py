import sys
from operator import mul
from math import factorial as fact
from functools import reduce

def choose(n, x):
    '''
    Returns the integer value for n choose x.
    '''
    if x in (0, n):
        return 1
    if x > n / 2:
        return reduce(mul, range(x + 1, n + 1)) / fact(n - x)
    else:
        return reduce(mul, range(n - x + 1, n + 1)) / fact(x)


def dbinom(n, p, x):
    '''
    Calculates the probability of getting x events with probability p in n trials.

    n = size of population
    p = prob of event
    x = number of events
    '''
    return choose(n, x) * p ** x * (1 - p) ** (n - x)


def pbinom(n, p, x):
    '''
    Calculates the cumulative binomial probability for X < x.

    n = size of population
    p = prob of event
    x = number of events
    '''
    return sum(dbinom(n, p, value) for value in range(x))


if __name__ == "__main__":
    '''
    Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation 
    has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each 
    organism always mates with an organism having genotype Aa Bb.
    Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree 
    (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
    '''
    k, N = [int(x) for x in sys.stdin.read().splitlines()[0].split(' ')]

    print(1 - pbinom(2 ** k, 0.25, N))