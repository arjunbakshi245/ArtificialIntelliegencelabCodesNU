def gameval(q):
    if(q%2==0):
        return int(-1)
    else:
        return int(1)

COUNT=[10]
def print2DUtil(root, space) : 
  
    # Base case  
    if (root == None) : 
        return
  
    # Increase distance between levels  
    space += COUNT[0] 
  
    # Process right child first  
    print2DUtil(root.right, space)  
  
    # Print current node after space  
    # count  
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
        print(root.data, root.win)

  
    # Process left child  
    print2DUtil(root.left, space)  
  
# Wrapper over print2DUtil()  
def print2D(root) : 
      
    # space=[0] 
    # Pass initial space count as 0  
    print2DUtil(root, 0)  

class Node:
     
    def __init__(self, data,level):
         
        self.data = data
        self.left = None
        self.right = None
        self.level = level
        self.win = None
        self.prev=None


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
        
n=int(input('Enter the number to start from:   '))
root=Node(n,0)
print(root.data)
makeTree(root)
print('')
print('')
print2D(root)
