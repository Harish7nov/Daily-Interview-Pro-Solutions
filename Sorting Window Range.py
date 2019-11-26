'''Given a list of numbers, find the smallest window to sort such that the whole list will be sorted. If the list is already sorted return (0, 0). You can assume there will be no duplicate numbers.

	Example:
		Input: [2, 4, 7, 5, 6, 8, 9]
		Output: (2, 4)
Explanation: Sorting the window (2, 4) which is [7, 5, 6] will also means that the whole list is sorted.'''

def min_window_to_sort(nums):
    flag=True
    ind=[]
    for i in range(1,len(nums)):
        if(flag==True):
            if(nums[i-1]<nums[i]):
                pass
            else:
                flag=False
        if(flag==False):
            if(nums[i-1]>nums[i]):
                ind.append(i-1)
            else:
                ind.append(i)
                flag=True
    return(ind[0],ind[-1])
  
 
 # Driver Code
 
 print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
