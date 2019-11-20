''' A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k, we want to figure out after k random moves
	by a knight, the probability that the knight will still be on the chessboard. Once the knight leaves the board it cannot move again and
	will be considered off the board. ''' 
	
	
import random
	
def is_knight_on_board(x, y, k, cache={}):
    steps_out=0
    i=1
    while(i<=k):
        steps_out=0
        x1=x
        y1=y
        c=random.randint(1,8)
        if(c==1):
            # Move 1
            x1+=2
            y1-=1
            if(x1<0 or y1<0):
                print("Out Of Board - 1 in {} move".format(i))
                return(1)
        elif(c==2):
            # Move 2
            x1+=2
            y1+=1
            if(x1<0 or y1<0):
                print("Out Of Board - 2 in {} move".format(i))
                return(1)
        elif(c==3):
            #Move 3
            x1+=1
            y1-=2
            if(x1<0 or y1<0):
                print("Out Of Board - 3 in {} move".format(i))
                return(1)
        elif(c==4):
            #Move 4
            x1+=1
            y1+=2
            if(x1<0 or y1<0):
                print("Out Of Board - 4 in {} move".format(i))
                return(1)
        elif(c==5):
            # Move 5
            x1-=1
            y1-=2
            if(x1<0 or y1<0):
                print("Out Of Board - 5 in {} move".format(i))
                return(1)
        elif(c==6):
            # Move 6
            x1-=1
            y1+=2
            if(x1<0 or y1<0):
                print("Out Of Board - 6 in {} move".format(i))
                return(1)
        elif(c==7):
            # Move 7
            x1-=2
            y1-=1
            if(x1<0 or y1<0):
                print("Out Of Board - 7 in {} move".format(i))
                return(1)
        elif(c==8):
            # Move 8
            x1-=2
            y1+=1
            if(x1<0 or y1<0):
                print("Out Of Board - 8 in {} move".format(i))
                return(1)
        i+=1
    # Move 1
    total_steps=8
    x1+=2
    y1-=1
    if(x1<0 or y1<0):
        steps_out+=1
        print("1")
    
    # Move 2
    x1+=2
    y1+=1
    if(x1<0 or y1<0):
        steps_out+=1
        print("2")
    
    #Move 3
    x1+=1
    y1-=2
    if(x1<0 or y1<0):
        steps_out+=1
        print("3")
    
    #Move 4
    x1+=1
    y1+=2
    if(x1<0 or y1<0):
        steps_out+=1
        print("4")
    
    # Move 5
    x1-=1
    y1-=2
    if(x1<0 or y1<0):
        steps_out+=1
        print("5")
    
    # Move 6
    x1-=1
    y1+=2
    if(x1<0 or y1<0):
        steps_out+=1
        print("6")
    
    # Move 7
    x1-=2
    y1-=1
    if(x1<0 or y1<0):
        steps_out+=1
        print("7")
    
    # Move 8
    x1-=2
    y1+=1
    if(x1<0 or y1<0):
        steps_out+=1
        print("8")
            
    return(steps_out/total_steps)
	
	

# Driver Code

print(is_knight_on_board(0, 0, 1))
