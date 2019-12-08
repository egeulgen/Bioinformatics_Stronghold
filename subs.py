import sys


def substr_locs(string, substr):
    ''' Locate all occurrences of substring in string
    :param string: string to search within (string)
    :param substr: substring to search for (string)
    :return: the locations of substring occurrences in string (list of integers, 1-based)
    '''
    match_idx = []
    k = len(substr)
    for i in range(len(string) - k + 1):
        if string[i:i+k] == substr:
            match_idx.append(i + 1)
    return match_idx


if __name__ == "__main__":
    '''
    Given: Two DNA strings s and t (each of length at most 1 kbp).
    Return: All locations of t as a substring of s.
    '''
    input_lines = sys.stdin.read().splitlines()
    s = input_lines[0]
    t = input_lines[1]
    result = (substr_locs(s, t))
    print(' '.join([str(idx) for idx in result]))
