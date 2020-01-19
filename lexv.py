import sys
from itertools import product, repeat


def lex_ordered(alphabet, n):
    lexv = []
    for item in product(alphabet, repeat=n):
        # Include all items without *'s.
        if '*' not in item:
            lexv.append(''.join(item))
        else:
            # Items with only trailing *'s should also be included with the *'s removed.
            for i in range(1, n):
                if ''.join(item[i:n]) == '*' * (n - i) and '*' not in item[:i]:
                    lexv.append(''.join(item).replace('*', ''))
    return lexv


if __name__ == "__main__":
    '''
    Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜 and a positive integer n (n≤4).
    Return: All strings of length at most n formed from 𝒜, ordered lexicographically. (Note: As in “Enumerating k-mers 
    Lexicographically”, alphabet order is based on the order in which the symbols are given.)
    '''
    input_lines = sys.stdin.read().splitlines()
    alphabet_string = ["*"] + input_lines[0].split(" ")
    n = int(input_lines[1])
    result = lex_ordered(alphabet_string, n)
    for res in result:
        print(res)
