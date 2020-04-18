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


if __name__ == "__main__":
    '''
    Given: A list L of n (n≤100) positive real numbers.
    Return: A protein string of length n−1 whose prefix spectrum is equal to L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.
    '''
    input_lines = sys.stdin.read().splitlines()
    prefix_spectrum = [float(w) for w in input_lines]

    differences = [w1 - w2 for w2, w1 in zip(prefix_spectrum, prefix_spectrum[1: ])]
    prt_seq = ""
    for weight in differences:
        prt_seq += min(MASS_TABLE.items(), key=lambda x: abs(x[1] - weight))[0]

    print(prt_seq)
