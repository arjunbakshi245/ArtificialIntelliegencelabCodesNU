
global N 
N = 4
global count
count=0  
def show(board): 
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
        print()   

def isAllow(board, row, col):   
    # Left lane
    for i in range(col): 
        if board[row][i] == 1: 
            return False
  
    # Left Up Diagonal
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    # Left Lower Diagonal 
    for i, j in zip(range(row, N, 1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False  
    return True
  
def placeCheck(board, col):       
    if col >= N: 
        return True  
    for i in range(N):  
        if isAllow(board, i, col):               
            board[i][col] = 1  
            #Recurse to Fulll depth till false, then backtrack
            if placeCheck(board, col + 1) == True:
                global count
                count+=1 
                return True 
            else:
                count+=1  
            board[i][col] = 0
  

def solveProb(): 
    board = [ [0, 0, 0, 0], 
              [0, 0, 0, 0,], 
              [0, 0, 0, 0,],  
              [0, 0, 0, 0,]
               ] 
  
    if(placeCheck(board, 0) == False): 
        print ("No Path") 
        return False  
    show(board)
    print(count) 
    return True
solveProb() 