import sys
from rosalind_utility import parse_fasta
from rosalind_utility import rev_comp
from rosalind_utility import hamming_dist


def error_correction(strings):
    """ Perform Error Correction
    """
    correct_strings = []
    incorrect_strings = []
    for str in strings:
        if (strings.count(str) + strings.count(rev_comp(str))) >= 2:
            correct_strings.append(str)
        else:
            incorrect_strings.append(str)

    correct_strings = list(set(correct_strings))

    corr_list = []
    for str in incorrect_strings:
        for str2 in correct_strings:
            if hamming_dist(str, str2) == 1:
                corr_list.append((str, str2))
                break
            elif hamming_dist(str, rev_comp(str2)) == 1:
                corr_list.append((str, rev_comp(str2)))
                break

    return corr_list


if __name__ == "__main__":
    '''
    Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were 
    generated with a single-nucleotide error. For each read s in the dataset, one of the following applies:
        s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
        s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly 
        one correct read in the dataset (or its reverse complement).
    Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol 
    substitution, and you may return the corrections in any order.)
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_strings = list(parse_fasta(input_lines).values())

    result = error_correction(DNA_strings)
    for corr in result:
        print(corr[0] + '->' + corr[1])