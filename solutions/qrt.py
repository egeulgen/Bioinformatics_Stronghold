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
        nol = [i for (n, i) in enumerate(names) if s[n] == '0']
        edi = [i for (n, i) in enumerate(names) if s[n] == '1']
        nolpairs = ((nol[i], nol[j]) for i in range(len(nol)) for j in range(i + 1, len(nol)))
        edipairs = ((edi[i], edi[j]) for i in range(len(edi)) for j in range(i + 1, len(edi)))
        for c in product(nolpairs, edipairs):
            result.add(frozenset(map(frozenset, c)))
    for ((a, b), (c, d)) in result:
        print('{%s, %s} {%s, %s}' % (a, b, c, d))