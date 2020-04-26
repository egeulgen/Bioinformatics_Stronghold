import sys

if __name__ == "__main__":
    '''
    Given: A positive integer n (n≤1000000) followed by an array P of length m (m≤20) containing numbers between 0 and 
    1. Each element of P can be seen as representing a probability corresponding to an allele frequency.
    Return: An array B of length m for which B[k] is the expected value of Bin(n,P[k]); in terms of Wright-Fisher, it 
    represents the expected allele frequency of the next generation.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    P_list = [float(p) for p in input_lines[1].split()]

    result = []
    for p_val in P_list:
        result.append(n * p_val)

    print(" ".join(map(str, result)))
