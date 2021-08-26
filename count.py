lst_input = input("Enter list number : ").split()
for i in range(len(lst_input)) : lst_input[i] = int(lst_input[i])
ans_lst = []
lst = []
for index in range(len(lst_input) - 1) :
    if lst_input == 0 or lst_input == 1 : continue
    if lst_input[index] == lst_input[index+1] + 1 : 
        sumOfnum = 0
        for j in range(index,index+lst_input[index]) :
            if j == len(lst_input) : break
            else : sumOfnum +=  lst_input[j] + abs(j-index) 
        if sumOfnum == lst_input[index]*lst_input[index] : 
            lst.append(lst_input[index:index+lst_input[index]])
            for i in range(index,index+lst_input[index]) : lst_input[i] = 0
ans_lst.append(lst)
ans_lst.insert(0,len(lst))
print(ans_lst)

