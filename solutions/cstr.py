import sys

if __name__ == "__main__":
    '''
    Given: A collection of at most 100 characterizable DNA strings, each of length at most 300 bp.
    Return: A character table for which each nontrivial character encodes the symbol choice at a single position of the 
    strings. (Note: the choice of assigning '1' and '0' to the two states of each SNP in the strings is arbitrary.)
    '''
    input_lines = sys.stdin.read().splitlines()

    base = input_lines[0]
    for i in range(len(base)):
        cnt_0 = 0
        cnt_1 = 0
        row = ''
        for seq in input_lines:
            if base[i] == seq[i]:
                row += '1'
                cnt_1 += 1
            else:
                row += '0'
                cnt_0 += 1
        if cnt_1 > 1 and cnt_0 > 1:
            print(row)

