ls = [int(e) for e in input('Enter All Bid : ').split()]
ls.sort()
ls.reverse()
error = False
for i in range(1,len(ls)) :
    if ls[i] == ls[0] :
        error = True
        break

if error == True : print('error : have more than one highest bid')

elif len(ls) == 1 : print('not enough bidder')

else : print('winner bid is',ls[0],'need to pay',ls[1])