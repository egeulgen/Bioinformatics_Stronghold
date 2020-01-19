import sys


def reversal_dist(s, t):
    """ Calculate Reversal Distance
    Given two permutations, return the reversal distance
    """
    # TO DO


if __name__ == "__main__":
    '''
    Given: A collection of at most 5 pairs of permutations, all of which have length 10.
    Return: The reversal distance between each permutation pair.
    '''
    input_lines = sys.stdin.read().splitlines()
    for idx in range(0, len(input_lines), 3):
        P1 = map(int, input_lines[idx].split())
        P2 = map(int, input_lines[idx + 1].split())

        print(reversal_dist(P1, P2))

