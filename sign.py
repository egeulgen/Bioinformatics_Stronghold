import sys
from itertools import permutations

if __name__ == "__main__":
    '''
    Given: A positive integer n≤6.
    Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may 
    list the signed permutations in any order).
    '''
    n = int(sys.stdin.read().splitlines()[0])
    permuts = list(permutations(range(1, n + 1)))

    for i in range(n):
        new_perm = []
        for perm in permuts:
            plus = perm
            minus = list(perm)
            minus[i] = -minus[i]
            new_perm += [minus, plus]
        permuts = new_perm

    print(len(permuts))
    for perm in permuts:
        print(' '.join([str(x) for x in perm]))
