def odd_list(al) :
    return [e for e in al if e%2 == 1]

print('***Function odd list***')
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ",ls,"\nOutput list : ",opls)