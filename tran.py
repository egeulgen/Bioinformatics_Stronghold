import sys
from rosalind_utility import parse_fasta

TI_DICT = {"A": "G", "G": "A", "C": "T", "T": "C"}

def ti_tv_ratio(string1, string2):
    ''' Calculate Ti/Tv ratio
    :param string1: string 1
    :param string2: query string
    :return: Ti/Tv ratio (float)
    '''
    num_ti = 0
    num_tv = 0

    for sym1, sym2 in zip(string1, string2):
        if sym1 != sym2:
            if sym2 == TI_DICT[sym1]:
                num_ti += 1
            else:
                num_tv += 1

    return num_ti / num_tv


if __name__ == "__main__":
    '''
    Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
    Return: The transition/transversion ratio R(s1,s2).
    '''
    input_lines = sys.stdin.read().splitlines()
    s, t = list(parse_fasta(input_lines).values())
    print(ti_tv_ratio(s, t))
