import numpy as np
import pandas as pd
import random
import math
from copy import copy, deepcopy

df = pd.read_csv("Country-data.csv")
df = df.drop(['country'], axis=1)

#==============UTILITY FUNCTIONS=============================
#Distance between points(all dimensions
def findDist(centroid,datapoint):
    d= 0 
    for i in range(len(datapoint)):
        d+= (centroid[i] - datapoint[i])**2
    return math.sqrt(d)


#Compute Cetroid
def compCentroid(j,matrix,df,d):
    numerator   = [0]*d
    denominator = 0
    m=2
    for i in range(len(matrix)):
        for k in range(d):
            numerator[k] += df.iloc[i][k]* (matrix[i][j])**m
    for i in range(len(matrix)):
        denominator+= (matrix[i][j])
    centroid = [number / denominator for number in numerator]

    return centroid

#Initialize Membership Matrix
def initMatrix(n,k):
    mem_matrix = []
    for i in range(n):
        mem = []
        for j in range(k):
            mem.append(random.randrange(0, 1000)/1000)
        mem_matrix.append(mem)
    return mem_matrix

#CAlculating the Fuzzification Factor
def calFuzzFactor(df,i,j,k,C):
    m = 2
    denominator = 0
    for l in range(k):
        denominator += (findDist(df.iloc[i],C[j])/findDist(df.iloc[i],C[l]))**(2/(m-1)) 
    U = denominator**(-1)
    return U 

#Difference value between successive matrixes
def diverge(a,b):
    n = len(a)
    m = len(a[0])
    diff = 0
    for i in range(n):
        for j in range(m):
            diff+=abs(a[i][j]-b[i][j])
    return diff

#Calcluate the Objective Function for each iteration
def calObj(C,df,k):
    m=2
    n= len(df)
    J = 0
    for i in range(n):
        for j in range(k):
            w = calFuzzFactor(df,i,j,k,C)
            J += (w**m)*(findDist(df.iloc[i],C[j]))
    return J

#=======================ALGORITHM===================

mat = initMatrix(167,3)
k = 3
diff =1000
iterations = 0
while(diff>6):
    iterations += 1
    a = deepcopy(mat)
    C=[]
    #Computing Centroids
    for j in range(k):
        C.append(compCentroid(j,a,df,9))
        
    #Computing Membership Matrix
    for i in range(len(mat)):
        for j in range(k):
            mat[i][j] =  calFuzzFactor(df,i,j,k,C)
    diff = diverge(a,mat)
    print("Interation :",iterations ,'   Change in Membership Matrix:  ',diff)
    print('Value of Objective Function: ',calObj(C,df,k))
    print('')
    print('=====================================')
print("Final Centroids",C)
print("Final Membership Matrix" , mat)
