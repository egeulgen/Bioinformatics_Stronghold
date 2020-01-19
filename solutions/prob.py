import sys
from math import log10

def calculate_prob(string, gc):
    ''' Calculate the probability that a random string matches string exactly
    :param string: string to compare
    :param gc: GC content to construct random strings
    :return: log(probability) that a random string constructed with the GC content matches string exactly
    '''
    sym_probs = {"G": log10(gc / 2), "C": log10(gc / 2), "A": log10((1 - gc) / 2), "T": log10((1 - gc) / 2)}
    log_probability = 0
    for sym in string:
        log_probability += sym_probs[sym]
    return log_probability

if __name__ == "__main__":
    '''
    Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
    Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that 
    a random string constructed with the GC-content found in A[k] will match s exactly.
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_string = input_lines[0]
    GC_list = map(float, input_lines[1].split(" "))

    prob_list = []
    for GC_content in GC_list:
        prob_list.append(calculate_prob(DNA_string, GC_content))

    print(' '.join(map(str, prob_list)))
