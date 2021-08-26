# ans = []
# def permute (lst,left,right) :
#     if (left == right) : 
#         ans.append(tuple(lst))
#     else :
#         for i in range(left,right) : 
#             lst[left] , lst [i] = lst[i] , lst[left]
#             permute(lst,left+1,right)
#             lst[left] , lst [i] = lst[i] , lst[left]

# print("*** Fun with permute ***")
# input_list = list(input("input : ").split(","))
# print("Collection of distinct numbers : ")

# for i in range(len(input_list)) :
#     input_list[i] = int(input_list[i])

# permute(input_list,0,len(input_list))

# for i in range(len(ans)) : 
#     ans[i] = list(ans[i])

# print(ans)

def addperm(x,l):
    return [ l[0:i] + [x] + l[i:]  for i in range(len(l)+1) ]

def perm(l):
    if len(l) == 0:
        return [[]]
    return [x for y in perm(l[1:]) for x in addperm(l[0],y) ]

print('*** Fun with permute ***')
str_input = input("input : ")
x = (str_input.split(","))
x_ = []
for e in x :
    x_.append(int(e))
print('Original Cofllection:  ',end='')
print(x_)
print('Collection of distinct numbers: ')
number = []
permu = []
x.reverse()
for i in x:
  number.append(int(i))
permu = perm(number)
print(' ',end='')
print(permu)

