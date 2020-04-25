import sys


if __name__ == "__main__":
    '''
    Given: An array A of length n for which A[k] represents the proportion of males in a population exhibiting the k-th 
    of n total recessive X-linked genes. Assume that the population is in genetic equilibrium for all n genes.
    Return: An array B of length n in which B[k] equals the probability that a randomly selected female will be a carrier
    for the k-th gene.
    '''
    input_lines = sys.stdin.read().splitlines()
    A = [float(x) for x in input_lines[0].split()]

    B = []
    for a in A:
        B.append(a * (1 - a) * 2)

    print(" ".join(map(str, B)))