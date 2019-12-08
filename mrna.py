import sys

reverse_table = {
    'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'G': 4,
    'C': 2, 'W': 1, 'P': 4, 'H': 2, 'Q': 2,
    'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2,
    'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2
}

if __name__ == "__main__":
    '''
    Given: A protein string of length at most 1000 aa.
    Return: The total number of different RNA strings from which the protein could have been translated, modulo 
    1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
    '''
    protein = sys.stdin.read().splitlines()[0]

    possible = 1
    for aa in protein:
        possible *= reverse_table[aa]
    # stop codons
    possible *= 3

    possible = possible % 10 ** 6
    print(possible)
