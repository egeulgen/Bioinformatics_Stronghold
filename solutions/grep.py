import sys


def coverings(s, edges, k):
    '''Generate all possible complete cycle coverings from the given edges.'''
    # Determine the possible next elements to add to the covering.
    add_on = [index for index, item in enumerate(edges) if item[0] == s[-k+1:]]

    # If there's nothing left to add, return the string if we have a perfect covering (no edges left).
    # If we don't have perfect covering, return an empty list, which gets removed when flattened.
    if len(add_on) == 0:
        return [s if edges == [] else []]
    # Otherwise, proceed with all possible coverings.
    else:
        return [coverings(s+edges[i][1][-1], edges[:i]+edges[i+1:], k) for i in add_on]


def flatten(lst):
    '''Unpacks nested lists as a generator.'''
    for element in lst:
        if isinstance(element, list):
            for subelement in flatten(element):
                yield subelement
        else:
            yield element


if __name__ == "__main__":
    '''
    Given: A list Sk+1 of error-free DNA (k+1)-mers (k≤5) taken from the same strand of a circular chromosome 
    (of length ≤50).
    Return: All circular strings assembled by complete cycles in the de Bruijn graph Bk of Sk+1. The strings may be 
    given in any order, but each one should begin with the first (k+1)-mer provided in the input.
    '''
    k_mers = sys.stdin.read().splitlines()

    k = len(k_mers[0])
    edge = lambda elmt: [elmt[0:k - 1], elmt[1:k]]
    DBG_edges = [edge(elmt) for elmt in k_mers[1:]]

    circular_strings = [circular[:len(k_mers)] for circular in set(flatten(coverings(k_mers[0], DBG_edges, k)))]
    for string in circular_strings:
        print(string)