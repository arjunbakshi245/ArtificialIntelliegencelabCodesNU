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
        print(root.data, root.level) 
    else:
        print(root.data, root.level)

  
    # Process left child  
    print2DUtil(root.left, space)  
  
# Wrapper over print2DUtil()  
def print2D(root) : 
      
    # space=[0] 
    # Pass initial space count as 0  
    print2DUtil(root, 0)  



class Node:
     
    def __init__(self, data , level):
         
        self.data = data
        self.left = None
        self.right = None
        self.level = level
        self.middle = None

#Making the tree
root= Node(6,0)
a = Node(3,1)
b = Node(6,1)
c = Node(5,1)
d = Node(5,2)
e = Node(3,2)
f = Node(6,2)
g = Node(7,2)
h = Node(5,2)
i = Node(8,2)
j = Node(5,3)
k = Node(4,3)
l = Node(3,3)
m = Node(6,3)
n = Node(6,3)
o = Node(7,3)
p = Node(5,3)
q = Node(8,3)
r = Node(6,3)
s = Node(5,4)
t = Node(6,4)
u = Node(7,4)
v = Node(4,4)
w = Node(5,4)
x = Node(3,4)
y = Node(6,4)
z = Node(6,4)
aa = Node(9,4)
ab = Node(7,4)
ac = Node(5,4)
ad = Node(9,4)
ae = Node(8,4)
af = Node(6,4)
root.left=a
root.middle=b
root.right=c
a.left=d
a.right=e
b.left=f
b.right=g
c.left=h
c.right=i
d.left=j
d.right=k
e.right=l
f.left=m
f.right=n
g.left=o
h.left=p
i.left=q
i.right=r
j.left=s
j.right=t
k.left=u
k.middle=v
k.right=w
l.left=x
m.left=y
n.left=z
n.right=aa
o.left=ab
p.left=ac
q.left=ad
q.right=ae
r.left=af


print2D(root)