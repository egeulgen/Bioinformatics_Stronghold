import sys

def mortal_fibonacci(n, m):
    ''' Modified Fibonacci Sequence
    :param n: number of generations (integer)
    :param k: number of pairs a reproduction age pair of rabbits produces (integer)
    :return: the nth element in the sequence (integer)
    '''
    rabbits = [0] * m
    rabbits[0] = 1
    for i in range(n-1):
        newborns = sum(rabbits[1:])
        rabbits = [newborns] + rabbits[:m-1]
    return sum(rabbits)


if __name__ == "__main__":
    '''
    Given: Positive integers n≤100 and m≤20.
    Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
    '''
    n, m = [int(x) for x in sys.stdin.read().splitlines()[0].split(" ")]
    print(mortal_fibonacci(n, m))
