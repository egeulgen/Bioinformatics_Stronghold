import sys
from scipy.special import comb
from numpy import zeros
from math import log10


if __name__ == "__main__":
    '''
    Given: Two positive integers N and m, followed by an array A containing k integers between 0 and 2N. A[j] represents
    the number of recessive alleles for the j-th factor in a population of N diploid individuals.
    Return: An m×k matrix B for which Bi,j represents the common logarithm of the probability that after i generations,
    no copies of the recessive allele for the j-th factor will remain in the population. Apply the Wright-Fisher model.
    '''
    input_lines = sys.stdin.read().splitlines()
    N, m = [int(x) for x in input_lines[0].split()]
    A = [int(x) for x in input_lines[1].split()]

    M = zeros((m, len(A)))
    for index, rec_allele in enumerate(A):
        p_rec = rec_allele/(2.0 * N)
        p = [comb(2 * N, i) * (p_rec ** i) * (1.0 - p_rec) ** (2 * N - i) for i in range(0, 2 * N + 1)]
        M[0][index] = log10(p[0])

        for gen in range(1, m - 1):
            temp_p = []
            for j in range(0, 2 * N + 1):
                temp_term = [comb(2 * N, j) * ((x / (2.0 * N)) ** j) * (1.0 - (x / (2.0 * N))) ** (2 * N - j) for x in range(0, 2 * N + 1)]
                temp_p.append(sum([temp_term[i] * p[i] for i in range(len(temp_term))]))
            p = temp_p
            M[gen][index] = log10(p[0])

        temp_term = [(1.0 - (x / (2.0 * N))) ** (2 * N) for x in range(0, 2 * N + 1)]
        M[m-1][index] = log10(sum([temp_term[i] * p[i] for i in range(len(temp_term))]))

    for row in M:
        print(" ".join(map(str, row)))
