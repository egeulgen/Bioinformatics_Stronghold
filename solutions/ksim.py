import sys
from edit import edit_distance


if __name__ == "__main__":
    '''
    Given: A positive integer k (k≤50), a DNA string s of length at most 5 kbp representing a motif, and a DNA string t 
    of length at most 50 kbp representing a genome.
    Return: All substrings t′ of t such that the edit distance dE(s,t′) is less than or equal to k. Each substring 
    should be encoded by a pair containing its location in t followed by its length.
    '''
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])
    stringA = input_lines[1]
    stringB = input_lines[2]

    ## Find a faster solution!!!!!
    result = []
    checked = []
    for i in range(len(stringB) - 2):
        for j in range(i + 2, len(stringB)):
            substring = stringB[i:j]
            if edit_distance(stringA, substring) <= k:
                result.append((i + 1, len(substring)))

    for r in result:
        print(str(r[0]) + " " + str(r[1]))
