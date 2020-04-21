import sys

if __name__ == "__main__":
    '''
    Given: An array A for which A[k] represents the proportion of homozygous recessive individuals for the k-th 
    Mendelian factor in a diploid population. Assume that the population is in genetic equilibrium for all factors.
    Return: An array B having the same length as A in which B[k] represents the probability that a randomly selected 
    individual carries at least one copy of the recessive allele for the k-th factor.
    '''
    input_lines = sys.stdin.read().splitlines()
    A = map(float, input_lines[0].split())

    B = []
    for a in A:
        B.append(-a + 2 * a ** 0.5)

    print(" ".join(map(str, B)))

