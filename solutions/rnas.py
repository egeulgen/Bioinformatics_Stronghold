import sys

memo = {}


def helper(seq):
    if len(seq) == 0 or len(seq) == 1:
        return 1
    if seq in memo:
        return memo[seq]

    memo[seq] = helper(seq[1:])
    for i in range(4, len(seq)):
        if ((seq[0] == 'A' and seq[i] == 'U') or
                (seq[0] == 'U' and seq[i] == 'A') or
                (seq[0] == 'C' and seq[i] == 'G') or
                (seq[0] == 'G' and seq[i] == 'C') or
                (seq[0] == 'U' and seq[i] == 'G') or
                (seq[0] == 'G' and seq[i] == 'U')):
            memo[seq] += helper(seq[1:i]) * helper(seq[i+1:])
    return memo[seq]


if __name__ == "__main__":
    '''
    Given: An RNA string s (of length at most 200 bp).
    Return: The total number of distinct valid matchings of basepair edges in the bonding graph of s. Assume that wobble
    base pairing is allowed.
    '''
    input_lines = sys.stdin.read().splitlines()

    rna_string = input_lines[0]

    print(helper(rna_string))
