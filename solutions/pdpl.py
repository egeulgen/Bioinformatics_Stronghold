import sys
from collections import Counter


def partial_digest(distances):
    '''Returns a set whose positive pairwise differences generate 'distances'.'''
    # Initialize variables.
    X = {0}
    width = max(distances)

    # Create lambda functions for multiset operations.
    new_dist = lambda y, S: Counter(abs(y-s) for s in S)
    containment = lambda a, b: all(a[x] <= b[x] for x in a)

    # Create the multiset which generates 'distances'.
    while len(distances) > 0:
        y = max(distances)
        if containment(new_dist(y, X), distances):
            X |= {y}
            distances -= new_dist(y, X)
        else:
            X |= {width - y}
            distances -= new_dist(width - y, X)

    return X


if __name__ == "__main__":
    '''
    Given: A multiset L containing (n2) positive integers for some positive integer n.
    Return: A set X containing n nonnegative integers such that ΔX=L.
    '''
    input_lines = sys.stdin.read().splitlines()
    L = Counter(int(x) for x in input_lines[0].split())

    X = sorted(list(partial_digest(L)))
    print(' '.join(map(str, X)))