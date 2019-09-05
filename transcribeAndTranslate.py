#!/usr/bin/env python
# coding: utf-8

# In[6]:


from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


# In[22]:


def transcribe_translate(sequence):
    coding_dna = Seq(sequence, IUPAC.unambiguous_dna)
    print(f"Original Sequence   : {sequence}")
    print(f"Transcribe Sequence : {coding_dna.transcribe()}")
    print(f"Translated Sequence : {coding_dna.translate()}")
    print("\n")


# In[25]:


def main():
    for sequence in ["ATGATTGGCCCGGTTTTTTAA", "GTGGTGGGGAAATTCCGCTGA"]:
        transcribe_translate(sequence)


# In[26]:


if __name__ == '__main__':
    main()


# In[ ]:




