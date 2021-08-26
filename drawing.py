def print_p1_23(row) :
    if row != 0 : print("+"*(2*row-1),end="")
    if row != 0 : print("*",end="")

print("*** Fun with Drawing ***")
num = int(input("Enter input : "))

# #print piece 1
for row in range(num) :

    #print piece 1/1
    print("."*(num - (row+1)),end="")

    #print piece 1/2
    print("*",end="")
    print_p1_23(row)

    #print picec 1/3 
    if ( 2*(num-2) + 1 ) - (row*2) >= 0 : print("."*( ( 2*(num-2) + 1 ) - (row*2) ),end="")

    #print picec 1/4 
    if row != num - 1 : print("*",end="")
    print_p1_23(row)  

    #print piece 1/5
    print("."*(num - (row+1)),end="\n")

#print piece 2
for row in range(2*num-2) :

    #print piece 2/1
    print("."*(row+1),end="")

    #print piece 2/2
    print("*",end="")
    print("+"*( (4*num-7) - (row*2)) ,end="")
    if row != 2*num - 3 : print("*",end="")

    #print piece 2/3
    print("."*(row+1),end="\n")
    

