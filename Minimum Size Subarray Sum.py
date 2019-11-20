''' Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s.
	If there isn't one, return 0 instead.

	Example:
		Input: s = 7, nums = [2,3,1,2,4,3]
		Output: 2
	Explanation: the subarray [4,3] has the minimal length under the problem constraint.
''' 


from itertools import combinations
import numpy as np

def minSubArrayLen(nums, s):
    a=[]
    min=100
    for i in range(2,len(nums)):
        a.append(list(combinations(nums,i)))
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(np.sum(a[i][j])==s):
                if(len(a[i][j])<min):
                    min=len(a[i][j])
            
    if(min==100):
        return(0)
    else:
        return(min)

# Driver Code

nums = [2,3,1,2,4,3,10]
s = 7
print(minSubArrayLen(nums, s))
