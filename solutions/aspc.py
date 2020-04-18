import sys
from math import factorial


if __name__ == "__main__":
    '''
    Given: Positive integers n and m with 0≤m≤n≤2000.
    Return: The sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000. In shorthand, ∑nk=m(nk).
    '''
    n, m = map(int, sys.stdin.read().splitlines()[0].split())

    total = 0
    for i in range(m, n + 1):
        total += factorial(n) // (factorial(i) * factorial(n - i))

    print(total % int(1e6))