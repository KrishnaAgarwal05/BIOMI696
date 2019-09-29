#!/usr/bin/env python
# coding: utf-8

import os

def bwt(seq):
    #Determine the length of sequence
    len_seq = len(seq)
    
    #Assigning $ symbol to the end of sequence
    seq_dollar = seq + "$"
    
    #Empty list to contain combinations of BWT algorithm and empty dict to contain the index positions
    seq_list = []
    seq_dict = {}
    
    for i in range(len_seq,-1,-1):
        temp = seq_dollar[i:]
        seq_list.append(temp + seq[:i])
        seq_dict[temp + seq[:i]]  = i
    
    #Sorting the list to arrange alphabetically
    seq_list.sort()
    
    #Empty list to contain index positions of the sorted seq_list
    index_list = []
    
    with open('reference-all.sa','a') as outfile:
        for seq in seq_list:
            index_list.append(seq_dict[seq])
            outfile.write(str(seq_dict[seq])+"\n")
    
    #Empty list to contain even index positions of the sorted seq_list
    even_index_list = []
    
    with open('reference-even.sa','a') as outfile:
        for index in index_list:
            if index%2 == 0:
                even_index_list.append(index)
                outfile.write(str(index)+"\n")
    
    with open('reference.fl','a') as outfile:
        for seq in seq_list:
            outfile.write(seq[0] + '\t' + seq[-1] + '\n')

def main():
    seq = "AATTGCGCGG"
    if os.path.exists("reference-all.sa"):
        os.remove("reference-all.sa")
    if os.path.exists("reference-even.sa"):
        os.remove("reference-even.sa")
    if os.path.exists("reference.fl"):
        os.remove("reference.fl")
    bwt(seq)

if __name__ == '__main__':
    main()
