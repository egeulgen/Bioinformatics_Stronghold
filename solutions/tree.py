import sys


if __name__ == "__main__":
    '''
    Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains 
    no cycles.
    Return: The minimum number of edges that can be added to the graph to produce a tree.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    current_num_edges = len(input_lines) - 1

    # a tree with n edges always has n - 1 edges
    desired_num_edges = n - 1
    print(desired_num_edges - current_num_edges)
