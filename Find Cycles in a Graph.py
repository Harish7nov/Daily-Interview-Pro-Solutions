



import numpy as np
from itertools import combinations


def findSequence(seq):
    u=[]
    for i in range(2,len(a)):
        u.append(list(combinations(a,i)))
    
    uni=[]
    for i in range(len(u)):
        for j in range(len(u[i])):
            if(len(np.unique(u[i][j])) == 2):
                uni.append(u[i][j])
    
    len1=[]
    for i in range(len(uni)):
        b=uni[i]
        for j in range(0,len(a)-len(b)):
            count=0
            for k in range(len(b)):
                if(b[k]==a[j+k]):
                    count+=1
            if(count==len(b)):
                len1.append(len(b))
    
    print(max(len1))
	

# Driver Code
a=[1, 3, 5, 3, 1, 3, 1, 5]
findSequence(a)
