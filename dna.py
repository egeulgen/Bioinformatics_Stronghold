import sys


def count_symbols(sequence):
    ''' Count number of occurrences of each symbol in sequence
    :param sequence: sequence to calculate frequencies from (string)
    :return: list of counts of symbols in the sequence (given in alphabetical order)
    '''
    # extract symbols from the string
    symbols = sorted(set(sequence))

    # calculate frequency of each symbol
    counts_list = []
    for sym in symbols:
        counts_list.append(sequence.count(sym))
    return counts_list


if __name__ == "__main__":
    '''
    Given: A DNA string s of length at most 1000 nt.
    Return: Four integers (separated by spaces) counting the respective number of times that the symbols 
    'A', 'C', 'G', and 'T' occur in s.
    '''
    DNA_seq = sys.stdin.read().splitlines()[0]
    print(' '.join(str(c) for c in count_symbols(DNA_seq)))