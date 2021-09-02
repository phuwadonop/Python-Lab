class Stack :
    def __init__(self):
        self.ls = []

    def __str__(self):
        s = 'stack of '+ str(self.size())+' items : '
        for ele in self.ls:
            s += str(ele)+' '
        return s
    
    def delete(self,i) :
        return self.ls.remove(i)

    def items(self):
        return self.ls

    def push(self,i) :
        self.ls.append(i)

    def isEmpty(self) :
        return self.ls == []
    
    def size(self) :
        return len(self.ls)

    def pop(self) :
        if self.ls == [] :
            print("Don't have item in stack.")
        else : return self.ls.pop()

# /////////////////////////////////////////////
ls_input = input('Enter Input : ').split(',')
s = Stack()

for e in ls_input :
    if e[0] == 'A' : 
        s.push(int(e[2:]))
        print("Add =",int(e[2:]))
    elif e[0] == 'P' : 
        if not s.isEmpty() : 
            print("Pop =",s.pop())
        else : print(-1)
    elif e[0] == 'D' :
        if not s.isEmpty() :
            ls = s.items()
            for i in range(ls.count(int(e[2:]))):
                print("Delete =",int(e[2:]))
                s.delete(int(e[2:]))
        else : print(-1)
    elif e[0] == 'L' : 
        if not s.isEmpty() :
            ls = [ele for ele in s.items() if( ele < int(e[3:]))]
            ls.sort()
            for ele in ls : print("Delete = {} Because {} is less than {}".format(ele,ele,int(e[3:])))
            for ele in ls : s.delete(ele)
        else : print(-1)
    elif e[0] == 'M' : 
        if not s.isEmpty() :
            ls = [ele for ele in s.items() if( ele > int(e[3:]))]
            ls.sort()
            for ele in ls : print("Delete = {} Because {} is more than {}".format(ele,ele,int(e[3:])))
            for ele in ls : s.delete(ele)
        else : print(-1)
print("Value in Stack =",str(s.items()))







