import sys


def ASMQ(dna_strings):
    total_len = sum([len(x) for x in dna_strings])
    dna_strings.sort(key=len)

    curr_len = 0
    n50 = total_len
    n75 = total_len
    for i in range(len(dna_strings) - 1, -1, -1):
        curr_len += len(dna_strings[i])
        if n50 == total_len and curr_len > total_len * 0.5:
            n50 = len(dna_strings[i])
        if curr_len > total_len * 0.75:
            n75 = len(dna_strings[i])
            break
    return n50, n75


if __name__ == "__main__":
    '''
    Given: A collection of at most 1000 DNA strings (whose combined length does not exceed 50 kbp).
    Return: N50 and N75 for this collection of strings.
    '''
    dna_strings = sys.stdin.read().splitlines()

    n50, n75 = ASMQ(dna_strings)

    print(str(n50) + ' ' + str(n75))