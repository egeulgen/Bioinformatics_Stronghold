import sys
from rosalind_utility import parse_fasta


def consensus(strings):
    ''' Create Consensus String and Profile Matrix
    :param strings: list of DNA strings
    :return: consensus string and profile matrix
    '''
    profile_matrix = {"A": {}, "C": {}, "G": {}, "T": {}}
    for string in strings:
        for i in range(len(string)):
            if i in profile_matrix[string[i]]:
                profile_matrix[string[i]][i] += 1
            else:
                profile_matrix[string[i]][i] = 1
    consensus_string = ""
    for i in range(len(strings[0])):
        max_val = -1
        consensus_sym = ""
        for sym in profile_matrix.keys():
            if i in profile_matrix[sym]:
                if profile_matrix[sym][i] > max_val:
                    max_val = profile_matrix[sym][i]
                    consensus_sym = sym
        consensus_string += consensus_sym

    return consensus_string, profile_matrix


if __name__ == "__main__":
    '''
    Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
    Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, 
    then you may return any one of them.)
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_strings = parse_fasta(input_lines)
    DNA_strings = list(DNA_strings.values())
    cons_string, profile_mat = consensus(DNA_strings)

    print(cons_string)
    for sym, counts in profile_mat.items():
        line = sym + ': '
        for i in range(len(DNA_strings[0])):
            if i in counts:
                line += str(counts[i]) + ' '
            else:
                line += '0 '
        print(line)
