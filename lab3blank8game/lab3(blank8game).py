m=[[1,1,3],
   [1,1,2],
   [2,2,2]]

final=[[1,1,2],
       [1,1,2],
       [2,2,3]]

def findpos(m,e):
    r=0
    for i in range(len(m)):
        if e in m[i]:
            r=i
            c=m[i].index(e)
    return([r,c])
#print(findpos(m,3))

def north(m,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=m[i][j]
    temp=t[r][c]
    t[r][c]=t[r-1][c]
    t[r-1][c]=temp
    return(t)
        
#print(north(final,2,2))
    
def south(m,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=m[i][j]
    temp=t[r][c]
    t[r][c]=t[r+1][c]
    t[r+1][c]=temp
    return(t)

def east(m,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=m[i][j]
    temp=t[r][c]
    t[r][c]=t[r][c+1]
    t[r][c+1]=temp
    return(t)
        
def west(m,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=m[i][j]
    #print(t)
    temp=t[r][c]
    t[r][c]=t[r][c-1]
    t[r][c-1]=temp
    
    return(t)
#print(mat)      
#print(east(m,0,0))  


states=[]

def tracepath(mat,st):
    o1,o2,o3,o4=-1,-1,-1,-1
    #print(mat)
    if(mat in states):
        return (-9999999)
    p=findpos(mat,3)
    r=p[0]
    c=p[1]
    
    states.append(mat)
    
    if(mat==final):
        print(st+'   '+str(r)+','+str(c))
        return 1
    
    
    if(r>=1):
        new_m= north(mat,r,c)
        #print(new_m)
        o1 = 1+tracepath(new_m,st+'   '+str(r)+','+str(c))
    if(r<=1):
        new_m= south(mat,r,c)
        o2= 1+tracepath(new_m,st+'   '+str(r)+','+str(c))
    if(c>=1):
        new_m= west(mat,r,c)
        o3= 1+tracepath(new_m,st+'   '+str(r)+','+str(c))
    if(c<=1):
        new_m= east(mat,r,c)
        o4= 1+tracepath(new_m,st+' '+str(r)+','+str(c))
    
    if(o1<0 and o2<0 and o3<0 and o4<0):
        return -9944999
    else:
        return min(o1,o2,o3,o4)
    

print(tracepath(m,'Paths  '))
