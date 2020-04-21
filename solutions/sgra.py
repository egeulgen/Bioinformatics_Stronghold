import sys
MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}

def find_weight_match(approx_weight, error = 0.001):
    for aa, weight in MASS_TABLE.items():
        if abs(weight - approx_weight) < error:
            return aa
    return None


def construct_spectrum_graph(spectrum):
    graph = {}
    for w1 in spectrum:
        for w2 in spectrum:
            if w2 > w1 and find_weight_match(w2 - w1) is not None:
                graph[(w1, w2)] = find_weight_match(w2 - w1)
    return graph


def find_longest_path(graph):
    longest_string = ""
    for edge, label in graph.items():
        protein_string = label

        possible_edges = []
        for e in graph.keys():
            if e[0] == edge[1]:
                possible_edges.append(e)

        while possible_edges:
            for edge2, label2 in graph.items():
                if edge2[0] == edge[1]:
                    edge = edge2
                    protein_string += label2
                    possible_edges = []
                    for e in graph.keys():
                        if e[0] == edge[1]:
                            possible_edges.append(e)
        if len(protein_string) > len(longest_string):
            longest_string = protein_string
    return longest_string


if __name__ == "__main__":
    '''
    Given: A list L (of length at most 100) containing positive real numbers.
    Return: The longest protein string that matches the spectrum graph of L (if multiple solutions exist, you may output any
    one of them). Consult the monoisotopic mass table.
    '''
    input_lines = sys.stdin.read().splitlines()
    spectrum = [float(wt) for wt in input_lines]

    spectrum_graph = construct_spectrum_graph(spectrum)
    print(find_longest_path(spectrum_graph))
