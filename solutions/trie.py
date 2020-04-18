import sys


class Trie:
    ''' Trie Structure
    '''

    def __init__(self):
        self.all_nodes = []
        self.all_edges = []
        self.root = self.add_node()

    class node:
        ''' Trie Node Structure
        '''

        def __init__(self):
            '''
            Each node has the following attributes:
            - label: node label
            - edges: list of edges from this node (edge objects)
            '''
            self.label = None
            self.edges = []

    class edge:
        ''' Trie Edge Structure
        '''

        def __init__(self):
            '''
            Each edge has the following attributes:
            - from_node: parent node object
            - target_node: child node object
            - label: label of this edge
            '''
            self.from_node = None
            self.target_node = None
            self.label = None

    def add_node(self):
        ''' Add a node
        Creates node newNode and adds this node to the trie
        Labels the new node with the next available integer
        (assuming root label is 1)
        '''
        newNode = Trie.node()
        newNode.label = len(self.all_nodes) + 1

        self.all_nodes.append(newNode)

        return newNode

    def add_edge(self, from_node, target_node, lbl):
        ''' Add an edge
        Creates edge newEdge from 'from_node' to 'target_node' with label
        Adds the new edge to 'from_node' and to the tree
        '''
        newEdge = Trie.edge()
        newEdge.from_node = from_node
        newEdge.target_node = target_node
        newEdge.label = lbl

        from_node.edges.append(newEdge)
        self.all_edges.append(newEdge)

        return newEdge

    @staticmethod
    def current_node_edge_labels(node):
        labels = []
        for edge in node.edges:
            labels.append(edge.label)
        return labels

    def construct_trie(self, seq_list):
        for seq in seq_list:
            current_node = self.root
            for char in seq:
                if char not in self.current_node_edge_labels(current_node):
                    child = self.add_node()
                    self.add_edge(current_node, child, char)
                for edge in current_node.edges:
                    if edge.label == char:
                        current_node = edge.target_node

    def __str__(self):
        ''' Custom __str__ method
        For printing the Trie as an adjacency list
        '''
        # header
        res = ""

        for edge in self.all_edges:
            res += str(edge.from_node.label) + ' ' + str(edge.target_node.label) + ' ' + str(edge.label) + '\n'

        return res

    def __repr__(self):
        return '<Trie adjacency list representation>'


if __name__ == "__main__":
    '''
    Given: A list of at most 100 DNA strings of length at most 100 bp, none of which is a prefix of another.
    Return: The adjacency list corresponding to the trie T for these patterns, in the following format. If T has n 
    nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n in any order you
    like. Each edge of the adjacency list of T will be encoded by a triple containing the integer representing the 
    edge's parent node, followed by the integer representing the edge's child node, and finally the symbol labeling the 
    edge.
    '''
    dna_strings = sys.stdin.read().splitlines()

    result = Trie()
    result.construct_trie(dna_strings)
    print(result)
