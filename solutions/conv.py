import sys


def Minkowski_difference(set1, set2):
    diff_multiset = []
    for s1 in set1:
        for s2 in set2:
            diff_multiset.append(round(s1 - s2, 5))

    multiplicities = {}
    for item in diff_multiset:
        multiplicities[item] = diff_multiset.count(item)

    max_val = -1
    for item, count in multiplicities.items():
        if count > max_val:
            max_val = count
            max_x = item

    return max_val, max_x


if __name__ == "__main__":
    '''
    Given: Two multisets of positive real numbers S1 and S2. The size of each multiset is at most 200.
    Return: The largest multiplicity of S1⊖S2, as well as the absolute value of the number x maximizing (S1⊖S2)(x) 
    (you may return any such value if multiple solutions exist).
    '''
    input_lines = sys.stdin.read().splitlines()

    S1 = [float(x) for x in input_lines[0].split()]
    S2 = [float(x) for x in input_lines[1].split()]

    res = Minkowski_difference(S1, S2)
    print(res[0])
    print(res[1])
