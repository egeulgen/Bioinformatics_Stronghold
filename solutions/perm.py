import sys
from itertools import permutations

if __name__ == "__main__":
    '''
    Given: A positive integer n≤7.
    Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
    '''
    n = int(sys.stdin.read().splitlines()[0])
    permutations = list(permutations(range(1, n + 1)))

    print(len(permutations))
    for perm in permutations:
        print(' '.join([str(x) for x in perm]))