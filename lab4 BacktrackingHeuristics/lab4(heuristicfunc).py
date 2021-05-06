#Arbitrary Start State 
mat=[[1,3,1],
   [1,2,1],
   [2,2,2]]

#Final as Defined in question
final=[[1,1,1],
       [1,2,2],
       [2,2,3]]

#========Fixed heuristic Values of each type of elemnt on the basis of postions=======
#1s
ones=[
[0,0,0],
[0,1,1],
[1,2,2]]

#2
twos=[
[2,1,1],
[1,0,0],
[0,0,1]]

#blank i.e 3
bl=[[4,3,2],[3,2,1],[2,1,0]]

#================Hueristic Function. Sum of minimum manhattan distances of each element(self defined)======
def heur(trix):
    heaurval=0
    for i in range(3):
        for j in range(3):
            if(trix[i][j]==1):
                heaurval+=ones[i][j]
            elif(trix[i][j]==2):
                heaurval+=twos[i][j]
            else:
                heaurval+=bl[i][j]
    return(heaurval)

#=====Utility function for finding coordinates of the blank i.e 3
def findpos(m,e):
    r=0
    for i in range(len(m)):
        if e in m[i]:
            r=i
            c=m[i].index(e)
    return([r,c])

#===============Directional matrix alteration functions===============
#altering matrix to north switch with blank i.e 3
def north(m,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=m[i][j]
    temp=t[r][c]
    t[r][c]=t[r-1][c]
    t[r-1][c]=temp
    return(t)

#Returning new matrix to South switch with blank i.e 3
def south(m,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=m[i][j]
    temp=t[r][c]
    t[r][c]=t[r+1][c]
    t[r+1][c]=temp
    return(t)

#Returning new matrix to east switch with blank i.e 3
def east(m,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=m[i][j]
    temp=t[r][c]
    t[r][c]=t[r][c+1]
    t[r][c+1]=temp
    return(t)
        
#Returning new matrix to West switch with blank i.e 3
def west(m,r,c):
    t=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            t[i][j]=m[i][j]
    temp=t[r][c]
    t[r][c]=t[r][c-1]
    t[r][c-1]=temp    
    return(t)


#================Main code================
visited_states=[]
print('Start: ')
for i in mat:
    print(i)
print('')
print('    ||')

states=[]
k=0
while(k<=20):#limiting only 20 steps
    visited_states.append(mat)
    #Break condition
    if(mat==final):
        break
    p=findpos(mat,3)
    r=p[0]
    c=p[1]
    k+=1
    

    #===Storing each possible child in 'children' list
    children=[]

    #If north possible then append
    if(r>=1):
        new_m= north(mat,r,c)
        children.append([new_m,1])

    #If south possible then append       
    if(r<=1):
        new_m= south(mat,r,c)
        children.append([new_m,2])

    #If west possible then append     
    if(c>=1):
        new_m= west(mat,r,c)
        children.append([new_m,3])

    #If east possible then append        
    if(c<=1):
        new_m= east(mat,r,c)
        children.append([new_m,4])

    #Calculating and storing Heuristic values of each child only if that child has not been visted before.
    heurvals=[]
    deci=[]
    for i in children:
        if i not in visited_states:#if visited then no need to calculate hueristic value at all
            heurvals.append(heur(i[0]))
            deci.append([heur(i[0]),i[1]])
    
    #====If all its children are visited then this path cannot lead to a goal State
    if(len(heurvals)==0):
        print('All children Vistied')
        print('No path exists that leads to the Goal State w.r.t this heuristic function.')
        break
    
    #==Selcting the minimum wrt to heuristics if some children are unvisited
    mini=min(heurvals)

    #Altering matrix wrt to which direction gave the least heuristic value
    for i in deci:
        if(mini==i[0]):
            if(i[1]==1):
                mat= north(mat,r,c)
            elif(i[1]==2):
                mat= south(mat,r,c)
            elif(i[1]==3):
                mat= west(mat,r,c)
            else:
                mat= east(mat,r,c)

    #Output for each iteration
    for i in mat:
        print(i)
    print('')
    print('    ||')
    print('')

    
print('End')          
