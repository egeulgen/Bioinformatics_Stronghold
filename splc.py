import sys
from rosalind_utility import parse_fasta
from prot import rna2prot

CODON_TBL = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
}

if __name__ == "__main__":
    '''
    Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings 
    are given in FASTA format.
    Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will 
    exist for the dataset provided.)
    '''
    input_lines = sys.stdin.read().splitlines()
    strings = parse_fasta(input_lines)
    strings = list(strings.values()) ## dictionary keeps insertion order?
    DNA_string = strings[0]
    introns = strings[1:]
    for intron in introns:
        DNA_string = DNA_string.replace(intron, "")
    DNA_string = DNA_string.replace("T", "U")
    print(rna2prot(DNA_string))
