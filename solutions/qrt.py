import sys
from itertools import product

if __name__ == "__main__":
    '''
    Given: A partial character table C.
    Return: The collection of all quartets that can be inferred from the splits corresponding to the underlying 
    characters of C.
    '''
    input_lines = sys.stdin.read().splitlines()
    names = input_lines[0].split()

    result = set()
    for s in input_lines[1: ]:
        zeros = [n for (i, n) in enumerate(names) if s[i] == '0']
        ones = [n for (i, n) in enumerate(names) if s[i] == '1']
        zero_pairs = ((zeros[i], zeros[j]) for i in range(len(zeros)) for j in range(i + 1, len(zeros)))
        one_pairs = ((ones[i], ones[j]) for i in range(len(ones)) for j in range(i + 1, len(ones)))
        for c in product(zero_pairs, one_pairs):
            result.add(frozenset(map(frozenset, c)))
    for ((a, b), (c, d)) in result:
        print('{%s, %s} {%s, %s}' % (a, b, c, d))