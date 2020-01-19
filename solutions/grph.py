import sys
from rosalind_utility import parse_fasta


def olap_graph(strings, k):
    ''' Create Overlap Graph
    :param strings: DNA strings
    :param k: suffix length
    :return: adjacency list of Ok
    '''
    adj_list = []
    for name, string in strings.items():
        for name2, string2 in strings.items():
            if name != name2:
                if string[-k:] == string2[:k]:
                    adj_list.append((name, name2))
    return adj_list


if __name__ == "__main__":
    '''
    Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
    Return: The adjacency list corresponding to O3. You may return edges in any order.
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_strings = parse_fasta(input_lines)
    olap_adj_list = olap_graph(DNA_strings, 3)

    for olap in olap_adj_list:
        print(' '.join(olap))
