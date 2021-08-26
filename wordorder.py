n = int(input())
ls = []
ls_same_str = []
ls_num_of_occ = []

for i in range(n) : ls.append(input().strip())
set_ls = set(ls)

for i in range(len(ls)) :
    if i == 0 : ls_same_str.append(ls[i])
    elif ls[i] in ls_same_str : continue
    else : ls_same_str.append(ls[i])
    count = 1
    for j in range(i+1,len(ls[i:])) :
        if ls[j] == ls[i] : count += 1
    ls_num_of_occ.append(count)
    
print(len(set_ls))
print(*ls_num_of_occ)


