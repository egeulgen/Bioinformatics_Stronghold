import sys


def count_symbols(string):
    ''' Count number of occurrences of each symbol in string
    :param string: string to calculate frequencies from (string)
    :return: list of counts of symbols in the string (given in alphabetical order, list)
    '''
    # extract symbols from the string
    symbols = sorted(set(string))

    # calculate frequency of each symbol
    counts_list = []
    for sym in symbols:
        counts_list.append(string.count(sym))
    return counts_list


if __name__ == "__main__":
    '''
    Given: A DNA string s of length at most 1000 nt.
    Return: Four integers (separated by spaces) counting the respective number of times that the symbols 
    'A', 'C', 'G', and 'T' occur in s.
    '''
    DNA_string = sys.stdin.read().splitlines()[0]
    print(' '.join(str(c) for c in count_symbols(DNA_string)))
