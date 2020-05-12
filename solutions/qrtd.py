import sys
from nwck import Newick
from ctbl import character_table
from itertools import combinations
from scipy.special import comb


def quartets(nwck, all_leaves):
    tree = Newick(nwck)
    tbl = character_table(tree)

    named_nodes = lambda n: 'Node_' not in n
    unnamed_edges = lambda e: 'Node_' in e[0] and 'Node_' in e[1]

    # Get the nontrial edges.
    nontrivial_edges = list(filter(unnamed_edges, tree.edge_names()))

    quarts = []
    for edge in nontrivial_edges:
        taxa_1 = list(filter(named_nodes,
                           set(tree.get_descendants(edge[0])) & set(tree.get_descendants(edge[1]))))
        taxa_0 = [node for node in all_leaves if node not in taxa_1]

        if len(taxa_1) > 1 and len(taxa_0) > 1:
            quarts += ([[tup1, tup0] for tup1 in combinations(taxa_1, 2) for tup0 in combinations(taxa_0, 2)])

    quarts = set([tuple(sorted(x)) for x in quarts])  # eliminate redundancy

    return quarts


if __name__ == "__main__":
    '''
    Given: A list containing n taxa (n≤2000) and two unrooted binary trees T1 and T2 on the given taxa. Both T1 and T2 
    are given in Newick format.
    Return: The quartet distance dq(T1,T2).
    '''
    ## this is to slow, will improve later
    input_lines = sys.stdin.read().splitlines()
    taxa = input_lines[0].split()
    n = len(taxa)
    nwck1 = input_lines[1]
    nwck2 = input_lines[2]

    quartets1 = quartets(nwck1, taxa)
    quartets2 = quartets(nwck2, taxa)

    shared = 0
    for q1 in quartets1:
        if q1 in quartets2:
            shared += 1

    dist = 2 * comb(n, 4) - 2 * shared

    print(int(dist))