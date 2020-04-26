import sys
from Bio import Phylo


if __name__ == "__main__":
    '''
    Given: A list of n species (n≤80) and an n-column character table C in which the jth column denotes the jth species.
    Return: An unrooted binary tree in Newick format that models C.
    '''
    ## solution from https://github.com/pjvandehaar/rosalind/blob/master/chbp.py, will attempt again later

    input_lines = sys.stdin.read().splitlines()
    clades = list(Phylo.BaseTree.Clade(name=name) for name in input_lines[0].split())

    splits = []
    for line in input_lines[1:]:
        splits.append([int(x) for x in line])


    def find_cols_to_unify(splits):
        for split in splits:
            if 2 == sum(split):
                return tuple(i for i, x in enumerate(split) if x == 1)
            elif len(split) - 2 == sum(split):
                return tuple(i for i, x in enumerate(split) if x == 0)
        raise Exception('no cols to unify!', splits)


    def print_clades(clades):
        for clade in clades:
            tree = Phylo.BaseTree.Tree.from_clade(clade)
            Phylo.write(tree, sys.stdout, 'newick', plain=True)


    while 0 < len(splits):
        col1, col2 = find_cols_to_unify(splits)

        # remove the second of the unified columns
        for split in splits:
            split.pop(col2)
        # remove all trivial splits
        splits = list(split for split in splits if sum(split) > 1 and sum(split) + 1 < len(split))

        # unify the clades
        clades[col1] = Phylo.BaseTree.Clade(clades=[clades[col1], clades[col2]])
        clades.pop(col2)

    final_clade = Phylo.BaseTree.Clade(clades=clades)
    print_clades([final_clade])