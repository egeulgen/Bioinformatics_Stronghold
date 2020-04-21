import sys


class Tree:
    ''' Tree Structure
    '''

    def __init__(self):
        self.all_edges = []
        self.nodes_dict = {}

    class node:
        ''' Tree Node Structure
        '''

        def __init__(self):
            '''
            Each node has the following attributes:
            - label: node label
            - edges: list of edges from this node (edge objects)
            - depth: depth of node (by default 0)
            - number of leaves below node
            '''
            self.label = None
            self.edges = []
            self.depth = 0
            self.num_leaves = 0

    class edge:
        ''' Tree Edge Structure
        '''

        def __init__(self):
            '''
            Each edge has the following attributes:
            - target_node: target node object
            - position: position of the substring in Text (used to construct the tree) belonging this edge
            - length: length of substring belonging to this edge
            '''
            self.from_node = None
            self.target_node = None
            self.position = None
            self.length = None

    def add_node(self, label):
        ''' Add a node
        If the node exists, returns the node
        Creates node newNode, labels the new node with "label", adds this node to the tree and
        :returns "new_node" (node object)
        '''
        if label in self.nodes_dict:
            return self.nodes_dict[label]
        new_node = Tree.node()
        new_node.label = label
        self.nodes_dict[label] = new_node
        return new_node

    def add_edge(self, from_node, target_node, pos, length):
        ''' Add an edge
        Creates edge "new_edge" from "from_node" to "target_node" with position "pos"
        and length 'length'
        Updates depth attribute of 'target_node'
        Adds the new edge to "from_node" and to the tree
        :returns "new_edge" (edge object)
        '''
        new_edge = Tree.edge()
        new_edge.from_node = from_node
        new_edge.target_node = target_node
        new_edge.position = pos
        new_edge.length = length

        target_node.depth = from_node.depth + length

        from_node.edges.append(new_edge)
        self.all_edges.append(new_edge)

        return new_edge

    def get_descendants(self, label):
        descendants = []
        for edge in self.nodes_dict[label].edges:
            child = edge.target_node
            descendants.append(child)
            descendants += self.get_descendants(child.label)
        return descendants

    def num_leaves_below_node(self, label):
        node = self.nodes_dict[label]
        all_descendants = self.get_descendants(node.label)
        num_leaves = 0
        for desc in all_descendants:
            if not desc.edges:
                num_leaves += 1
        node.num_leaves = num_leaves

    def __str__(self):
        ''' Custom __str__ method
        For printing the Trie as an adjacency list
        '''
        # header
        res = 'From->To:position:length\n\n'

        for edge in self.all_edges:
            res += str(edge.from_node.label) + '->' + str(edge.target_node.label) + ':' + str(
                edge.position) + ':' + str(edge.length) + '\n'

        return res

    def __repr__(self):
        return '<Tree object>'


def backtrace_path_from_node(tree, node, Text):
    # if root is reached, stop
    if node.label == "node1":
        return ''

    for edge in tree.all_edges:
        if edge.target_node == node:
            incoming_edge = edge
            break

    path_substring = Text[incoming_edge.position - 1: incoming_edge.position + incoming_edge.length - 1]

    path_substring = backtrace_path_from_node(tree, incoming_edge.from_node, Text) + path_substring

    return path_substring


def find_longest_repeated_substring(suffix_tree, Text_s, k):
    # Basically, build the suffix tree, match the substring starting from the root and count the leaf nodes below that
    # point. That's the number of times the word appears in the text.

    candidate_nodes = []
    for label, node in suffix_tree.nodes_dict.items():
        suffix_tree.num_leaves_below_node(label)
        if len(node.edges) != 0 and node.num_leaves >= k:
            candidate_nodes.append(node)

    longest_substring = ""
    for candidate in candidate_nodes:
        substr = backtrace_path_from_node(suffix_tree, candidate, Text_s)
        if len(substr) > len(longest_substring):
            longest_substring = substr
    return longest_substring


def build_tree_from_edges(edges_list):
    suffix_tree = Tree()
    for edge in edges_list:
        edge = edge.split()
        node_A = suffix_tree.add_node(edge[0])
        node_B = suffix_tree.add_node(edge[1])
        suffix_tree.add_edge(node_A, node_B, int(edge[2]), int(edge[3]))
    return suffix_tree


if __name__ == "__main__":
    '''
    Given: A DNA string s (of length at most 20 kbp) with $ appended, a positive integer k, and a list of edges defining 
    the suffix tree of s. Each edge is represented by four components:
        the label of its parent node in T(s);
        the label of its child node in T(s);
        the location of the substring t of s∗ assigned to the edge; and
        the length of t.
    Return: The longest substring of s that occurs at least k times in s. (If multiple solutions exist, you may return 
    any single solution.)
    '''
    input_lines = sys.stdin.read().splitlines()
    Text_s = input_lines[0]
    k = int(input_lines[1])
    edges = input_lines[2:]

    suffix_tree = build_tree_from_edges(edges)
    print(find_longest_repeated_substring(suffix_tree, Text_s, k))
