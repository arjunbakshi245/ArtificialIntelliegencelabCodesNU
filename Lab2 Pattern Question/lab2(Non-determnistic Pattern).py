import random
from Queue import Queue
 

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
        
        ArbitraryStates=[1,2,3]
        PossibleStates=[]
        for i in ArbitraryStates:
            if(i!=a):
                PossibleStates.append(i)
        rand_idx = random.randrange(len(PossibleStates)) 
        b = PossibleStates[rand_idx]
        #print(a,b)
    
   
    
    print(a,b)
