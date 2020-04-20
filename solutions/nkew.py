import sys


class Node():
    def __init__(self, number, parent, name = None):
        self.number = number
        self.parent = parent
        self.name = "Node_" + str(self.number) if name is None else name

    def __repr__(self):
        tmp = ""
        if self.name != "Node_" + str(self.number):
            tmp = "(" + self.name + ")"
        return "Node_" + str(self.number) + tmp


class WeightedNewick():
    def __init__(self, data):
        self.nodes = []
        self.edge_weight = {}
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

            elif item[0] == ')':
                if len(item) > 1:
                    self.edge_weight[(current_parent.number, current_parent.parent)] = int(item[item.find(':') + 1:])
                    if len(item) > 2:
                        current_parent.name = item[1:item.find(':')]
                current_parent = self.nodes[current_parent.parent]

            else:
                self.edge_weight[(len(self.nodes), current_parent.number)] = int(item[item.find(':') + 1:])
                self.nodes.append(Node(len(self.nodes), current_parent.number, item[:item.find(':')]))

    def distance(self, name1, name2):
        '''Returns the distance between name1 and name2.'''
        if name1 == name2:
            return 0

        # Create the branches from the two desired nodes to the root.
        idx1 = self.name_index[name1]
        branch1 = [(idx1, self.nodes[idx1].parent)]
        idx2 = self.name_index[name2]
        branch2 = [(idx2, self.nodes[idx2].parent)]
        while branch1[-1][1] != -1:
            current_idx = branch1[-1][1]
            branch1.append((current_idx, self.nodes[current_idx].parent))
        while branch2[-1][1] != -1:
            current_idx = branch2[-1][1]
            branch2.append((current_idx, self.nodes[current_idx].parent))

        return sum([self.edge_weight[edge] for edge in set(branch1) ^ set(branch2)])


if __name__ == "__main__":
    '''
    Given: A collection of n weighted trees (n≤40) in Newick format, with each tree containing at most 200 nodes; each 
    tree Tk is followed by a pair of nodes xk and yk in Tk.
    Return: A collection of n numbers, for which the kth number represents the distance between xk and yk in Tk.
    '''
    input_lines = sys.stdin.read().splitlines()

    distance_list = []
    for i in range(0, len(input_lines) - 1, 3):
        tree = input_lines[i]
        nodeA, nodeB = input_lines[i + 1].split()

        distance_list.append(str(WeightedNewick(tree).distance(nodeA, nodeB)))

    print(" ".join(distance_list))
