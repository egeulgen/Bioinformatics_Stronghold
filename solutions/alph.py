import sys
import operator
from rosalind_utility import parse_fasta
from rosalind_utility import hamming_dist


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


def best_string(str1, str2):
    final_str = ""
    for pos in range(len(str1)):
        if str1[pos] == "-" and str2[pos] == "-":
            final_str += "A"
        elif str1[pos] == str2[pos]:
            final_str += str1[pos]
        elif str1[pos] != "-" and str2[pos] != "-":
            final_str += str1[pos]
        elif str1[pos] == "-":
            final_str += str2[pos]
        else:
            final_str += str1[pos]

    return final_str


class Newick():
    def __init__(self, data):
        self.nodes = []
        self.node_index = 0
        self.edges = []
        self.construct_tree(data)
        self.name_index = {node.name: node.number for node in self.nodes}

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

    def get_descendants(self, node_name):
        descendants = []
        for child in self.nodes[self.name_index[node_name]].children:
            descendants.append(self.nodes[child].name)
            descendants += self.get_descendants(self.nodes[child].name)
        return descendants

    def alph(self, m_alignment):
        new_m_alignment = {}
        remaining_nodes = [node for node in self.nodes if node.name not in new_m_alignment]

        inv_name_index = {v: k for k, v in self.name_index.items()}

        while remaining_nodes:
            for node in remaining_nodes:
                if node.name not in m_alignment:
                    if all(x in [self.name_index[name] for name in m_alignment] for x in node.children):
                        string = best_string(m_alignment[inv_name_index[node.children[0]]], m_alignment[inv_name_index[node.children[1]]])
                        m_alignment[node.name] = string
                        new_m_alignment[node.name] = string
                        remaining_nodes = [node for node in self.nodes if node.name not in m_alignment]
        return new_m_alignment, m_alignment

    def distance(self, m_alignment):
        inv_name_index = {v: k for k, v in self.name_index.items()}
        tot_dist = 0
        for edge in self.edges:
            tot_dist += hamming_dist(m_alignment[inv_name_index[edge[0]]], m_alignment[inv_name_index[edge[1]]])
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

    ## need to fix ""
    distance, internal_mult_alignment = ALPH(newick, multiple_alignment)
    print(distance)
    print_fasta(internal_mult_alignment)