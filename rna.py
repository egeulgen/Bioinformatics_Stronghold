import sys


def transcribe(sequence):
    ''' Transcribe a DNA sequence to an RNA sequence
    :param sequence: sequence to transcribe from (string)
    :return: the transcribed RNA (string)
    '''
    return sequence.replace('T', 'U')


if __name__ == "__main__":
    '''
    Given: A DNA string t having length at most 1000 nt.
    Return: The transcribed RNA string of t.
    '''
    DNA_seq = sys.stdin.read().splitlines()[0]
    print(transcribe(DNA_seq))