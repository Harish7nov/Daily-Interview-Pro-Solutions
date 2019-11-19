'''You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

Your solution should run in linear time.'''

from itertools import combinations

def max_subarray_sum(arr):
    s=[]
    su=[]
    for i in range(2,len(arr)):
        s.append(list(combinations(arr,i))) 
    for i in range(len(s)):
        for j in range(len(s[i])):
            su.append(sum(s[i][j]))
    return(max(su))


 # Driver Code
 
 print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
