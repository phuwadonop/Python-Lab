def merge_the_tools(string,k) :
    t = []
    i = 0
    while i < len(string) :
        subt = string[i:i+k]
        t.append(subt)
        i += k
    u = []
    for st in t :
        subu = ""
        for i in range(len(st)) :
             if i == 0 : subu = subu + st[i]
             elif st[i] in subu : continue
             else : subu = subu + st[i] 
        u.append(subu)
    print(*u,sep='\n')

string,k = input() , int(input())
merge_the_tools(string,k)


