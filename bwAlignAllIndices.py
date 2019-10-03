#!/usr/bin/env python
# coding: utf-8

def index_calc(column_list):
    temp = {}
    
    temp_list =[]
    for x in column_list:
        if x not in temp:
            temp_list.append(x+'0')
            temp[x] = 1
        else:
            temp_list.append(x + str(temp[x]))
            temp[x] = temp[x] + 1
    
    return temp_list

def bwt(seq, p_seq):
    len_seq = len(seq)
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
    
    index_list = []
    first_column = []
    last_column = []
    suffix_array = []
    index_read_start = []
    
    #Retrieving the index data
    with open('reference-all.sa','r') as safiles:
        for safile in safiles:
            index_list.append(safile.strip())
    
    #Retrieving the first and last column data
    with open('reference.fl','r') as flfiles:
        for flfile in flfiles:
            first_column.append(flfile.strip().split('\t')[0])
            last_column.append(flfile.strip().split('\t')[1])
    
    #Determining the suffix array
    for i,x in enumerate(seq_list):
        suffix_array.append(x[:len_seq - int(index_list[i])+1])
    
    #Index for LF mapping
    first_column = index_calc(first_column)
    last_column = index_calc(last_column)
    
    last_dict = {}
    for i in range(len_seq+1):
        last_dict[last_column[i]] = index_list[i]
    
    #Reversing the P sequence
    p_seq = p_seq[::-1]
    
    
    #Calculating the index start read
    for i in range(len_seq+1):
        if p_seq[0]==suffix_array[i][0] and len(p_seq) <= len(suffix_array[i])-1:
            start = index_list[i]
            temp_str = suffix_array[i][0]
            for x in range(len_seq+1):
                #To get the value in last column corresponding the current index start
                for key,val in last_dict.items():
                    if val == start:
                        temp_val = key
                
                #To get the position of temp_val in first column
                for pos,val in enumerate(first_column):
                    if val == temp_val:
                        start = index_list[pos]
                temp_str += temp_val[0]
            
                if temp_str in p_seq:
                    if temp_str == p_seq:
                        index_read_start.append(start)
                        break
                    else:
                        continue
                else:   
                    temp_str=""
    
    return index_read_start

def main():
    seq = "AATTGCGCGG"
    p_seq = "TTGC"
    bwt_index = bwt(seq, p_seq)
    print("The index read start are at the below postion(s):")
    for index in bwt_index:
        print(index)

if __name__ == '__main__':
    main()
