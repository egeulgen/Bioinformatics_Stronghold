import sys
from scipy.special import comb

if __name__ == "__main__":
    '''
    Given: Positive integers N (N≤7), m (m≤2N), g (g≤6) and k (k≤2N).
    Return: The probability that in a population of N diploid individuals initially possessing m copies of a dominant 
    allele, we will observe after g generations at least k copies of a recessive allele. Assume the Wright-Fisher model.
    '''
    input_lines = sys.stdin.read().splitlines()
    N, m, g, k = [int(x) for x in input_lines[0].split()]

    p_rec = 1 - m / (2.0 * N)
    # probabilities of given number of recessive alleles in the Generation 1
    previous_p = [comb(2 * N, i) * p_rec ** i * (1 - p_rec) ** (2 * N - i) for i in range(1, 2 * N + 1)]

    # probabilities of given number of recessive alelles in generations 2, ..., g
    # P(1 Rec in current gen.) = P(1 Rec in current gen. | 0 rec in previous gen.) + ... +
    # P(1 rec in current gen. | 2N rec in previous gen.)
    for generation in range(2, g + 1):
        current_p = []
        for j in range(1, 2 * N + 1):
            temp = [comb(2 * N, j) * (x / (2 * N)) ** j * (1 - x / (2 * N)) ** (2 * N -j) for x in range(1, 2 * N + 1)]
            current_p.append(sum(temp[i] * previous_p[i] for i in range(len(temp))))
        previous_p = current_p

    final_prob = sum(current_p[k - 1:])
    print(final_prob)