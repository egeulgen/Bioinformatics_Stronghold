import sys


def parse_set(txt):
    res = txt[1:-1]
    res = [int(e) for e in res.split(", ")]
    res = set(res)
    return res


def repr_set(set_x):
    return "{" + ", ".join(str(x) for x in set_x) + "}"


if __name__ == "__main__":
    '''
    Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.
    Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are taken with respect to {1,2,…,n}).
    '''
    input_lines = sys.stdin.read().splitlines()

    N = int(input_lines[0])
    A = parse_set(input_lines[1])
    B = parse_set(input_lines[2])

    Univ_set = set([i for i in range(1, N + 1)])

    union_set = A | B
    intersection_set = A & B
    C = A - B
    D = B - A
    Ac = Univ_set - A
    Bc = Univ_set - B

    print(repr_set(union_set))
    print(repr_set(intersection_set))
    print(repr_set(C))
    print(repr_set(D))
    print(repr_set(Ac))
    print(repr_set(Bc))
