"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line2=list(line)
    len_line2=len(line2)-1
    for c_i in range(len_line2):
        if(line2[c_i]==0):
            c_j=c_i+1
            while(line2[c_j]==0 and c_j<len_line2):
                c_j=c_j+1
            line2[c_i]=line2[c_j]
            line2[c_j]=0
            
    for c_i in range(len_line2):
        if(line2[c_i]==line2[c_i+1]):
            line2[c_i]=line2[c_i]+line2[c_i+1]
            line2[c_i+1]=0

    for c_i in range(len_line2):
        if(line2[c_i]==0):
            c_j=c_i+1
            while(line2[c_j]==0 and c_j<len_line2):
                c_j=c_j+1
            line2[c_i]=line2[c_j]
            line2[c_j]=0
    return line2


l=[2,2]
print(merge(l))
print(l)
