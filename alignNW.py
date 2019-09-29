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
    scores_df = pd.DataFrame(np.nan, index=range(len_S2+1), columns=range(len_S1+1))
    move_df = pd.DataFrame("A", index=range(len_S2+1), columns=range(len_S1+1))
    
    #Initializing cost on all rows in first column
    for i in range(len_S2+1):
        scores_df.iloc[i][0] = i * -2

    #Initializing cost all columns in first row
    for j in range(len_S1+1):
        scores_df.iloc[0][j] = j * -2

    for i in range(1,len_S2+1):
        for j in range(1,len_S1+1):
            hor = scores_df.iloc[i][j-1] - gap
            ver = scores_df.iloc[i-1][j] - gap

            if S2[i-1] == S1[j-1]:
                diag = scores_df.iloc[i-1][j-1] + val
            else:
                diag = scores_df.iloc[i-1][j-1] - val

            scores_df.iloc[i][j] = max([hor,ver,diag])
            
            move = ""
            if scores_df.iloc[i][j] == hor:
                move += "H"
            if scores_df.iloc[i][j] == diag:
                move += "D"
            if scores_df.iloc[i][j] == ver:
                move += "V"
            move_df.iloc[i][j] = move

    score = int(scores_df.iloc[len_S2][len_S1])
    
    return move_df,score

def find_allignment(S1, S2, move_df):
    #Getting the length of both sequences
    len_S1 = len(S1)
    len_S2 = len(S2)
    
    i = len_S2
    j = len_S1
    
    align_1 = []
    align_2 = []
    align_3 = []
    while (i!=0 and j!=0):
        #This for the condition that the pointer reaches first column and due to tie can move vertically
        if j==1 and len(move_df.iloc[i][j]) >1:
            move_df.iloc[i][1] = move_df.iloc[i][1][1:]
            
        if (move_df.iloc[i][j])[0] == "D":
            A1 = S1[j-1]
            A2 = S2[i-1]
            align_1.append(A1)
            align_3.append(A2)
            i -= 1
            j -= 1
            
        elif (move_df.iloc[i][j])[0] == "H":
            A1 = S1[j-1]
            A2 = "-"
            align_1.append(A1)
            align_3.append(A2)
            j -= 1
        elif (move_df.iloc[i][j])[0] == "V":
            A1 = "-"
            A2 = S2[i-1]
            align_1.append(A1)
            align_3.append(A2)
            i -= 1    
            
        #print(A1, A2)
        if A2 == A1:
            align_2.append("|")
        else:
            align_2.append(" ")
            
        #This is the condition where movement doesn't reach to cost 0. Hence we need to capture those in alignment too
        if (i==0 and j!=0) or (i!=0 and j==0):
            if j!=0:
                A1 = S1[j-1]
                A2 = "-"
                align_1.append(A1)
                align_3.append(A2)
            else:
                A1 = "-"
                A2 = S2[i-1]
                align_1.append(A1)
                align_3.append(A2)
            if A2 == A1:
                align_2.append("|")
            else:
                align_2.append(" ")
    
    print(''.join(align_1)[::-1])
    print(''.join(align_2)[::-1])
    print(''.join(align_3)[::-1])

def main():
    seq1 = "TATCGCGCTTT"
    seq2 = "ATTACCGCCGTT"
    val = 1
    gap = 2
    
    move_df, score = NW_alignment_score(seq1, seq2, val, gap)
    print("The alignment score is " + str(score))
    
    print("\nThe alignment is")
    find_allignment(seq1, seq2, move_df)

if __name__ == '__main__':
    main()
