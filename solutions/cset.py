import sys
from collections import Counter


def has_conflict(c1, c2):
    """Return True if two rows of character table conflict."""
    hasConflict = True
    s1 = set(i for i, c in enumerate(c1) if c == '1')
    s1c = set(i for i, c in enumerate(c1) if c == '0')
    s2 = set(i for i, c in enumerate(c2) if c == '1')
    s2c = set(i for i, c in enumerate(c2) if c == '0')

    for a in [s1, s1c]:
        for b in [s2, s2c]:
            if len(a.intersection(b)) == 0:
                hasConflict = False
    return hasConflict


if __name__ == "__main__":
    '''
    Given: An inconsistent character table C on at most 100 taxa.
    Return: A submatrix of C′ representing a consistent character table on the same taxa and formed by deleting a single
    row of C. (If multiple solutions exist, you may return any one.)
    '''
    character_table = sys.stdin.read().splitlines()
    conflictCount = Counter()
    for i in range(len(character_table)):
        for j in range(i + 1, len(character_table)):
            if has_conflict(character_table[i], character_table[j]):
                conflictCount[i] += 1
                conflictCount[j] += 1

    skipIndex = max(conflictCount, key=lambda x: conflictCount[x])

    for i in range(len(character_table)):
        if i != skipIndex:
            print(character_table[i])
