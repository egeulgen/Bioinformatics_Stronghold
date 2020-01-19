import sys
from rosalind_utility import parse_fasta
from rosalind_utility import rev_comp


def reverse_palindromes(string, min_len = 4, max_len = 12):
    ''' Locate reverse palindromes within string
    :param string: string to locate palindromes in (string)
    :return: list of all palindromic positions and lengths (list of 2-tuples)
    '''
    pos_list = []
    for k in range(min_len, max_len + 1):
        for i in range(len(string) - k + 1):
            subseq = string[i:i + k]
            if subseq == rev_comp(subseq):
                pos_list.append((i + 1, k))
    return pos_list


if __name__ == "__main__":
    '''
    Given: A DNA string of length at most 1 kbp in FASTA format.
    Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may 
    return these pairs in any order.
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_string = list(parse_fasta(input_lines).values())[0]
    positions = reverse_palindromes(DNA_string)
    for pos in positions:
        print(' '.join([str(x) for x in pos]))
