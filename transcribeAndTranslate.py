#!/usr/bin/env python
# coding: utf-8

#Loading the required modules
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#Definition for transcribing and translating
def transcribe_translate(sequence):
    coding_dna = Seq(sequence, IUPAC.unambiguous_dna)
    print(f"Original Sequence   : {sequence}")
    print(f"Transcribe Sequence : {coding_dna.transcribe()}")
    print(f"Translated Sequence : {coding_dna.translate()}")
    print("\n")

#Main definition
def main():
    for sequence in ["ATGATTGGCCCGGTTTTTTAA", "GTGGTGGGGAAATTCCGCTGA"]:
        transcribe_translate(sequence)

#Invokes the main definition
if __name__ == '__main__':
    main()


