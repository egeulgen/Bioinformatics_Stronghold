import sys
import urllib.request
from re import finditer


def get_fasta(id):
    urllib.request.urlretrieve("http://www.uniprot.org/uniprot/" + id + ".fasta", "temp.fa")
    file = open("temp.fa")
    string = []
    for line in file:
        if not line.startswith(">"):
            string.append(line.rstrip())
    string = "".join(string)
    return string


if __name__ == "__main__":
    '''
    Given: At most 15 UniProt Protein Database access IDs.
    Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of 
    1locations in the protein string where the motif can be found.
    N{P}[ST]{P}
    '''
    uniprot_ids = sys.stdin.read().splitlines()

    for id in uniprot_ids:
        fasta_string = get_fasta(id)
        # Find all the positions of the N-glycosylation motif.
        locations = [g.start() + 1 for g in finditer(r'(?=N[^P][ST][^P])', fasta_string)]
        if len(locations) != 0:
            print(id)
            print(" ".join(map(str, locations)))
