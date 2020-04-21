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


def find_weight_match(current_w, w_list):
    for weight in w_list:
        for aa, wt in MASS_TABLE.items():
            if abs(wt - (weight - current_w)) < 0.01:
                return aa
    return -1


if __name__ == "__main__":
    '''
    Given: A list L containing 2n+3 positive real numbers (n≤100). The first number in L is the parent mass of a peptide 
    P, and all other numbers represent the masses of some b-ions and y-ions of P (in no particular order). You may 
    assume that if the mass of a b-ion is present, then so is that of its complementary y-ion, and vice-versa.
    Return: A protein string t of length n for which there exist two positive real numbers w1 and w2 such that for every 
    prefix p and suffix s of t, each of w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists a
    protein string whose t-prefix and t-suffix weights correspond to the non-parent mass values of L.) If multiple 
    solutions exist, you may output any one.
    '''
    input_lines = sys.stdin.read().splitlines()

    weights = [float(x) for x in input_lines]
    n = (len(weights) - 3) / 2

    protein = ""
    current = weights[1]
    remaining_weights = weights[2:]

    while len(protein) < n:
        aa = find_weight_match(current, remaining_weights)
        if aa == -1:
            break
        else:
            protein += aa
            current += MASS_TABLE[aa]
            remaining_weights = list(filter(lambda w: w - current > 0, remaining_weights))

    print(protein)