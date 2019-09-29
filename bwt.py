#!/usr/bin/env python
# coding: utf-8

def bwt(seq):
    #Determine the length of sequence
    len_seq = len(seq)

    #Assigning $ symbol to the end of sequence
    seq_dollar = seq + "$"

    #Empty list to contain combinations of BWT algorithm
    seq_list = []

    for i in range(len_seq,-1,-1):
        temp = seq_dollar[i:]
        seq_list.append(temp + seq[:i])

    #Sorting the list to arrange alphabetically
    seq_list.sort()

    bwt = ''
    for seq in seq_list:
        bwt += seq[-1]
    
    return bwt

def main():
    seq = "TATCGCGCTTT"
    bwt_seq = bwt(seq)
    print("The BWT of " + seq + " is " + bwt_seq)

if __name__ == '__main__':
    main()
