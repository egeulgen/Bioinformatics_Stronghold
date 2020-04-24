import sys
from nwck import Newick


def child_prob(a, b):
    AA = a[0] * b[0] + 0.5 * (a[0] * b[1] + a[1] * b[0] + 0.5 * a[1] * b[1])
    Aa = a[0] * b[2] + a[2] * b[0] + 0.5 * (a[0] * b[1] + a[1] * b[0] + a[1] * b[1] + a[2] * b[1] + a[1] * b[2])
    aa = a[2] * b[2] + 0.5 * (a[1] * b[2] + a[2] * b[1] + 0.5 * a[1] * b[1])
    return [AA, Aa, aa]


if __name__ == "__main__":
    '''
    Given: A rooted binary tree T in Newick format encoding an individual's pedigree for a Mendelian factor whose 
    alleles are A (dominant) and a (recessive).
    Return: Three numbers between 0 and 1, corresponding to the respective probabilities that the individual at the root 
    of T will exhibit the "AA", "Aa" and "aa" genotypes.
    '''
    input_lines = sys.stdin.read().splitlines()
    tree = input_lines[0]

    nwck = Newick(tree)
    genotype_prob = lambda genotype: [int(genotype.count('a') == i) for i in range(3)]

    # Convert the nodes with genotype names to probabilities.
    for node in [node for node in nwck.nodes if 'Node' not in node.name]:
        node.name = genotype_prob(node.name)

    # Compute the offspring genotype probabilities.
    while nwck.nodes[0].name == 'Node_0':
        for node in [node for node in nwck.nodes if 'Node' in node.name]:
            if 'Node' not in ''.join([str(nwck.nodes[i].name) for i in node.children]):
                node.name = child_prob(nwck.nodes[node.children[0]].name, nwck.nodes[node.children[1]].name)

    print(" ".join(map(str, nwck.nodes[0].name)))
