def fact(n) : 
    if n == 0 : return 1
    return n*fact(n-1)
    
print('*** Fun with permute ***')
ls_input = [int(e) for e in input('input : ').split(',')]
print('Original Cofllection:  ' + str(ls_input))
print('Collection of distinct numbers: ')
copyList = ls_input
lengOfList = len(ls_input)
storage = []
for i in range(fact(lengOfList)) :
    if i % lengOfList == 0 :
        subList = copyList[:lengOfList-2]
        ls = copyList[lengOfList-2:]
        for ele in ls : subList.insert(0,ele)
        copyList = subList

    else : 
        copyList[(i%lengOfList)-1] , copyList[i%lengOfList] = copyList[i%lengOfList] , copyList[(i%lengOfList)-1]
    storage.append(list(copyList))

print(" " + str(storage))

