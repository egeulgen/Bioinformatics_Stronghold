import sys
from rosalind_utility import parse_fasta
from rosalind_utility import hamming_dist


def most_frequent(List):
    return max(set(List), key=List.count)


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

    def alph(self, m_alignment):
        post_order = self.post_order_traversal()
        pre_order = self.pre_order_traversal()

        internal_mult_alignment = {}

        k = len(list(m_alignment.values())[0])
        for pos in range(k):
            options = {}
            for node_label in self.name_index:
                if node_label in m_alignment:
                    options[node_label] = {m_alignment[node_label][pos]}
                else:
                    options[node_label] = {}

            for node in post_order:
                if node.children:
                    common = options[self.inv_name_index[node.children[0]]] & options[self.inv_name_index[node.children[1]]]
                    union = options[self.inv_name_index[node.children[0]]] | options[self.inv_name_index[node.children[1]]]
                    options[node.name] = common if common else union

            for node in pre_order:
                if node.children:
                    if node.number == 0:
                        if node.name in internal_mult_alignment:
                            internal_mult_alignment[node.name] += options[node.name].pop()
                        else:
                            internal_mult_alignment[node.name] = options[node.name].pop()
                    else:
                        parent_node = self.nodes[node.parent]
                        parent_choice = internal_mult_alignment[parent_node.name][pos]
                        if parent_choice in options[node.name]:
                            if node.name in internal_mult_alignment:
                                internal_mult_alignment[node.name] += parent_choice
                            else:
                                internal_mult_alignment[node.name] = parent_choice
                        else:
                            if node.name in internal_mult_alignment:
                                internal_mult_alignment[node.name] += options[node.name].pop()
                            else:
                                internal_mult_alignment[node.name] = options[node.name].pop()

        for label, alignment in internal_mult_alignment.items():
            m_alignment[label] = alignment

        return internal_mult_alignment, m_alignment


    def distance(self, m_alignment):
        tot_dist = 0
        for edge in self.edges:
            tot_dist += hamming_dist(m_alignment[self.inv_name_index[edge[0]]], m_alignment[self.inv_name_index[edge[1]]])
        return tot_dist



def ALPH(nwck, m_alignment):
    tree = Newick(nwck)
    internal_m_alignment, m_alignment = tree.alph(m_alignment)
    dist = tree.distance(m_alignment)

    return dist, internal_m_alignment


def print_fasta(fasta_dict):
    for key, val in fasta_dict.items():
        print(">" + key)
        print(val)


if __name__ == "__main__":
    '''
    Given: A rooted binary tree T on n (n≤500) species, given in Newick format, followed by a multiple alignment of m 
    (m≤n) augmented DNA strings having the same length (at most 300 bp) corresponding to the species and given in FASTA 
    format.
    Return: The minimum possible value of dH(T), followed by a collection of DNA strings to be assigned to the internal 
    nodes of T that will minimize dH(T) (multiple solutions will exist, but you need only output one).
    '''
    input_lines = sys.stdin.read().splitlines()
    newick = input_lines[0]
    multiple_alignment = parse_fasta(input_lines[1:])

    ## need to fix "best_string"
    distance, internal_mult_alignment = ALPH(newick, multiple_alignment)
    print(distance)
    print_fasta(internal_mult_alignment)
