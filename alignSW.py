#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

#Please run the below command after loading anaconda3 but before executing the program
#conda install pandas


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


def NW_alignment_score(S1, S2, val, gap):
    
    #Getting the length of both sequences
    len_S1 = len(S1)
    len_S2 = len(S2)
    
    #Creating an empty data frame
    scores_df = pd.DataFrame(np.nan, index=range(len_S2+1), columns=range(len_S1+1))
    move_df = pd.DataFrame("A", index=range(len_S2+1), columns=range(len_S1+1))
    
    #Initializing cost on all rows in first column
    for i in range(len_S2+1):
        scores_df.iloc[i][0] = 0

    #Initializing cost all columns in first row
    for j in range(len_S1+1):
        scores_df.iloc[0][j] = 0

    for i in range(1,len_S2+1):
        for j in range(1,len_S1+1):
            hor = scores_df.iloc[i][j-1] - gap
            ver = scores_df.iloc[i-1][j] - gap

            if S2[i-1] == S1[j-1]:
                diag = scores_df.iloc[i-1][j-1] + val
            else:
                diag = scores_df.iloc[i-1][j-1] - val

            temp = max([hor,ver,diag])
            if temp < 0:
                temp = 0
            scores_df.iloc[i][j] = temp
            
            move = ""
            if scores_df.iloc[i][j] == hor:
                move += "H"
            if scores_df.iloc[i][j] == diag:
                move += "D"
            if scores_df.iloc[i][j] == ver:
                move += "V"
            move_df.iloc[i][j] = move
    
    #Gives the highest score in the dataframe
    score = scores_df.max().max()
    
    #Finding the closest coordinate of highest score
    closest = [len_S2,len_S1]
    for i in range(1,len_S1):
        temp = scores_df.iloc[i].eq(score).idxmax()
        if temp !=0 and sum([i,temp]) < sum(closest):
            closest[0] = i
            closest[1] = temp
    return move_df,closest


# In[4]:


def find_allignment(S1, S2, move_df,closest):
    #Getting the length of both sequences
    len_S1 = len(S1)
    len_S2 = len(S2)
    
    i = closest[0]
    j = closest[1]
    
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

    
    print(''.join(align_1)[::-1])
    print(''.join(align_2)[::-1])
    print(''.join(align_3)[::-1])
        


# In[5]:


def main():
    seq1 = "TATCGCGCTTT"
    seq2 = "ATTACCGCCGTT"
    val = 1
    gap = 2
    
    move_df, closest = NW_alignment_score(seq1, seq2, val, gap)
    
    print("\nThe alignment is")
    find_allignment(seq1, seq2, move_df,closest)


# In[6]:


if __name__ == '__main__':
    main()


# In[ ]:




