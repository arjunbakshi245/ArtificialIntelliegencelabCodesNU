import random


#initial states
a=2
b=1

for _ in range(20):
    
    #Decision1
    if(a==b):
        pass
    else:
        a=b
        #print(a,b)

    #Decision2
    if(a!=b):
        pass
    else:
        
        if(a==1):
            b=2
        else:
            b=1    

    
    
    print(a,b)
