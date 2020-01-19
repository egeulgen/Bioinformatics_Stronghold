import sys
from math import pow


def rstr_prob(num_strs, gc_content, seq_string):
    prob = 1
    for nuc in seq_string:
        if nuc in "GC":
            prob *= gc_content * 0.5
        else:
            prob *= (1 - gc_content) * 0.5
    return 1 - pow(1 - prob, num_strs)



if __name__ == "__main__":
    '''
    Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.
    Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x 
    (see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random 
    string to be created more than once.
    '''
    input_lines = sys.stdin.read().splitlines()

    N, x = input_lines[0].split(" ")
    N = int(N)
    x = float(x)
    DNA_string = input_lines[1]

    print(rstr_prob(N, x, DNA_string))