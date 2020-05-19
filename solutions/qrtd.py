import sys
import re
import math


def quartet_distance(taxa, t1, t2):
    ## thank to yx749
    def parse_newick(taxa, t):
        tree = {}
        parent = {}
        name = {}
        new_node = 0
        root = new_node
        tree[root] = []
        current = root
        for match in re.finditer("\(|\)|,|;|([^\(\),;]+)", t):
            if match.group() == '(':
                new_node += 1
                tree[current].append(new_node)
                parent[new_node] = current
                current = new_node
                tree[current] = []
            elif match.group() == ',':
                new_node += 1
                tree[parent[current]].append(new_node)
                parent[new_node] = parent[current]
                current = new_node
                tree[current] = []
            elif match.group() == ')':
                current = parent[current]
            elif match.group() == ';':
                break
            else:
                name[current] = match.group()
        return tree, parent, name
    tree1, parent1, leaves1 = parse_newick(taxa, t1)
    tree2, parent2, leaves2 = parse_newick(taxa, t2)

    #get the children of each directed edge, negative number for the reversed edge
    n = len(taxa)
    def children(tree, parent, edge):
        if edge > 0:
            return tree[edge]
        else:
            p = parent[-edge]
            if p == 0:
                return [e for e in tree[p] if e != -edge]
            else:
                return [-p] + [e for e in tree[p] if e != -edge]
    children1 = [None for _ in range(4*n-5)]
    for i in range(1, 2*n-2):
        children1[i] = children(tree1, parent1, i)
    for i in range(3-2*n, 0):
        children1[i] = children(tree1, parent1, i)
    children2 = [None for _ in range(4*n-5)]
    for j in range(1, 2*n-2):
        children2[j] = children(tree2, parent2, j)
    for j in range(3-2*n, 0):
        children2[j] = children(tree2, parent2, j)

    shared_leaves = [[None for _ in range(4*n-5)] for _ in range(4*n-5)]
    def compute_shared_leaves(i, j):
        if shared_leaves[i][j] == None:
            if children1[i] == [] and children2[j] == []:
                shared_leaves[i][j] = int(leaves1[i] == leaves2[j])
            elif children1[i] == [] and children2[j] != []:
                j1, j2 = children2[j]
                shared_leaves[i][j] = compute_shared_leaves(i, j1) + compute_shared_leaves(i, j2)
            elif children1[i] != [] and children2[j] == []:
                i1, i2 = children1[i]
                shared_leaves[i][j] = compute_shared_leaves(i1, j) + compute_shared_leaves(i2, j)
            else:
                i1, i2 = children1[i]
                j1, j2 = children2[j]
                shared_leaves[i][j] = compute_shared_leaves(i1, j1) + compute_shared_leaves(i1, j2) \
                                        + compute_shared_leaves(i2, j1)+ compute_shared_leaves(i2, j2)
        return shared_leaves[i][j]
    for i in list(range(1, 2*n-2)) + [edge for edge in range(3-2*n, 0) if leaves1.get(-edge) == None]:
        for j in list(range(1, 2*n-2)) + [edge for edge in range(3-2*n, 0) if leaves2.get(-edge) == None]:
            compute_shared_leaves(i, j)

    internal1 = [edge for edge in range(1, 2*n-2) if leaves1.get(edge) == None] + [edge for edge in range(3-2*n, 0) if leaves1.get(-edge) == None]
    internal2 = [edge for edge in range(1, 2*n-2) if leaves2.get(edge) == None] + [edge for edge in range(3-2*n, 0) if leaves2.get(-edge) == None]
    quartets = [[0 for _ in range(4*n-5)] for _ in range(4*n-5)]
    for c1 in internal1:
        for c2 in internal2:
            a1, b1 = children1[-c1]
            a2, b2 = children2[-c2]
            quartets[c1][c2] = (shared_leaves[a1][a2]*shared_leaves[b1][b2]+shared_leaves[a1][b2]*shared_leaves[b1][a2]) \
                               * ((shared_leaves[c1][c2])*(shared_leaves[c1][c2]-1)/2)

    return 2*math.factorial(n)/math.factorial(n-4)/math.factorial(4) - sum(sum(row) for row in quartets)


if __name__ == "__main__":
    '''
    Given: A list containing n taxa (n≤2000) and two unrooted binary trees T1 and T2 on the given taxa. Both T1 and T2 
    are given in Newick format.
    Return: The quartet distance dq(T1,T2).
    '''
    input_lines = sys.stdin.read().splitlines()
    taxa = input_lines[0].split()
    nwck1 = input_lines[1]
    nwck2 = input_lines[2]

    print(quartet_distance(taxa, nwck1, nwck2))
