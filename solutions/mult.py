import sys
from itertools import product
from rosalind_utility import parse_fasta


def multiple_alignment(str_list):
    str_list = ["-" + string for string in str_list]

    score_mat = {}
    backtrack_mat = {}

    def add_tuples_elemwise(t1, t2):
        return tuple(sum(x) for x in zip(t1, t2))

    ## all possible "moves"
    perm_list = list(product([0, -1], repeat=len(str_list)))[1:]

    ## fill n-dimensional score and backtrack matrices
    for index in product(*map(range, map(lambda s: len(s) + 1, str_list))):
        if index.count(0) >= len(str_list) - 1:
            if sum(index) == 0:
                score_mat[index] = 0
            else:
                score_mat[index] = -max(index)
                move = tuple(0 if id == 0 else -1 for id in index)
                bck = -1
                for idx, perm in enumerate(perm_list):
                    if perm == move:
                        bck = idx
                        break
                backtrack_mat[index] = bck
        else:
            possible_scores = []
            for perm_idx, move in enumerate(perm_list):
                prev_idx = add_tuples_elemwise(index, move)
                if -1 not in prev_idx:
                    prev_score = score_mat[prev_idx]
                    chars = [str_list[i][index[i] - 1] if val == -1 else "-" for i, val in enumerate(move)]
                    current_cost = 0
                    for i in range(len(chars) - 1):
                        for j in range(i + 1, len(chars)):
                            if chars[i] != chars[j]:
                                current_cost -= 1
                    possible_scores.append((prev_score + current_cost, perm_idx))
            score_mat[index], backtrack_mat[index] = max(possible_scores, key=lambda p: p[0])

    ## backtrack
    alignment = ["" for x in str_list]
    current_index = list(map(len, str_list))
    max_score = score_mat[tuple(current_index)]

    while sum(current_index) != 0:
        back_perm_idx = backtrack_mat[tuple(current_index)]
        permutation = perm_list[back_perm_idx]
        for i, perm_value in enumerate(permutation):
            if perm_value == 0:
                alignment[i] = "-" + alignment[i]
            else:
                alignment[i] = str_list[i][current_index[i] - 1] + alignment[i]

        current_index = add_tuples_elemwise(tuple(current_index), permutation)

    ## remove all "-" columns
    to_rm_idx = []
    for pos in range(len(alignment[0])):
        temp = [x[pos] for x in alignment]
        if all(x == "-" for x in temp):
            to_rm_idx.append(pos)

    for i in range(len(alignment)):
        alignment[i] = "".join([char for idx, char in enumerate(alignment[i]) if idx not in to_rm_idx])

    return max_score, alignment


if __name__ == "__main__":
    '''
    Given: A collection of four DNA strings of length at most 10 bp in FASTA format.
    Return: A multiple alignment of the strings having maximum score, where we score matched symbols 0 (including 
    matched gap symbols) and all mismatched symbols -1 (thus incorporating a linear gap penalty of 1).
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_strings_list = list(parse_fasta(input_lines).values())

    score, alignment = multiple_alignment(DNA_strings_list)

    print(score)

    for aligned in alignment:
        print(aligned)



