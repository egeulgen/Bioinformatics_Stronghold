import sys
import collections


def all_reversals(permutation):
    """ Generator for all reversals of a permutation
    :param permutation: the input permutation string
    :return: each reversal of the permutation
    """
    for i in range(len(permutation)):
        for j in range(i + 2, len(permutation) + 1):
            yield permutation[:i] + permutation[i:j][::-1] + permutation[j:], (i + 1, j)


def determine_reversals(p_init, p_target):
    """ Sorting by reversals
    :param p_init: the initial permutation string
    :param p_target: the target permutation string
    :return: the reversal distance (int) and the reversal endpoint indices (list of 2-tuples)
    """
    # if the permutations are equal, the reversal distance is 0 with no reversals
    if p_init == p_target:
        return 0, ("", "")

    # search forwards
    q = collections.deque((p_init, ))
    dist_init = {p_init: 0}
    rev_hist_init = {p_init: []}
    while q:
        perm = q.popleft()
        dist = dist_init[perm]
        rev_hist = rev_hist_init[perm]

        for (perm_new, rev) in all_reversals(perm):
            if perm_new == p_target:
                return dist + 1, rev_hist + [rev]
            if perm_new not in dist_init:
                dist_init[perm_new] = dist + 1
                rev_hist_init[perm_new] = rev_hist + [rev]
                if dist != 4:
                    q.append(perm_new)

    # search backwards
    q = collections.deque((p_target,))
    dist_target = {p_target: 0}
    rev_hist_target = {p_target: []}
    final_dist = 1e6
    while q:
        perm = q.popleft()
        dist = dist_target[perm]
        rev_hist = rev_hist_target[perm]

        for (perm_new, rev) in all_reversals(perm):
            if perm_new not in dist_target:
                dist_target[perm_new] = dist + 1
                rev_hist_target[perm_new] = rev_hist + [rev]
                if dist != 3:
                    q.append(perm_new)
            if perm_new in dist_init:
                if final_dist > dist_init[perm_new] + dist_target[perm_new]:
                    final_dist = dist_init[perm_new] + dist_target[perm_new]
                    final_rev_hist = rev_hist_init[perm_new] + rev_hist_target[perm_new][::-1]
    return final_dist, final_rev_hist


if __name__ == "__main__":
    '''
    Given: Two permutations π and γ, each of length 10.
    Return: The reversal distance drev(π,γ), followed by a collection of reversals sorting π into γ. If multiple collections of such reversals exist, you may return any one.
    '''
    input_lines = sys.stdin.read().splitlines()
    perm1 = tuple([x for x in input_lines[0].split()])
    perm2 = tuple([x for x in input_lines[1].split()])

    (rev_distance, revs_list) = determine_reversals(perm1, perm2)
    print(rev_distance)
    for (x1, x2) in revs_list:
        print(x1, x2)
