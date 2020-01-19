import sys
from rosalind_utility import parse_fasta


def calculate_gc_content(string):
    ''' Calculate GC content
    :param string: string to calculate GC content for (string)
    :return: GC content (float)
    '''
    count_gc = string.count("G") + string.count("C")
    gc_content = count_gc / len(string)
    return gc_content


if __name__ == "__main__":
    '''
    Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
    Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_strs = parse_fasta(input_lines)
    max_GC_content = -1
    max_name = ''
    for name, seq in DNA_strs.items():
        GC_content = calculate_gc_content(seq)
        if GC_content > max_GC_content:
            max_name = name
            max_GC_content = GC_content
    print(max_name)
    print(max_GC_content * 100)
