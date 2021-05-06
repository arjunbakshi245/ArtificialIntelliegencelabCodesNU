
#=============================Uitility Functions========================================

#Function to count total attacks on a particular position given a matrix wrt queen moves
def countAttacks(board, row, col):   
    # Horizontals
    attacks=0
    for i in range(len(board)):
        if(board[i][col]==1):
            attacks+=1
        if(board[row][i]==1):
            attacks+=1
    attacks=attacks-2
  
    # Left Up Diagonal
    for i, j in zip(range(row-1, -1, -1),  
                    range(col-1, -1, -1)): 
        if board[i][j] == 1: 
            attacks+=1 

    # Right Up Diagonal
    for i, j in zip(range(row-1, -1, -1),  
                    range(col+1, len(board), 1)): 
        if board[i][j] == 1: 
            attacks+=1
  
    # Right Lower Diagonal 
    for i, j in zip(range(row+1, len(board), 1),  
                    range(col+1, len(board), 1)): 
        if board[i][j] == 1: 
            attacks+=1  

    # Left Lower Diagonal 
    for i, j in zip(range(row+1, len(board), 1),  
                    range(col-1, -1, -1)): 
        if board[i][j] == 1: 
            attacks+=1  
    return attacks

#For printing
def show(board): 
    for i in range(len(board)): 
        for j in range(len(board)): 
            print (board[i][j], end = " ") 
        print()

#Function to find the position of the queen under maximum threat
def maxattacks(board):
    poss=[]
    att=[]
    for i in range(len(board)):
        for j in range(len(board)):  
            if(board[i][j]==1):
                poss.append([i,j,countAttacks(board,i,j)])
                att.append(countAttacks(board,i,j))
    for i in range(len(att)):
        if att[i]==max(att):
            return [poss[i][0],poss[i][1]]

#Function to collect all possible points to where a queen at (r,c) can move.
def wheretomove(board,row,col):
    moves=[]

    for i in range(len(board)):
        if(board[i][col]==0):
            if(i!=row):
                moves.append([i,col])
        if(board[row][i]==0):
            if(i!=col):
                moves.append([row,i])
    # Left Up Diagonal
    for i, j in zip(range(row-1, -1, -1),  
                    range(col-1, -1, -1)): 
        if board[i][j] == 0: 
            moves.append([i,j]) 

    # Right Up Diagonal
    for i, j in zip(range(row-1, -1, -1),  
                    range(col+1, len(board), 1)): 
        if board[i][j] == 0: 
            moves.append([i,j])
  
    # Right Lower Diagonal 
    for i, j in zip(range(row+1, len(board), 1),  
                    range(col+1, len(board), 1)): 
        if board[i][j] == 0: 
            moves.append([i,j])  

    # Left Lower Diagonal 
    for i, j in zip(range(row+1, len(board), 1),  
                    range(col-1, -1, -1)): 
        if board[i][j] == 0: 
            moves.append([i,j])  
    return(moves)

#Function to calculate heuristic value of a given matrix. 
def heurfunc(board):
    heurval=0
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j]==1):
                heurval+=countAttacks(board,i,j)
    return(heurval)


#=============================Main Code=================================
#Initial Board 4X4 with 4 queens
mat=[
[0,0,0,0],
[1,0,1,0],
[0,1,0,0],
[0,1,0,0]]

#======Core Loop============

k=0
visited=[]
while k<50:
    #Succesfull break
    if(heurfunc(mat)==0):
        print('Goal Node Reached')
        show(mat)
        print('')
        print("Total Moves Required :  ",k)
        break
    #Visted or not
    #if(mat in visited):
    #    print('This position has occcured before. No solution wrt this heuristic')

    #Extracting position of queen under maximum threats
    r=maxattacks(mat)[0]
    c=maxattacks(mat)[1]

    heurvals=[]
    heurwithmoves=[]

    #Extracting possible moves on the board wrt r,c
    possmoves=wheretomove(mat,r,c)
    for i in possmoves:

        #creating possible child matrix
        mat[r][c]=0
        mat[i[0]][i[1]]=1

        #Calulating hueristics of possible child matrix
        val=heurfunc(mat)

        #Restoring to Initial matrix to calculate heuristics for other possible chindren as well
        mat[r][c]=1
        mat[i[0]][i[1]]=0

        heurvals.append(val)
        heurwithmoves.append([i,val])
    
    #Changing matrix for least heuristic(Making a chosen move)
    for i in heurwithmoves:
        if(i[1]==min(heurvals)):
            mat[i[0][0]][i[0][1]]= 1
            mat[r][c]=0
            break

    #Showing each step
    show(mat)
    print('')
    k+=1

    #Add to visited
    visited.append(mat)
#==================End========================== 




