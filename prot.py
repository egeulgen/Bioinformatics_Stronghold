import sys

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


def rna2prot(seq):
    ''' Translate RNA sequence to protein sequence
    :param seq: RNA sequence to translate (string)
    :return: the protein sequence (string)
    '''
    protein = ""
    for i in range(0, len(seq) - 2, 3):
        aa = CODON_TBL[seq[i:i+3]]
        if aa != "STOP":
            protein += aa
    return protein


if __name__ == "__main__":
    '''
    Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
    Return: The protein string encoded by s.
    '''
    input_lines = sys.stdin.read().splitlines()
    rna_str = input_lines[0]
    print(rna2prot(rna_str))
