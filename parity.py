import random

def parity():
    print("What is the number of the bits in the parity?")
    count = int(input())
    plist = []
    x = 0
    for i in range(count):
        x = random.randint(0,1)
        plist.append(x)
    print(plist)
    

    return plist

def even(plist):
    zero = 0
    one = 0
    for i in range(len(plist)):
        if plist[i] == 1:
            one += 1
        else:
            zero += 1
    print("There are", zero ,"zeroes and", one ,"ones")
    # if i divide the number of ones by 2 and get a remainder of 0 ie its divisible by 2
    if one%2 == 0:
        #yes i have even ones - put a 1 in the parity bit
    else:
        #yes i have even ones - put a 1 in the parity bit
    return plist
    
    
#main program starts here
parityList=parity() # argument 
print("Is this parity odd or even?\n'O' for odd and 'E' for even")
oddeven = input().upper()
#while
    if oddeven == "O":
            partityList=odd(parityList)
    elif oddeven == "E":
            partityList=even(parityList)
    else:
        print("Incorrect input")
        print("Is this parity odd or even?\n'O' for odd and 'E' for even")
        oddeven = input().upper()

# printout the partilist with it partiy bit
           
    
