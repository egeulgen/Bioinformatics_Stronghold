import sys
from math import log10
from math import factorial as f


def binomial_pdf(n, k, p = 0.5):
    return f(n) // f(k) // f(n - k) * p ** k * (1 - p) ** (n - k)


if __name__ == "__main__":
    '''
    Given: A positive integer n≤50.
    Return: An array A of length 2n in which A[k] represents the common logarithm of the probability that two diploid 
    siblings share at least k of their 2n chromosomes (we do not consider recombination for now).
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])

    result = []
    for k in range(1, 2 * n + 1):
        cum_pr = sum(binomial_pdf(2 * n, i) for i in range(k, 2 * n + 1))
        result.append(log10(cum_pr))

    print(" ".join(map(str, result)))