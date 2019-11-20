''' You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a
	standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix. '''
	
''' Example:

	[['F', 'A', 'C', 'I'],
	 ['O', 'B', 'Q', 'P'],
	 ['A', 'N', 'O', 'B'],
	 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.'''

def word_search(matrix, word):
    for i in matrix:
        if(word == ''.join(i)):
            return True
        if(word[::-1] == ''.join(i)):
            return True
    for i in range(len(matrix)):
        w=[]
        for j in range(len(matrix[i])):
            w.append(matrix[j][i])
        if(''.join(w) == word):
            return(True)
        if(''.join(w) == word[::-1]):
            return True
    return(False)


# Driver Code

words=[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
print(word_search(words,'MAOF'))
