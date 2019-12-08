import sys

if __name__ == "__main__":
    '''
    Given: Six non-negative integers, each of which does not exceed 20,000. The integers correspond to the number of 
    couples in a population possessing each genotype pairing for a given factor. In order, the six given integers 
    represent the number of couples having the following genotypes:
    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa
    Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the 
    assumption that every couple has exactly two offspring.
    '''
    num_couples = [int(i) for i in sys.stdin.read().splitlines()[0].split(" ")]
    print(2 * (num_couples[0] + num_couples[1] + num_couples[2] + num_couples[3] * 3 / 4 + num_couples[4] / 2))