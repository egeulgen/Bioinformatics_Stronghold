import sys
from rosalind_utility import parse_fasta


def lcsm(strings_list):
    ''' Find the longest common substring
    :param strings_list: list of DNA strings
    :return: the longest common substring
    '''
    min_len = 1e6
    min_len_string = ""
    for string in strings_list:
        if len(string) < min_len:
            min_len = len(string)
            min_len_string = string
    other_strings = [x for x in strings_list if x != min_len_string]
    for k in range(len(min_len_string) - 1, 1, -1):
        for i in range(len(min_len_string) - k + 1):
            substring = min_len_string[i:i + k]
            for other in other_strings:
                if substring not in other:
                    break
            else:
                return substring


if __name__ == "__main__":
    '''
    Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
    Return: A longest common substring of the collection. (If multiple solutions exist, you may return any 
    single solution.)
    '''
    input_lines = sys.stdin.read().splitlines()
    strings_dict = parse_fasta(input_lines)
    DNA_strings = list(strings_dict.values())
    print(lcsm(DNA_strings))
