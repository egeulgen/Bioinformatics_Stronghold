import sys
from rosalind_utility import parse_fasta


class Node():
    def __init__(self, number, parent, name = None):
        self.number = number
        self.parent = parent
        self.children = []
        self.name = "Node_" + str(self.number) if name is None else name

    def __repr__(self):
        tmp = ""
        if self.name != "Node_" + str(self.number):
            tmp = "(" + self.name + ")"
        return "Node_" + str(self.number) + tmp

    def add_child(self, child):
        '''Add a child to the node.'''
        self.children.append(child)


class Newick():
    def __init__(self, data):
        self.nodes = []
        self.node_index = 0
        self.edges = []
        self.construct_tree(data)
        self.name_index = {node.name: node.number for node in self.nodes}
        self.inv_name_index = {node.number: node.name for node in self.nodes}

    def construct_tree(self, data):
        '''Constructs the Newick Tree.'''
        data = data.replace(',', ' ').replace('(', '( ').replace(')', ' )').strip(';').split()
        current_parent = Node(-1, None)
        for item in data:
            if item[0] == '(':
                current_parent = Node(len(self.nodes), current_parent.number)
                self.nodes.append(current_parent)
                if len(self.nodes) > 1:
                    self.nodes[current_parent.parent].add_child(current_parent.number)
                    self.edges.append((current_parent.parent, current_parent.number))

            elif item[0] == ')':
                if len(item) > 1:
                    current_parent.name = item[1:]
                current_parent = self.nodes[current_parent.parent]

            else:
                self.nodes[current_parent.number].add_child(len(self.nodes))
                self.edges.append((current_parent.number, len(self.nodes)))
                self.nodes.append(Node(len(self.nodes), current_parent.number, item))

    def pre_order_traversal(self, node_index=0):
        res = []
        node = self.nodes[node_index]
        res.append(node)
        if node.children:
            res += self.pre_order_traversal(node.children[0])
            res += self.pre_order_traversal(node.children[1])
        return res

    def post_order_traversal(self, node_index=0):
        res = []
        node = self.nodes[node_index]
        if node.children:
            res = self.post_order_traversal(node.children[0])
            res += self.post_order_traversal(node.children[1])
        res.append(node)
        return res

    def max_depth(self, node):
        if not node.children:
            return 0

        left_depth = self.max_depth(self.nodes[node.children[0]])
        right_depth = self.max_depth(self.nodes[node.children[1]])

        if left_depth > right_depth:
            return left_depth + 1
        return right_depth + 1

    def all_paths(self, node):
        if not node.children:
            return []

        visited = [node.name]

        all_paths = []
        Q = [(node, [node.name])]

        while Q:
            current, path = Q.pop()
            for child_idx in current.children:
                path2 = path[:]
                child = self.nodes[child_idx]
                if child.name not in visited:
                    visited.append(child.name)
                    path2.append(child.name)
                    all_paths.append(path2[:])
                    Q.append((child, path2[:]))

        return all_paths

    def rsub(self, DNA_strings):
        rsub_list = []

        max_dep = self.max_depth(self.nodes[0])

        pre_order = self.pre_order_traversal()
        k = len(list(DNA_strings.values())[0])
        for pos in range(k):
            for node in pre_order:
                if node.children:
                    paths = self.all_paths(node)
                    for path in paths:
                        if len(path) >= 3:
                            nucs = [DNA_strings[label][pos] for label in path]
                            if nucs[0] == nucs[-1] and nucs[0] != nucs[1]:
                                if all(x == nucs[1:-1][0] for x in nucs[1:-1]):
                                    rsub_list.append([path[1], path[-1], str(pos + 1), "->".join([nucs[0], nucs[1], nucs[-1]])])
        return rsub_list


if __name__ == "__main__":
    '''
    Given: A rooted binary tree T with labeled nodes in Newick format, followed by a collection of at most 100 DNA 
    strings in FASTA format whose labels correspond to the labels of T. We will assume that the DNA strings have the 
    same length, which does not exceed 400 bp).
    Return: A list of all reversing substitutions in T (in any order), with each substitution encoded by the following 
    three items:
        the name of the species in which the symbol is first changed, followed by the name of the species in which it 
        changes back to its original state
        the position in the string at which the reversing substitution occurs; and
        the reversing substitution in the form original_symbol->substituted_symbol->reverted_symbol.
    '''
    input_lines = sys.stdin.read().splitlines()
    newick = input_lines[0]
    DNA_strings = parse_fasta(input_lines[1:])

    tree = Newick(newick)
    result = tree.rsub(DNA_strings)
    for r in result:
        print(" ".join(r))
