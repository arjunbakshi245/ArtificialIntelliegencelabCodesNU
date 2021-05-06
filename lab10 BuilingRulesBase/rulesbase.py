#Labeling Rules
'''
soil 
1=>sandy
2=>humous
3=>clay

crop type(c1==>minimum water)
1=>C1
2=>C2
3=>C3
4=>C4
5=>C5

weather
1=>dry
2=>light rain
3=>heavy rain

wetness of soil
1=>very wet
2=> wet
3=> moist
4=> dry
'''
#1. add dont cares
#2. conflict rules

rules=['0,0,1,4','0,0,3,1','1,1,0,0','1,<=3,2,>=3','>=2,<=3,2,>=3','0,<=3,2,>=3','1,4,2,0','>=2,4,2,0','1,<=3,1,>=3','>=2,<=3,1,>=3','0,<=3,1,<=2','>=2,4,1,0','1,<=3,3,>=4','>=2,<=3,3,>=4','0,<=3,3,<=3','1,4,3,>=4','>=2,4,3,>=4']
#rules
def instruction(iput):
    rules=[]
    soil=iput[0]
    crop=iput[1]
    weather=iput[2]
    wetness=iput[3]

    #dont cares
    if(wetness==4 and weather==1):
        rules.append('0,0,1,4')
        print('rule 1 is triggered')
        return('high')
    if(wetness==1 and weather==3):
        rules.append('0,0,3,1')
        print('rule 2 is triggered')
        return('off')
    if(soil==1 and crop==1):
        print('rule 3 is triggered')
        rules.append('1,1,0,0')
        return('high')
    #moderates
    if(weather == 2):
        if(crop<=3):
            if(wetness>=3):
                if(soil==1):
                    print('rule 4 is triggered')
                    rules.append('1,<=3,2,>=3')
                    return'medium'
                else:
                    print('rule 5 is triggered')
                    rules.append('>=2,<=3,2,>=3')
                    return'off'
            else:
                print('rule 6 is triggered')
                rules.append('0,<=3,2,>=3')
                return'off'
        else:
            if(soil==1):
                print('rule 7 is triggered')
                rules.append('1,4,2,0')
                return'medium'
            else:
                print('rule 8 is triggered')
                rules.append('>=2,4,2,0')
                return'off'
    elif(weather == 1):
        if(crop<=3):
            if(wetness>=3):
                if(soil==1):
                    print('rule 9 is triggered')
                    rules.append('1,<=3,1,>=3')
                    return'high'
                else:
                    print('rule 10 is triggered')
                    rules.append('>=2,<=3,1,>=3')
                    return'medium'
            else:
                print('rule 11 is triggered')
                rules.append('0,<=3,1,<=2')
                return'medium'
        else:
            if(soil==1):
                print('rule 12 is triggered')
                rules.append('1,4,1,0')
                return'high'
            else:
                print('rule 13 is triggered')
                rules.append('>=2,4,1,0')
                return'medium'
    else:
        if(crop<=3):
            if(wetness>=4):
                if(soil==1):
                    print('rule 14 is triggered')
                    rules.append('1,<=3,3,>=4')
                    return 'medium'#conflict
                else:
                    print('rule 15 is triggered')
                    rules.append('>=2,<=3,3,>=4')
                    return 'off'
            else:
                print('rule 16 is triggered')
                rules.append('0,<=3,3,<=3')        
                return 'medium'
        else:
            if(soil==1):
                print('rule 17 is triggered')
                rules.append('1,4,3,>=4')
                return 'medium'
            else:
                print('rule 18 is triggered')
                rules.append('>=2,4,3,>=4')
                return 'off'           



print("Don't care => 0")
print('enter the 4 states =  soil,crop,weather,wetness:  ')
iput = list(map(int, input().split()))
pump= instruction(iput)
print('irrigation pump:  ',pump)
add=int(input("Add rule? :"))
if(add==1):
    print('Comma separated rules soil, crop waether, wetness eg(1,3,2,1) or (>=1,3,<=2,4)  0 means dont care: ')
    rule=input('enter string form rule: ')
    if(rule in rules):
        print('Conflicting rule: This rule already exists')
    else:
        rules.append(rule)