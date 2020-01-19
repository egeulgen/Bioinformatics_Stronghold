import sys
from rosalind_utility import parse_fasta


def failure_array(string):
    """ Calculate the Knuth-Morris-Pratt failure array
    :param string: the input string
    :return: failure array (list)
    """
    n = len(string)
    arr = [0] * n
    for i in range(1, n):
        j = arr[i - 1]
        while j > 0 and string[i] != string[j]:
            j = arr[j - 1]
        if string[i] == string[j]:
            j += 1
        arr[i] = j
    return arr


if __name__ == "__main__":
    '''
    Given: A DNA string s (of length at most 100 kbp) in FASTA format.
    Return: The failure array of s.
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_string = list(parse_fasta(input_lines).values())[0]
    result = failure_array(DNA_string)
    print(" ".join(map(str, result)))
