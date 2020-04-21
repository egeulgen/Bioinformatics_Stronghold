import sys
from numpy import zeros


def is_interwoven(dna1, dna2, superstr):
    if len(superstr) == 0:
        return True
    elif dna1[0] == dna2[0] == superstr[0]:
        return is_interwoven(dna1[1:], dna2, superstr[1:]) or is_interwoven(dna1, dna2[1:], superstr[1:])
    elif dna1[0] == superstr[0]:
        return is_interwoven(dna1[1:], dna2, superstr[1:])
    elif dna2[0] == superstr[0]:
        return is_interwoven(dna1, dna2[1:], superstr[1:])
    else:
        return False


if __name__ == "__main__":
    '''
    Given: A text DNA string s of length at most 10 kbp, followed by a collection of n (n≤10) DNA strings of length at 
    most 10 bp acting as patterns.
    Return: An n×n matrix M for which Mj,k=1 if the jth and kth pattern strings can be interwoven into s and Mj,k=0 
    otherwise.
    '''
    input_lines = sys.stdin.read().splitlines()

    super_string = input_lines[0]
    patterns = input_lines[1:]

    # Initialize the zero matrix.
    M = zeros((len(patterns), len(patterns)), dtype=int)

    # Run through all combinations of dna strings.
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            if i <= j:
                # Count the combined number of each type of nucleotide in given dna strands.
                current_profile = [(patterns[i] + patterns[j]).count(nuc) for nuc in "ACGT"]
                # Compare the current profile to each substring of the same length in the superstring.
                for index in range(len(super_string) - len(patterns[i]) - len(patterns[j]) + 1):
                    # Having an identical profile is a necessary condition in order to be interweavable, but less computationally intensive.
                    if current_profile == [super_string[index:index + len(patterns[i]) + len(patterns[j])].count(nuc)
                                           for nuc in "ACGT"]:
                        # Check the interweave if the profiles match, add an extra character outside the alphabet to avoid index out of range errors.
                        if is_interwoven(patterns[i] + '$', patterns[j] + '$', super_string[index:index + len(patterns[i]) + len(patterns[j])]):
                            M[i][j] = 1
                            break
            # The comparison are symmetric, so we've already done these computations.
            else:
                M[i][j] = M[j][i]

    for row in M:
        print(" ".join(map(str, row)))