def num_grid(lst) :
    for r in range(len(lst)) :
        for c in range(len(lst)) :
            if(lst[r][c] == '#') :
                for j in range(r+2) :
                    for i in range(c+2) :
                        if i > 4 or j > 4 : continue
                        if i+j >= r+c-2 and i+j <= r+c+2 and abs(c-i) <= 1 and abs(r-j) <= 1 and lst[j][i] != '#' :
                            if lst[j][i] == '-' : lst[j][i] = '1'
                            else : lst[j][i] = str(int(lst[j][i]) + 1)
            elif (lst[r][c] == '-') : lst[r][c] = '0'
            
    return lst

lst_input = []
input_list = input().split(",")

for e in input_list :
    lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep="\n")
print("\n",*num_grid(lst_input),sep="\n")


