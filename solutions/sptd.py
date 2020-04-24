import sys
import random


def get_fingerprints_list(taxa_dict, tree):
    result = []
    last_symbol = ''
    taxon = ''
    taxa_stack = []
    for next_symbol in tree:
        if next_symbol == '(' or next_symbol == ',' or next_symbol == ')':
            if last_symbol == '(' or last_symbol == ',':
                if taxon:
                    taxa_stack.append(taxa_dict[taxon])
            elif last_symbol == ')':
                t1 = taxa_stack.pop()
                t2 = taxa_stack.pop()
                res = t1 ^ t2
                t = res
                result.append(t)
                taxa_stack.append(t)
            last_symbol = next_symbol
            taxon = ''
        else:
            if next_symbol != ' ':
                taxon += next_symbol
    return result


def find_split_distance(taxa, tree1, tree2):
    taxa_dict = {taxon: random.randint(0, 2 << 11) for taxon in taxa}

    fingerprints1 = sorted(get_fingerprints_list(taxa_dict, tree1))
    fingerprints2 = sorted(get_fingerprints_list(taxa_dict, tree2))

    shared = 0
    i = len(fingerprints1) - 1
    j = len(fingerprints2) - 1
    while i > -1 and j > -1:
        if fingerprints1[i] == fingerprints2[j]:
            i -= 1
            j -= 1
            shared += 1
        elif fingerprints1[i] > fingerprints2[j]:
            i -= 1
        elif fingerprints1[i] < fingerprints2[j]:
            j -= 1

    result = 2 * (len(taxa) - 3) - 2 * shared

    return result


if __name__ == "__main__":
    '''
    Let B(n) represent the total number of distinct rooted binary trees on n labeled taxa.
    Given: A collection of at most 3,000 species taxa and two unrooted binary trees T1 and T2 on these 
    taxa in Newick format.
    Return: The split distance dsplit(T1,T2).
    '''
    input_lines = sys.stdin.read().splitlines()
    taxa = input_lines[0].split()
    tree1 = input_lines[1]
    tree2 = input_lines[2]

    max_result = 0
    for i in range(500):
        result = find_split_distance(taxa, tree1, tree2)
        if result > max_result:
            max_result = result

    print(max_result)
