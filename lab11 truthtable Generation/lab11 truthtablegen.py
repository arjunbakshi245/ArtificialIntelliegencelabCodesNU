
#imports
import re
from prettytable import PrettyTable

#====================Utility Functions to be used later in the code=========================

#not operator
def rev(o):
    if(o==1):
        return 0
    else: 
        return 1

#evaluating AND ORs between only 2 entities 
def binop(ex,a,b):
    #processing not operators if any
    if(ex[0][0]=='!'):
        a=rev(a)
    if(ex[2][0]=='!'):
        b=rev(b)
    
    if(ex[1]=='or'):
        return a or b
    elif(ex[1] == 'and'):
        return a and b   

# verifying binop function
#print(binop(['!A','or','B'],0,1))


# Function to evaluate an expresion given in list for strings-space separated with a and b as inputs  (uses binop coded above)
# Returns Clause wise output 
def put_a_b(a,b,seqops):
    
    seqres=[]
    clauses=[a,b]
    for i in range(len(seqops)):
        if(i%2==0):
            out=binop(seqops[i],a,b)
            seqres.append(out)
            clauses.append(out)
        else:
            operator = ' '.join(map(str, seqops[i]))
            seqres.append(operator)
    #print(seqres)
    result = -1 # initialized to -1
    x=int(seqres[0])
    for i in range(0,len(seqres)-2,2):
        if(seqres[i+1]=='or'):
            result = x or int(seqres[i+2])
        else:
            result = x and int(seqres[i+2])
        x = result

    # Apeended in the end for Z as output
    clauses.append(result)
    return clauses



#==================================================MAIN CODE===============================================

strs = "(A and B) or (A or !B)"  # hard coded input for Z
exp = [" ".join(x.split()) for x in re.split(r'[()]',strs) if x.strip()]
vars = [i for i in strs if i.isupper()]
varset=set(vars)
print('The variables included are          : ',varset)
print('Expression is                       : ',exp)
seqops = []
for i in exp:
    sub_exp = [" ".join(x.split()) for x in re.split(r' ',i) if x.strip()]
    seqops.append(sub_exp)
print("Expression broken into smaller exps : ",seqops)
print('')
print('')

final_matrix=[]
for i in range(2):
    for j in range(2):
        final_matrix.append(put_a_b(i,j,seqops))


#=====================Formated using 'prettytable' Library================
x = PrettyTable()
x.field_names = ["A", "B", "Clause1", "Clause2","Z"]
for i in final_matrix:        
    x.add_row(i)
print('Two Clauses ',strs)
print(x)