#!/usr/bin/env python
# coding: utf-8

#Please run the below command after loading anaconda3 but before executing the program
#conda install pandas

import pandas as pd
import numpy as np

def NW_alignment_score(S1, S2, val, gap):
    
    #Getting the length of both sequences
    len_S1 = len(S1)
    len_S2 = len(S2)
    
    #Creating an empty data frame
    df = pd.DataFrame(np.nan, index=range(len_S2+1), columns=range(len_S1+1))
    
    #Initializing cost on all rows in first column
    for i in range(len_S2+1):
        df.iloc[i][0] = i * -2

    #Initializing cost all columns in first row
    for j in range(len_S1+1):
        df.iloc[0][j] = j * -2

    for i in range(1,len_S2+1):
        for j in range(1,len_S1+1):
            hor = df.iloc[i][j-1] - gap
            ver = df.iloc[i-1][j] - gap

            if S2[i-1] == S1[j-1]:
                diag = df.iloc[i-1][j-1] + val
            else:
                diag = df.iloc[i-1][j-1] - val

            df.iloc[i][j] = max([hor,ver,diag])

    score = int(df.iloc[len_S2][len_S1])
    return score

def main():
    seq1 = "TATCGCGCTTT"
    seq2 = "ATTACCGCCGTT"
    val = 1
    gap = 2
    
    score = NW_alignment_score(seq1, seq2, val, gap)
    print("The alignment score is " + str(score))

if __name__ == '__main__':
    main()
