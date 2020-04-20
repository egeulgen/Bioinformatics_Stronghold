import sys
from numpy import zeros
from nwck import Newick


def character_table(tree):
    named_nodes = lambda n: 'Node_' not in n
    unnamed_edges = lambda e: 'Node_' in e[0] and 'Node_' in e[1]

    # A dictionary relating node name to alphabetical order.
    node_order = {name: index for index, name in
                  enumerate(sorted(filter(named_nodes, [node.name for node in tree.nodes])))}

    # Get the nontrial edges.
    nontrivial_edges = list(filter(unnamed_edges, tree.edge_names()))

    # Find and mark the on/off taxa.
    M = zeros((len(nontrivial_edges), len(node_order)), dtype=int)
    for i, edge in enumerate(nontrivial_edges):
        taxa = list(filter(named_nodes,
                           set(tree.get_descendants(edge[0])) & set(tree.get_descendants(edge[1]))))
        for t in taxa:
            M[i][node_order[t]] = 1
    return M


if __name__ == "__main__":
    '''
    Given: An unrooted binary tree T in Newick format for at most 200 species taxa.
    Return: A character table having the same splits as the edge splits of T. The columns of the character table should 
    encode the taxa ordered lexicographically; the rows of the character table may be given in any order. Also, for any 
    given character, the particular subset of taxa to which 1s are assigned is arbitrary.
    '''
    input_lines = sys.stdin.read().splitlines()
    tree_nwck = input_lines[0]

    tree = Newick(tree_nwck)

    res = character_table(tree)
    for row in res:
        print("".join(map(str, row)))
