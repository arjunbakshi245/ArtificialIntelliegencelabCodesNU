
#Displaying the tree Source - https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/  (not self written, can explain)
COUNT=[10]
def print2DUtil(root, space) : 
  
    # Base case  
    if (root == None) : 
        return
  
    space += COUNT[0]   
    print2DUtil(root.right, space)     
    print()  
    for i in range(COUNT[0], space): 
        print(end = " ") 
    if(root.data==1 or root.data==2):
        if(root.level%2==1):
            val='p2 wins'
        else:
            val='p1 wins'
        print(root.data, root.win) 
    else:
        print(root.data,root.win)
   
    print2DUtil(root.left, space)   
 
def print2D(root) : 
     print2DUtil(root, 0)  


#Utility Function to return  -1 and +1 for alternate layers labeling Min or Max Levels
def gameval(q):
    if(q%2==0):
        return int(-1)
    else:
        return int(1)

#Class Definition
class Node:
     
    def __init__(self, data,level):
         
        self.data = data
        self.left = None
        self.right = None
        self.level = level
        self.win=None

#Creating tree and backtracking along with minmax
def makeTree(root):
    if(root.data==1 or root.data==2):
        root.win=gameval(root.level)
        return 0
    root.left=Node(root.data-1,root.level+1)
    root.right=Node(root.data-2,root.level+1)
    makeTree(root.left)
    makeTree(root.right)
    #if min
    if(root.level%2==1):        
        root.win=min(root.left.win,root.right.win)        
    else:        
        root.win=max(root.left.win,root.right.win)
n=int(input("Enter the number to start the game from:    "))
root=Node(n,0)
print(root.data)
makeTree(root)
print('')
print('')
print2D(root)
