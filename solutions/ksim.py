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

        if i != len(str1) - 1:
            for j in range(len(str2) + 1):
                previous_row[j] = current_row[j]

    return current_row[-1]


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

    len_A = len(stringA)

    edit_dist_dict = {}

    for i in range(len(stringB)):
        j = len_A - k
        while j <= len_A + k:
            substr_B = stringB[i:i + j]

            if substr_B not in edit_dist_dict:
                edit_dist_dict[substr_B] = fast_edit_distance(substr_B, stringA)

            d = edit_dist_dict[substr_B]
            if d <= k:
                print(i + 1, len(substr_B))
            if d > k:
                break
            j += 1
