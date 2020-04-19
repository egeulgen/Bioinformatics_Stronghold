import sys


def expected_num_substrings(n, substring, gc_content):
    num_gc = substring.count("G") + substring.count("C")
    num_at = substring.count("A") + substring.count("T")
    num_slots = n - len(substring) - 1
    # The probability the a randomly created dna sequence will with a specific GC content will match the
    # given dna sequence.
    dna_prob = ((0.5 * gc_content) ** num_gc) * ((0.5 * (1 - gc_content)) ** num_at)
    return dna_prob * num_slots


if __name__ == "__main__":
    '''
    Given: A positive integer n (n≤1,000,000), a DNA string s of even length at most 10, and an array A of length at 
    most 20, containing numbers between 0 and 1.
    Return: An array B having the same length as A in which B[i] represents the expected number of times that s will 
    appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i] 
    (see “Introduction to Random Strings”).
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    substr = input_lines[1]
    gc_content_list = [float(gc) for gc in input_lines[2].split()]

    results = []
    for gc_content in gc_content_list:
        results.append(str(expected_num_substrings(n, substr, gc_content)))

    print(" ".join(results))