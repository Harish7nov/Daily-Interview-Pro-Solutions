'''

class TicTacToe:
    def __init__(self, n,n1=5):
        self.n=n
        self.l=[['' for i in range(self.n)] for j in range(self.n)]

    def move(self, row, col, player):
        if(player==1):
            self.l[row][col]='X'
        elif(player==2):
            self.l[row][col]='O'
        else:
            print("Enter a valid player number!!!")
        for i in range(self.n):
            for j in range(self.n):
                print('|',self.l[i][j],end='')
            print('|')
        print()
        
        countx=counto=0
        
        for i in range(self.n):
            if(self.l[i][i]=='X'):
                countx+=1
            elif(self.l[i][i]=='O'):
                counto+=1
            if(countx==3):
                return(1)
            elif(counto==3):
                return(2)
            else:
                return(0)
        
        for i in range(self.n):
            countx=counto=0
            for j in range(self.n):
                if(self.l[i][j]=='X' or self.l[j][i]=='X'):
                    countx+=1
                elif(self.l[i][j]=='O' or self.l[j][i]=='O'):
                    counto+=1
        if(countx==3):
            return(1)
        elif(counto==3):
            return(2)
        else:
            return(0)

# Driver Code

board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))
