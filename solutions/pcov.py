import sys


def determine_superstring(dna_strings):
    DBG_edge_elements = set()
    for kmer in dna_strings:
        DBG_edge_elements.add(kmer)

    k = len(dna_strings[0])
    DBG_edges = [[elem[0:k - 1], elem[1:k]] for elem in DBG_edge_elements]

    # Construct the cyclic superstring from the edges
    temp = DBG_edges.pop(0)
    super_string = temp[0][-1]
    while DBG_edges:
        super_string += temp[1][-1]
        [index] = [i for i, pair in enumerate(DBG_edges) if pair[0] == temp[1]]
        temp = DBG_edges.pop(index)

    return super_string


if __name__ == "__main__":
    '''
    Given: A collection of (error-free) DNA k-mers (k≤50) taken from the same strand of a circular chromosome. In this 
    dataset, all k-mers from this strand of the chromosome are present, and their de Bruijn graph consists of exactly 
    one simple cycle.
    Return: A cyclic superstring of minimal length containing the reads (thus corresponding to a candidate cyclic 
    chromosome).
    '''
    input_lines = sys.stdin.read().splitlines()
    result = determine_superstring(input_lines)

    print(result)