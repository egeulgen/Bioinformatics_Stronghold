import sys


def fast_edit_distance(str1, str2):
    if str1 == str2:
        return 0
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    previous_row = [i for i in range(len(str2) + 1)]
    current_row = [0 for _ in range(len(str2) + 1)]

    for i in range(len(str1)):
        current_row[0] = i + 1
        for j in range(len(str2)):
            cost = 0 if str1[i] == str2[j] else 1
            current_row[j + 1] = min(current_row[j] + 1, previous_row[j + 1] + 1, previous_row[j] + cost)

        for j in range(len(str2) + 1):
            previous_row[j] = current_row[j]

    return current_row


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

    ### Still brute force - very slow
    result = []
    for i in range(len(stringB) + len(stringA) - k):
        str_B = stringB[i:]
        last_row = fast_edit_distance(stringA, str_B)
        idx = [j for j in range(len(str_B)) if last_row[j] <= k]
        for j in idx:
            print(i + 1, j)