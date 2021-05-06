#LAB 12
#NOTE height is in form of decimals and not feet. Can be considered as smaller version of a metre. 

#UTILITY FUNCTIONS
def getMembershipVals_height(h):
    m_short = -1
    m_meduim = -1
    m_tall = -1
    #for short
    if(h < 5.2):
        m_short  = 1
    elif(5.2<=h<5.7):
        m_short = 11.4 - 2*h
    else:
        m_short = 0
    #for medium
    if(h < 5.5 or h>6.3):
        m_medium  = 0
    elif(5.5<=h<5.9):
        m_medium = (h-5.5)/0.4
    elif(5.9<=h<6.0):
        m_medium = 1
    else:
        m_medium = (6.3-h)/0.3
    
    #for tall
    if(h < 6.0):
        m_tall  = 0
    elif(6.0<=h<6.3):
        m_tall = 2*(h-6.0)
    else:
        m_tall = 1
    return[m_short , m_medium , m_tall]

def getMembershipVals_weight(w):
    m_under = -1
    m_ok = -1
    m_over = -1
    #for under
    if(w < 50):
        m_under  = 1
    elif(50 <= w < 60):
        m_under = 6 - w/10
    else:
        m_under = 0
    #for ok
    if(w < 57 or w > 72):
        m_ok  = 0
    elif(57 >= w > 64):
        m_ok = (w - 57)/7
    elif(69 <= w < 72):
        m_ok = (72  - w)/3
    else:
        m_ok = 1
    
    #for over
    if(w < 70):
        m_over = 0
    elif(70 <= w < 75):
        m_over = 0.2*(w-70)
    else:
        m_over = 1
    return[m_under , m_ok , m_over]
#inputs
height = float(input('Enter height:  '))
weight = float(input('Enter weight:  '))

#Function Calls
height_memberVals = getMembershipVals_height(height)
weight_memberVals = getMembershipVals_weight(weight)

#Displaying Memberships 
print('HIEGHT : short, medium, tall : ',height_memberVals)
print('WEIGHT : under, ok, over     : ', weight_memberVals)


#Defining Rules and printing their Strengths

#RULE 1 : If((Height is Medium or Short) and (Weight is Overweight) then not acceptable
r1_strength = min(max(height_memberVals[0],height_memberVals[1]), weight_memberVals[2])
print('Rule1 Strength:  ',r1_strength)

#RULE 2 : If(Height is Tall) then acceptable
r2_strength = height_memberVals[2]
print('Rule2 Strength:  ',r2_strength)

#RULE 3 : If((Height is Short) and (Weight is OK or Overweight)) then not acceptable
r3_strength = min(height_memberVals[0], max(weight_memberVals[1], weight_memberVals[2]))
print('Rule3 Strength:  ',r3_strength)