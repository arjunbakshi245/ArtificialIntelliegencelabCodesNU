def traverseMatrix(c, row, col, current_row, current_col, currentPath,charge):
    if(charge==current_row + current_col-2):#flag change
        return('Back to entry')
    if(current_row<0 or current_col<0):
        return ""
    if(current_row >= 3 or current_col >= 3):
    # hard coded here, can be made dynamic too
        return ""    
    if(current_row==row-1 and current_col==col-1):
             print(currentPath+"("+str(row-1)+","+str(col-1)+")")
             return ""          
    if(c[current_row][current_col]=='X'):
            return ""
    traverseMatrix(c,row,col,current_row+1,current_col,currentPath+"("+str(current_row)+","+str(current_col)+")->",charge-1)
    traverseMatrix(c,row,col,current_row,current_col+1,currentPath+"("+str(current_row)+","+str(current_col)+")->",charge-1)
    traverseMatrix(c,row,col,current_row+1,current_col+1,currentPath+"("+str(current_row)+","+str(current_col)+")->",charge-1)
    #traverseMatrix(c,row,col,current_row-1,current_col,currentPath+"("+str(current_row)+","+str(current_col)+")->")
    #traverseMatrix(c,row,col,current_row,current_col-1,currentPath+"("+str(current_row)+","+str(current_col)+")->")
charge=6 
p=[['O','O','O'],['O','O','O'],['O','O','X']]
print('The map pre-defined is below :')
for i in p:
    print(i)
print('')
print('Paths are below in coordinate form  : ')
traverseMatrix(p,3,3,0,0,"",charge)
#2,3 goldbox
#4,5 entrypoint
