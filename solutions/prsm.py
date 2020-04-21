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


def complete_spectrum(protein):
    spectrum = []
    for i in range(len(protein) - 1):
        prefix = protein[:i + 1]
        mass = 0
        for aa in prefix:
            mass += MASS_TABLE[aa]
        spectrum.append(mass)

    protein = protein[::-1]
    for i in range(len(protein) - 1):
        suffix = protein[:i + 1]
        mass = 0
        for aa in suffix:
            mass += MASS_TABLE[aa]
        spectrum.append(mass)

    return spectrum


if __name__ == "__main__":
    '''
    Given: A positive integer n followed by a collection of n protein strings s1, s2, ..., sn and a multiset R of 
    positive numbers (corresponding to the complete spectrum of some unknown protein string).
    Return: The maximum multiplicity of R⊖S[sk] taken over all strings sk, followed by the string sk for which this 
    maximum multiplicity occurs (you may output any such value if multiple solutions exist).
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    protein_strings = []
    for i in range(1, n + 1):
        protein_strings.append(input_lines[i])
    R = []
    for j in range(n + 1, len(input_lines)):
        R.append(float(input_lines[j]))

    max_multiplicity = -1
    max_prot = ""
    for protein in protein_strings:
        spec = complete_spectrum(protein)

        diff_multiset = []
        for s1 in R:
            for s2 in spec:
                diff_multiset.append(round(s1 - s2, 5))

        for item in diff_multiset:
            multip = diff_multiset.count(item)
            if multip > max_multiplicity:
                max_multiplicity = multip
                max_prot = protein

    print(max_multiplicity)
    print(max_prot)