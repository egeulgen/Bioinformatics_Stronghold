import sys
from rosalind_utility import parse_fasta

def superstring(strings):
    ''' Create Superstring
    :param strings: list of DNA strings
    :return: superstring via maximal overlap
    '''
    max_k = len(strings[0])
    min_k = max_k // 2 + 1
    super_string = strings.pop(0)
    while strings:
        for candidate in strings:
            for l in range(min_k, max_k):
                if candidate[-l:] == super_string[:l]:
                    super_string = candidate + super_string[l:]
                    strings.remove(candidate)
                    break
                elif candidate[:l] == super_string[-l:]:
                    super_string = super_string + candidate[l:]
                    strings.remove(candidate)
                    break

    return super_string


if __name__ == "__main__":
    '''
    Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent 
    reads deriving from the same strand of a single linear chromosome).
    The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire 
    chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
    Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
    '''
    input_lines = sys.stdin.read().splitlines()
    fasta_dict = parse_fasta(input_lines)
    DNA_strings = list(fasta_dict.values())
    print(superstring(DNA_strings))
