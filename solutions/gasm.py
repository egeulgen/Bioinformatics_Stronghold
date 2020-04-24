import sys
from rosalind_utility import rev_comp

def deBruijn(dna_strings):
    long_mers = set()
    for string in dna_strings:
        long_mers.add(string)
        long_mers.add(rev_comp(string))
    result = []
    for mer in long_mers:
        result.append((mer[:len(mer) - 1], mer[1:]))
    return result


def determine_superstrings(dna_strings):
    # We don't know which k value gives exactly two directed cycles, so iterate until we find the right value.
    for kval in range(1, len(dna_strings[0])):
        # Begin by constructing the De Bruijn Graph
        DBG_edge_elmts = set()
        for kmer in dna_strings:
            for i in range(kval):
                DBG_edge_elmts.add(kmer[i:len(kmer) + i - kval + 1])
                DBG_edge_elmts.add(rev_comp(kmer[i:len(kmer) - kval + i + 1]))

        # Create the edges of the Graph.
        k = len(list(DBG_edge_elmts)[0])
        edge = lambda elmt: [elmt[0:k - 1], elmt[1:k]]
        DBG_edges = [edge(elmt) for elmt in DBG_edge_elmts]

        # Construct the cyclic superstrings from the edges.
        cyclics_list = []
        for repeat in range(2):
            temp_kmer = DBG_edges.pop(0)
            cyclic = temp_kmer[0][-1]
            while temp_kmer[1] in [item[0] for item in DBG_edges]:
                cyclic += temp_kmer[1][-1]
                [index] = [i for i, pair in enumerate(DBG_edges) if pair[0] == temp_kmer[1]]
                temp_kmer = DBG_edges.pop(index)
            cyclics_list.append(cyclic)

        # Break if we've found exactly two directed cycles.
        if len(DBG_edges) == 0:
            break

    return cyclics_list


if __name__ == "__main__":
    '''
    Given: A collection S of (error-free) reads of equal length (not exceeding 50 bp). In this dataset, for some 
    positive integer k, the de Bruijn graph Bk on Sk+1∪Srck+1 consists of exactly two directed cycles.
    Return: A cyclic superstring of minimal length containing every read or its reverse complement.
    '''
    input_lines = sys.stdin.read().splitlines()
    result1, result2 = determine_superstrings(input_lines)

    print(result1)