'''Given an integer, check if that integer is a palindrome. For this problem do not convert the integer to a string to check if it is a
	palindrome.'''
	
def is_palindrome(n):
    x=[]
    while(n!=0):
        x.append(n%10)
        n=int(n/10)
    if(list(reversed(x))==x):
        return(True)
    else:
        return(False)
		
# Driver code
print(is_palindrome(1234321))

print(is_palindrome(1234322))
