import sys
from rosalind_utility import parse_fasta
from rosalind_utility import rev_comp

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


def possible_proteins(string):
    ''' Find Possible Proteins from ORFs
    :param string: DNA string
    :return: possible protein strings
    '''
    start_pos_list = []
    for i in range(len(string) - 2):
        if string[i:i + 3] == "ATG":
            start_pos_list.append(i)
    protein_list = set()
    for start_pos in start_pos_list:
        protein = ""
        for i in range(start_pos, len(string) - 2, 3):
            triplet = string[i:i + 3].replace("T", "U")
            aa = CODON_TBL[triplet]
            if aa == "STOP":
                protein_list.add(protein)
                break
            protein += aa
    return protein_list


if __name__ == "__main__":
    '''
    Given: A DNA string s of length at most 1 kbp in FASTA format.
    Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned 
    in any order.
    '''
    input_lines = sys.stdin.read().splitlines()
    DNA_string = parse_fasta(input_lines)
    DNA_string = list(DNA_string.values())[0]
    rev_string = rev_comp(DNA_string)
    protein_strings = possible_proteins(DNA_string)
    rev_protein_strings = possible_proteins(rev_string)
    for protein in (protein_strings | rev_protein_strings):
        print(protein)
