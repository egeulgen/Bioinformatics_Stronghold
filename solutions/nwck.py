import sys


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
        self.children.append(child)


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

    def edge_names(self):
        '''Return a list of edges referencing node names.'''
        return [(self.nodes[edge[0]].name, self.nodes[edge[1]].name) for edge in self.edges]

    def distance(self, name1, name2):
        '''Returns the distance between name1 and name2.'''
        if name1 == name2:
            return 0

        # Create the branches from the two desired nodes to the root.
        branch1 = [self.name_index[name1]]
        branch2 = [self.name_index[name2]]
        while self.nodes[branch1[-1]].parent != -1:
            branch1.append(self.nodes[branch1[-1]].parent)
        while self.nodes[branch2[-1]].parent != -1:
            branch2.append(self.nodes[branch2[-1]].parent)

        return len(set(branch1) ^ set(branch2))


if __name__ == "__main__":
    '''
    Given: A collection of n trees (n≤40) in Newick format, with each tree containing at most 200 nodes; each tree Tk is followed by a pair of nodes xk and yk in Tk.
    Return: A collection of n positive integers, for which the kth integer represents the distance between xk and yk in Tk.
    '''
    input_lines = sys.stdin.read().splitlines()

    distance_list = []
    for i in range(0, len(input_lines) - 2, 3):
        tree = input_lines[i]
        nodeA, nodeB = input_lines[i + 1].split()

        distance_list.append(str(Newick(tree).distance(nodeA, nodeB)))

    print(" ".join(distance_list))
